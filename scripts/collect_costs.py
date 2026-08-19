from __future__ import annotations

from datetime import date, timedelta

import boto3

from src.collector.config import get_settings
from src.collector.cost_explorer import CostExplorerClient
from src.collector.pipeline import collect_and_store_daily_costs
from src.collector.storage import CostDataStore


def main() -> None:
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

    print(
        f"Stored cost data: "
        f"s3://{settings.raw_cost_bucket_name}/{key}"
    )


if __name__ == "__main__":
    main()