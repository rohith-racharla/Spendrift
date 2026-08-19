from __future__ import annotations

from datetime import date, timedelta

import boto3

from .config import get_settings
from .cost_explorer import CostExplorerClient
from .pipeline import collect_and_store_daily_costs
from .storage import CostDataStore


def lambda_handler(event: dict, context: object) -> dict:
    """AWS Lambda entry point for daily cost collection."""

    settings = get_settings()

    session = boto3.Session()

    cost_explorer_client = CostExplorerClient(
        client=session.client("ce"),
    )

    data_store = CostDataStore(
        bucket_name=settings.raw_cost_bucket_name,
        client=session.client("s3"),
    )

    collection_date = date.today() - timedelta(days=1)

    key = collect_and_store_daily_costs(
        collection_date=collection_date,
        cost_explorer=cost_explorer_client,
        data_store=data_store,
    )

    print(f"Stored cost data: s3://{settings.raw_cost_bucket_name}/{key}")

    return {
        "status": "success",
        "key": key,
    }