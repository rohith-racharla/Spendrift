import json
from datetime import date
from decimal import Decimal

from src.collector.cost_explorer import DailyServiceCost
from src.collector.serialization import serialize_cost_records


def test_serialize_cost_records() -> None:
    records = [
        DailyServiceCost(
            date=date(2026, 8, 13),
            service="Amazon Simple Storage Service",
            cost=Decimal("0.0000000001"),
            currency="USD",
            estimated=True,
        )
    ]

    result = serialize_cost_records(records)

    payload = json.loads(result)

    assert payload == [
        {
            "date": "2026-08-13",
            "service": "Amazon Simple Storage Service",
            "cost": "0.0000000001",
            "currency": "USD",
            "estimated": True,
        }
    ]