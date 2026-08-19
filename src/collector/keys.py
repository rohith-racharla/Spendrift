from __future__ import annotations

from datetime import date


def build_daily_cost_key(collection_date: date) -> str:
    """Build the S3 object key for a daily cost dataset."""

    return (
        f"raw/"
        f"year={collection_date.year:04d}/"
        f"month={collection_date.month:02d}/"
        f"day={collection_date.day:02d}/"
        "service-costs.json"
    )