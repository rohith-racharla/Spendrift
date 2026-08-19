from datetime import date

from src.collector.keys import build_daily_cost_key


def test_build_daily_cost_key() -> None:
    result = build_daily_cost_key(date(2026, 8, 18))

    assert result == (
        "raw/"
        "year=2026/"
        "month=08/"
        "day=18/"
        "service-costs.json"
    )