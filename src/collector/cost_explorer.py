from __future__ import annotations

from datetime import date, timedelta
from typing import Any

import boto3


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


def yesterday() -> date:
    """Return yesterday's date."""

    return date.today() - timedelta(days=1)


def today() -> date:
    """Return today's date."""

    return date.today()