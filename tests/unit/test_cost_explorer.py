from datetime import date
from unittest.mock import Mock
from decimal import Decimal

from src.collector.cost_explorer import CostExplorerClient
from src.collector.cost_explorer import normalize_response


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


def test_normalize_response() -> None:
    response = {
        "ResultsByTime": [
            {
                "Estimated": True,
                "TimePeriod": {
                    "Start": "2026-08-13",
                    "End": "2026-08-14",
                },
                "Groups": [
                    {
                        "Keys": ["Amazon Simple Storage Service"],
                        "Metrics": {
                            "UnblendedCost": {
                                "Amount": "0.0000000001",
                                "Unit": "USD",
                            }
                        },
                    },
                    {
                        "Keys": ["Amazon Elastic Container Registry"],
                        "Metrics": {
                            "UnblendedCost": {
                                "Amount": "0.0000000072",
                                "Unit": "USD",
                            }
                        },
                    },
                ],
            }
        ]
    }

    records = normalize_response(response)

    assert len(records) == 2

    assert records[0].service == "Amazon Simple Storage Service"
    assert records[0].cost == Decimal("0.0000000001")
    assert records[0].currency == "USD"
    assert records[0].estimated is True

    assert records[1].service == "Amazon Elastic Container Registry"
    assert records[1].cost == Decimal("0.0000000072")