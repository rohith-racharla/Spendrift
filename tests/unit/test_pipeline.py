from datetime import date
from unittest.mock import Mock

from src.collector.pipeline import collect_and_store_daily_costs


def test_collect_and_store_daily_costs() -> None:
    mock_cost_explorer = Mock()
    mock_data_store = Mock()

    mock_cost_explorer.get_daily_service_costs.return_value = {
        "ResultsByTime": [
            {
                "Estimated": True,
                "TimePeriod": {
                    "Start": "2026-08-18",
                    "End": "2026-08-19",
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
                    }
                ],
            }
        ]
    }

    key = collect_and_store_daily_costs(
        collection_date=date(2026, 8, 18),
        cost_explorer=mock_cost_explorer,
        data_store=mock_data_store,
    )

    assert key == (
        "raw/"
        "year=2026/"
        "month=08/"
        "day=18/"
        "service-costs.json"
    )

    mock_cost_explorer.get_daily_service_costs.assert_called_once()

    mock_data_store.put_json.assert_called_once()

    stored_key = mock_data_store.put_json.call_args.kwargs["key"]

    assert stored_key == key