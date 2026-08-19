from src.collector.config import get_settings


def test_get_settings(monkeypatch) -> None:
    monkeypatch.setenv(
        "RAW_COST_BUCKET_NAME",
        "test-cost-bucket",
    )

    settings = get_settings()

    assert settings.raw_cost_bucket_name == "test-cost-bucket"