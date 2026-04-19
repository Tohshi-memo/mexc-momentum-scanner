"""
core/experiment_archive.py
シャドウトレードの月次 gzip アーカイブ I/O

experiments.json を肥大化させないため、古い closed 記録を
data/archive/experiments_YYYY-MM.json.gz に移動する。

archive ファイルは月単位 (closed_at の YYYY-MM) で分かれ、
analyze_experiments.py が hot ファイル + 全 archive を結合して
全期間の分析を行う。

ファイル形式は hot ファイルと同じく {"closed": [...]}。
gzip + JSON なので Python 標準ライブラリだけで読み書きできる。
"""
from __future__ import annotations

import gzip
import json
import logging
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Iterable

logger = logging.getLogger(__name__)

ARCHIVE_DIR = Path("data/archive")
ARCHIVE_PREFIX = "experiments_"   # experiments_YYYY-MM.json.gz


def archive_path_for(month_key: str, base_dir: Path = ARCHIVE_DIR) -> Path:
    """YYYY-MM → data/archive/experiments_YYYY-MM.json.gz"""
    return base_dir / f"{ARCHIVE_PREFIX}{month_key}.json.gz"


def _month_key(iso_timestamp: str) -> str | None:
    """ISO タイムスタンプから YYYY-MM を抽出。失敗時は None。"""
    if not iso_timestamp:
        return None
    try:
        dt = datetime.fromisoformat(iso_timestamp)
    except ValueError:
        return None
    return dt.strftime("%Y-%m")


def _record_month_key(rec: dict) -> str | None:
    """レコードの closed_at / outcome_at / detected_at から月キーを決める。

    ExperimentTrade は `outcome_at`、TradeRecord は `closed_at` を使うので
    どちらでも拾えるようにする。最後の保険として detected_at も見る。
    """
    for field in ("closed_at", "outcome_at", "detected_at"):
        key = _month_key(rec.get(field, ""))
        if key:
            return key
    return None


def append_records(
    records: Iterable[dict],
    base_dir: Path = ARCHIVE_DIR,
) -> dict[str, int]:
    """records を closed_at の月ごとにグルーピングし、各月の gzip に追記する。

    既存アーカイブがあればロードして結合 → 同ファイルに再保存。
    月判定に失敗した record は "unknown" 月のファイルに入れる。

    Returns:
        {"YYYY-MM": 追記件数} の辞書。
    """
    grouped: dict[str, list[dict]] = defaultdict(list)
    for rec in records:
        key = _record_month_key(rec) or "unknown"
        grouped[key].append(rec)

    base_dir.mkdir(parents=True, exist_ok=True)
    added: dict[str, int] = {}

    for key, new_list in grouped.items():
        path = archive_path_for(key, base_dir)
        existing: list[dict] = []
        if path.exists():
            try:
                with gzip.open(path, "rt", encoding="utf-8") as f:
                    data = json.load(f)
                existing = list(data.get("closed", []))
            except Exception as e:
                logger.warning(
                    "Failed to read existing archive %s (%s). Overwriting.",
                    path, e,
                )
                existing = []

        merged = existing + new_list
        payload = {"closed": merged}
        # 書き込み: tmp → rename でアトミック保存
        tmp = path.with_suffix(path.suffix + ".tmp")
        with gzip.open(tmp, "wt", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False)
        tmp.replace(path)
        added[key] = len(new_list)
        logger.info(
            "Archived %d record(s) → %s (total in archive: %d).",
            len(new_list), path, len(merged),
        )
    return added


def load_all_archived(
    base_dir: Path = ARCHIVE_DIR,
) -> list[dict]:
    """data/archive/ 以下の全 gzip から closed レコードを読み込む。

    hot ファイル (experiments.json) と合わせて analyze する想定。
    ファイルが無ければ空リスト。破損ファイルは warn して skip。
    """
    if not base_dir.exists():
        return []
    out: list[dict] = []
    for path in sorted(base_dir.glob(f"{ARCHIVE_PREFIX}*.json.gz")):
        try:
            with gzip.open(path, "rt", encoding="utf-8") as f:
                data = json.load(f)
            out.extend(data.get("closed", []))
        except Exception as e:
            logger.warning("Skipping unreadable archive %s: %s", path, e)
    return out
