import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")


def load_report():
    assert REPORT_PATH.exists(), "report.json not found"
    with REPORT_PATH.open() as f:
        return json.load(f)


def test_report_exists():
    """Success criterion: the solution generates report.json."""
    assert REPORT_PATH.exists(), "report.json not found"


def test_report_has_required_fields():
    """Success criterion: the report contains the required summary fields."""
    report = load_report()

    assert "total_requests" in report
    assert "unique_ips" in report
    assert "top_path" in report


def test_report_values():
    """Success criterion: the report contains the correct summary values."""
    report = load_report()

    assert report["total_requests"] == 8
    assert report["unique_ips"] == 4
    assert report["top_path"] == "/index.html"