from __future__ import annotations

from datetime import date, timedelta

from .cost_explorer import CostExplorerClient, normalize_response
from .keys import build_daily_cost_key
from .serialization import serialize_cost_records
from .storage import CostDataStore


def collect_and_store_daily_costs(
    collection_date: date,
    cost_explorer: CostExplorerClient,
    data_store: CostDataStore,
) -> str:
    """Collect one day's cost data and store it in S3."""

    start_date = collection_date
    end_date = collection_date + timedelta(days=1)

    response = cost_explorer.get_daily_service_costs(
        start_date=start_date,
        end_date=end_date,
    )

    records = normalize_response(response)

    content = serialize_cost_records(records)

    key = build_daily_cost_key(collection_date)

    data_store.put_json(
        key=key,
        content=content,
    )

    return key