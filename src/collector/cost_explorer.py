from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Any

import boto3

@dataclass(frozen=True)
class DailyServiceCost:
    """Normalized daily AWS service cost."""

    date: date
    service: str
    cost: Decimal
    currency: str
    estimated: bool


class CostExplorerClient:
    """Client for retrieving AWS cost and usage data."""

    def __init__(self, client: Any | None = None) -> None:
        self.client = client or boto3.client("ce")

    def get_daily_service_costs(
        self,
        start_date: date,
        end_date: date,
    ) -> dict[str, Any]:
        """Retrieve daily AWS costs grouped by service."""

        response = self.client.get_cost_and_usage(
            TimePeriod={
                "Start": start_date.isoformat(),
                "End": end_date.isoformat(),
            },
            Granularity="DAILY",
            Metrics=["UnblendedCost"],
            GroupBy=[
                {
                    "Type": "DIMENSION",
                    "Key": "SERVICE",
                }
            ],
        )

        return response


def normalize_response(
    response: dict[str, Any],
) -> list[DailyServiceCost]:
    """Convert a Cost Explorer response into normalized records."""

    records: list[DailyServiceCost] = []

    for result in response.get("ResultsByTime", []):
        period_start = date.fromisoformat(
            result["TimePeriod"]["Start"]
        )

        estimated = result.get("Estimated", False)

        for group in result.get("Groups", []):
            service = group["Keys"][0]

            metric = group["Metrics"]["UnblendedCost"]

            records.append(
                DailyServiceCost(
                    date=period_start,
                    service=service,
                    cost=Decimal(metric["Amount"]),
                    currency=metric["Unit"],
                    estimated=estimated,
                )
            )

    return records