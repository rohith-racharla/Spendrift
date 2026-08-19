from __future__ import annotations

import os


class Settings:
    """Application configuration loaded from environment variables."""

    def __init__(self) -> None:
        self.raw_cost_bucket_name = os.environ["RAW_COST_BUCKET_NAME"]


def get_settings() -> Settings:
    return Settings()