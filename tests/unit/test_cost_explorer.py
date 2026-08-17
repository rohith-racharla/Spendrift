from datetime import date
from unittest.mock import Mock

from src.collector.cost_explorer import CostExplorerClient


def test_get_daily_service_costs() -> None:
    mock_client = Mock()

    mock_client.get_cost_and_usage.return_value = {
        "ResultsByTime": [
            {
                "TimePeriod": {
                    "Start": "2026-08-12",
                    "End": "2026-08-13",
                },
                "Groups": [
                    {
                        "Keys": ["Amazon Elastic Compute Cloud - Compute"],
                        "Metrics": {
                            "UnblendedCost": {
                                "Amount": "42.50",
                                "Unit": "USD",
                            }
                        },
                    }
                ],
            }
        ]
    }

    client = CostExplorerClient(client=mock_client)

    result = client.get_daily_service_costs(
        start_date=date(2026, 8, 12),
        end_date=date(2026, 8, 13),
    )

    assert result["ResultsByTime"][0]["Groups"][0]["Metrics"][
        "UnblendedCost"
    ]["Amount"] == "42.50"

    mock_client.get_cost_and_usage.assert_called_once()