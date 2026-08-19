from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "src" / "collector"
BUILD_DIR = ROOT / "build" / "lambda"
ZIP_PATH = ROOT / "build" / "collector.zip"


def main() -> None:
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)

    BUILD_DIR.mkdir(parents=True)

    shutil.copytree(
        SOURCE_DIR,
        BUILD_DIR / "collector",
        ignore=shutil.ignore_patterns(
            "__pycache__",
            "*.pyc",
        ),
    )

    if ZIP_PATH.exists():
        ZIP_PATH.unlink()

    archive = shutil.make_archive(
        str(ZIP_PATH.with_suffix("")),
        "zip",
        BUILD_DIR,
    )

    print(f"Created Lambda package: {archive}")


if __name__ == "__main__":
    main()