import json
import pathlib

from veracode_to_sqlite import model


def test_parsing_an_empty_scan() -> None:
    "Test loading an empty Veracode scan produced by scanning the code for this tool."
    empty_scan_path = pathlib.Path(__file__).parent / "empty_results.json"
    with empty_scan_path.open(encoding="utf8") as inf:
        raw = json.load(inf)
    model.Scan.parse(raw)


def test_sample_scan() -> None:
    "Test loading part of a scan produced by scanning Open edX."
    sample_scan_path = pathlib.Path(__file__).parent / "sample_results.json"
    with sample_scan_path.open(encoding="utf8") as inf:
        raw = json.load(inf)
    model.Scan.parse(raw)
