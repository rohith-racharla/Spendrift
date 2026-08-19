from pathlib import Path
from zipfile import ZipFile


def test_lambda_package_contains_handler() -> None:
    package = Path("build/collector.zip")

    assert package.exists()

    with ZipFile(package) as archive:
        names = archive.namelist()

    assert "collector/handler.py" in names
    assert "collector/cost_explorer.py" in names
    assert "collector/pipeline.py" in names