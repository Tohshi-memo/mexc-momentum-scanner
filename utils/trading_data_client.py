"""Vendored Sakura trading-data gateway client.

Upstream: ``trading-data-infra/python/trading_data_client.py``.
Keep this copy byte-for-byte compatible with the shared client API.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import mimetypes
import os
from pathlib import Path
import re
import secrets
import time
from typing import Any, BinaryIO, Callable, Mapping, Sequence
import urllib.error
import urllib.parse
import urllib.request
import uuid

__all__ = [
    "TradingDataClient",
    "TradingDataError",
    "TradingDataHTTPError",
]

_DATASET_RE = re.compile(r"^[a-z0-9][a-z0-9._-]{0,63}$")
_OBJECT_KEY_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._=/-]{0,511}$")
_EVENT_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{7,127}$")
_SCHEMA_RE = re.compile(r"^[A-Za-z0-9._-]{1,32}$")
_IDEMPOTENCY_RE = re.compile(r"^[A-Za-z0-9._:-]{8,128}$")
_RFC3339_RE = re.compile(
    r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}"
    r"(?:\.[0-9]{1,6})?(?:Z|[+-][0-9]{2}:[0-9]{2})$"
)


class TradingDataError(RuntimeError):
    """Base client error."""


class TradingDataHTTPError(TradingDataError):
    """A non-success response from the ingest gateway."""

    def __init__(
        self,
        status: int,
        message: str,
        response: Mapping[str, Any] | None = None,
    ):
        super().__init__(
            f"trading-data gateway returned HTTP {status}: {message}"
        )
        self.status = status
        self.response = response


class TradingDataClient:
    """HMAC-authenticated client with safe retry and idempotency behavior."""

    def __init__(
        self,
        base_url: str,
        repo: str,
        secret: str | bytes,
        *,
        timeout: float = 30.0,
        max_retries: int = 3,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.repo = repo
        self.secret = (
            secret.encode("utf-8")
            if isinstance(secret, str)
            else bytes(secret)
        )
        self.timeout = timeout
        self.max_retries = max_retries

        parsed = urllib.parse.urlsplit(self.base_url)
        localhost = (parsed.hostname or "").lower() in {
            "localhost",
            "127.0.0.1",
            "::1",
        }
        if parsed.scheme != "https" and not (
            parsed.scheme == "http" and localhost
        ):
            raise ValueError(
                "base_url must use HTTPS "
                "(HTTP is accepted only for localhost tests)."
            )
        if not parsed.netloc or parsed.query or parsed.fragment:
            raise ValueError(
                "base_url must be an origin plus an optional path, "
                "without query or fragment."
            )
        if not re.fullmatch(r"[a-z0-9][a-z0-9_-]{1,63}", repo):
            raise ValueError("repo is invalid.")
        if len(self.secret) < 32:
            raise ValueError("HMAC secret must contain at least 32 bytes.")
        if timeout <= 0 or max_retries < 0 or max_retries > 10:
            raise ValueError("timeout or max_retries is invalid.")

    @classmethod
    def from_env(
        cls,
        *,
        timeout: float = 30.0,
        max_retries: int = 3,
    ) -> "TradingDataClient":
        """Build a client from TD_BASE_URL, TD_REPO, and a secret env/file."""
        base_url = os.environ.get("TD_BASE_URL", "")
        repo = os.environ.get("TD_REPO", "")
        secret_value = os.environ.get("TD_HMAC_SECRET")
        secret_file = os.environ.get("TD_HMAC_SECRET_FILE")
        if secret_value and secret_file:
            raise TradingDataError(
                "Set only one of TD_HMAC_SECRET or TD_HMAC_SECRET_FILE."
            )
        if secret_file:
            try:
                secret_value = (
                    Path(secret_file).read_text(encoding="utf-8").strip()
                )
            except OSError as exc:
                raise TradingDataError(
                    "Unable to read TD_HMAC_SECRET_FILE."
                ) from exc
        if not base_url or not repo or not secret_value:
            raise TradingDataError(
                "TD_BASE_URL, TD_REPO, and TD_HMAC_SECRET "
                "or TD_HMAC_SECRET_FILE are required."
            )
        return cls(
            base_url,
            repo,
            secret_value,
            timeout=timeout,
            max_retries=max_retries,
        )

    def health(self) -> dict[str, Any]:
        """Read the unauthenticated, non-sensitive readiness endpoint."""
        request = urllib.request.Request(
            self.base_url + "/v1/health",
            method="GET",
            headers={
                "Accept": "application/json",
                "User-Agent": "trading-data-client/1.0",
            },
        )
        try:
            with urllib.request.urlopen(
                request,
                timeout=self.timeout,
            ) as response:
                return self._decode_response(response.read(1_048_577))
        except urllib.error.HTTPError as exc:
            self._raise_http_error(exc)
        raise AssertionError("unreachable")

    def ingest_events(
        self,
        events: Sequence[Mapping[str, Any]],
        *,
        schema_version: str = "1",
        idempotency_key: str | None = None,
    ) -> dict[str, Any]:
        """Append a non-empty event batch.

        Reusing an event ID with new content returns 409.
        """
        self._validate_schema_version(schema_version)
        if not events or len(events) > 1_000:
            raise ValueError(
                "events must contain between 1 and 1000 entries."
            )
        for event in events:
            self._validate_event_envelope(event)
        body = json.dumps(
            {"schema_version": schema_version, "events": list(events)},
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        ).encode("utf-8")
        key = self._idempotency_key(idempotency_key)
        return self._request(
            method="POST",
            route="/v1/events",
            content_type="application/json",
            schema_version=schema_version,
            idempotency_key=key,
            body_sha256=hashlib.sha256(body).hexdigest(),
            body_length=len(body),
            body_factory=lambda: body,
        )

    def upload_object(
        self,
        local_path: str | os.PathLike[str],
        dataset: str,
        object_key: str,
        *,
        schema_version: str,
        content_type: str | None = None,
        observed_start: str | None = None,
        observed_end: str | None = None,
        idempotency_key: str | None = None,
    ) -> dict[str, Any]:
        """Stream an immutable .jsonl.gz, .json.gz, or .parquet object."""
        self._validate_schema_version(schema_version)
        self._validate_dataset(dataset)
        self._validate_object_key(object_key)
        if (observed_start is None) != (observed_end is None):
            raise ValueError(
                "observed_start and observed_end must be supplied together."
            )
        if observed_start is not None:
            if not _RFC3339_RE.fullmatch(
                observed_start
            ) or not _RFC3339_RE.fullmatch(observed_end or ""):
                raise ValueError(
                    "observed timestamps must be RFC3339."
                )

        path = Path(local_path)
        if not path.is_file() or path.is_symlink():
            raise ValueError(
                "local_path must be a regular, non-symlink file."
            )
        size = path.stat().st_size
        if size < 1:
            raise ValueError("Object file must not be empty.")
        body_hash = self._sha256_file(path)
        media_type = content_type or self._object_content_type(object_key)
        if "\n" in media_type or "\r" in media_type:
            raise ValueError("content_type is invalid.")

        route = f"/v1/objects/{dataset}/{object_key}"
        key = self._idempotency_key(idempotency_key)
        return self._request(
            method="PUT",
            route=route,
            content_type=media_type,
            schema_version=schema_version,
            idempotency_key=key,
            body_sha256=body_hash,
            body_length=size,
            body_factory=lambda: path.open("rb"),
            observed_start=observed_start or "",
            observed_end=observed_end or "",
        )

    def _request(
        self,
        *,
        method: str,
        route: str,
        content_type: str,
        schema_version: str,
        idempotency_key: str,
        body_sha256: str,
        body_length: int,
        body_factory: Callable[[], bytes | BinaryIO],
        observed_start: str = "",
        observed_end: str = "",
    ) -> dict[str, Any]:
        url = self.base_url + route
        request_path = urllib.parse.urlsplit(url).path
        last_error: BaseException | None = None

        for attempt in range(self.max_retries + 1):
            timestamp = str(int(time.time()))
            nonce = secrets.token_urlsafe(24)
            canonical = self._canonical_string(
                method,
                request_path,
                timestamp,
                nonce,
                idempotency_key,
                body_sha256,
                content_type,
                schema_version,
                observed_start,
                observed_end,
            )
            signature = hmac.new(
                self.secret,
                canonical.encode("utf-8"),
                hashlib.sha256,
            ).hexdigest()
            headers = {
                "Accept": "application/json",
                "Content-Type": content_type,
                "Content-Length": str(body_length),
                "User-Agent": "trading-data-client/1.0",
                "X-TD-Repo": self.repo,
                "X-TD-Timestamp": timestamp,
                "X-TD-Nonce": nonce,
                "X-TD-Idempotency-Key": idempotency_key,
                "X-TD-Body-SHA256": body_sha256,
                "X-TD-Schema-Version": schema_version,
                "X-TD-Observed-Start": observed_start,
                "X-TD-Observed-End": observed_end,
                "X-TD-Signature": f"v1={signature}",
            }
            body = body_factory()
            try:
                request = urllib.request.Request(
                    url,
                    data=body,
                    headers=headers,
                    method=method,
                )
                with urllib.request.urlopen(
                    request,
                    timeout=self.timeout,
                ) as response:
                    raw = response.read(1_048_577)
                    if len(raw) > 1_048_576:
                        raise TradingDataError(
                            "Gateway response exceeded 1 MiB."
                        )
                    return self._decode_response(raw)
            except urllib.error.HTTPError as exc:
                if (
                    exc.code not in {429, 500, 502, 503, 504}
                    or attempt >= self.max_retries
                ):
                    self._raise_http_error(exc)
                last_error = exc
            except (
                urllib.error.URLError,
                TimeoutError,
                OSError,
            ) as exc:
                if attempt >= self.max_retries:
                    raise TradingDataError(
                        "Gateway request failed after retries."
                    ) from exc
                last_error = exc
            finally:
                if hasattr(body, "close"):
                    body.close()
            time.sleep(min(0.5 * (2**attempt), 4.0))

        raise TradingDataError(
            "Gateway request failed after retries."
        ) from last_error

    def _canonical_string(
        self,
        method: str,
        path: str,
        timestamp: str,
        nonce: str,
        idempotency_key: str,
        body_sha256: str,
        content_type: str,
        schema_version: str,
        observed_start: str,
        observed_end: str,
    ) -> str:
        return "\n".join(
            [
                "TD-HMAC-SHA256",
                "v1",
                method.upper(),
                path,
                self.repo,
                timestamp,
                nonce,
                idempotency_key,
                body_sha256.lower(),
                content_type.strip().lower(),
                schema_version,
                observed_start,
                observed_end,
            ]
        )

    @staticmethod
    def _decode_response(raw: bytes) -> dict[str, Any]:
        try:
            value = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise TradingDataError(
                "Gateway returned invalid JSON."
            ) from exc
        if not isinstance(value, dict):
            raise TradingDataError(
                "Gateway returned a non-object JSON response."
            )
        return value

    @staticmethod
    def _raise_http_error(exc: urllib.error.HTTPError) -> None:
        raw = exc.read(1_048_577)
        response: Mapping[str, Any] | None = None
        message = exc.reason or "request failed"
        try:
            value = json.loads(raw.decode("utf-8"))
            if isinstance(value, dict):
                response = value
                error = value.get("error")
                if (
                    isinstance(error, dict)
                    and isinstance(error.get("message"), str)
                ):
                    message = error["message"]
        except (UnicodeDecodeError, json.JSONDecodeError):
            pass
        raise TradingDataHTTPError(
            exc.code,
            str(message),
            response,
        ) from exc

    @staticmethod
    def _sha256_file(path: Path) -> str:
        digest = hashlib.sha256()
        with path.open("rb") as source:
            for chunk in iter(
                lambda: source.read(1024 * 1024),
                b"",
            ):
                digest.update(chunk)
        return digest.hexdigest()

    @staticmethod
    def _object_content_type(object_key: str) -> str:
        if object_key.endswith(".gz"):
            return "application/gzip"
        if object_key.endswith(".parquet"):
            return "application/vnd.apache.parquet"
        guessed, _ = mimetypes.guess_type(object_key)
        return guessed or "application/octet-stream"

    @staticmethod
    def _validate_dataset(dataset: str) -> None:
        if not _DATASET_RE.fullmatch(dataset):
            raise ValueError("dataset is invalid.")

    @staticmethod
    def _validate_object_key(object_key: str) -> None:
        if (
            not _OBJECT_KEY_RE.fullmatch(object_key)
            or "//" in object_key
            or any(
                part in {"", ".", ".."} or part.startswith(".")
                for part in object_key.split("/")
            )
            or not object_key.endswith(
                (".jsonl.gz", ".json.gz", ".parquet")
            )
        ):
            raise ValueError(
                "object_key is invalid or has an unsupported extension."
            )

    @staticmethod
    def _validate_schema_version(schema_version: str) -> None:
        if not _SCHEMA_RE.fullmatch(schema_version):
            raise ValueError("schema_version is invalid.")

    @staticmethod
    def _validate_event_envelope(event: Mapping[str, Any]) -> None:
        required = {
            "event_id",
            "event_type",
            "dataset",
            "source_id",
            "event_time",
            "available_at",
            "payload",
        }
        if not isinstance(event, Mapping) or not required.issubset(event):
            raise ValueError(
                "event is missing required envelope fields."
            )
        if (
            not isinstance(event["event_id"], str)
            or not _EVENT_ID_RE.fullmatch(event["event_id"])
        ):
            raise ValueError("event_id is invalid.")
        if (
            not isinstance(event["dataset"], str)
            or not _DATASET_RE.fullmatch(event["dataset"])
        ):
            raise ValueError("event dataset is invalid.")
        if (
            not isinstance(event["payload"], Mapping)
            or not event["payload"]
        ):
            raise ValueError(
                "event payload must be a non-empty object."
            )

    @staticmethod
    def _idempotency_key(value: str | None) -> str:
        result = value or f"auto-{uuid.uuid4().hex}"
        if not _IDEMPOTENCY_RE.fullmatch(result):
            raise ValueError("idempotency_key is invalid.")
        return result
