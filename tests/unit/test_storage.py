from unittest.mock import Mock

from src.collector.storage import CostDataStore


def test_put_json() -> None:
    mock_client = Mock()

    store = CostDataStore(
        bucket_name="test-bucket",
        client=mock_client,
    )

    store.put_json(
        key="raw/2026/08/13/costs.json",
        content='{"cost": "42.50"}',
    )

    mock_client.put_object.assert_called_once_with(
        Bucket="test-bucket",
        Key="raw/2026/08/13/costs.json",
        Body=b'{"cost": "42.50"}',
        ContentType="application/json",
    )