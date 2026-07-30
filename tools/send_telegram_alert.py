"""Send one operational Telegram alert from a GitHub Actions step."""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from utils.notifier import Notifier


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--message",
        default=os.getenv("TELEGRAM_MESSAGE", ""),
    )
    args = parser.parse_args()
    message = str(args.message).strip()
    if not message:
        print("Telegram message is empty.", file=sys.stderr)
        return 2
    notifier = Notifier()
    if not notifier.telegram_enabled:
        print("Telegram credentials are missing.", file=sys.stderr)
        return 2
    return 0 if notifier.send_telegram_message(message) else 1


if __name__ == "__main__":
    raise SystemExit(main())
