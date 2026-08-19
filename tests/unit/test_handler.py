from unittest.mock import Mock

from src.collector import handler


def test_lambda_handler(monkeypatch) -> None:
    mock_cost_explorer = Mock()
    mock_data_store = Mock()

    mock_cost_explorer.get_daily_service_costs.return_value = {
        "ResultsByTime": []
    }

    monkeypatch.setenv(
        "RAW_COST_BUCKET_NAME",
        "test-cost-bucket",
    )

    monkeypatch.setattr(
        handler,
        "CostExplorerClient",
        Mock(return_value=mock_cost_explorer),
    )

    monkeypatch.setattr(
        handler,
        "CostDataStore",
        Mock(return_value=mock_data_store),
    )

    result = handler.lambda_handler(
        event={},
        context=Mock(),
    )

    assert result["status"] == "success"
    assert result["key"].startswith(
        "raw/year="
    )

    mock_cost_explorer.get_daily_service_costs.assert_called_once()
    mock_data_store.put_json.assert_called_once()