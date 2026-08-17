from __future__ import annotations

import json
from typing import Iterable

from .cost_explorer import DailyServiceCost


def serialize_cost_records(
    records: Iterable[DailyServiceCost],
) -> str:
    """Serialize normalized cost records to JSON."""

    payload = [
        {
            "date": record.date.isoformat(),
            "service": record.service,
            "cost": format(record.cost, "f"),
            "currency": record.currency,
            "estimated": record.estimated,
        }
        for record in records
    ]

    return json.dumps(
        payload,
        indent=2,
        sort_keys=True,
    )