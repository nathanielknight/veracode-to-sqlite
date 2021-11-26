import json
import pathlib

from veracode_to_sqlite import model

# Empty scan produced by scanning the in-development code for this tool.
def test_parsing_an_empty_scan() -> None:
    empty_scan_path = pathlib.Path(__file__).parent / "empty_results.json"
    with empty_scan_path.open() as inf:
        raw = json.load(inf)
    model.Scan.parse(raw)


# Partial scan (some findings elided) produced by scanning Open edX.
def test_sample_scan() -> None:
    sample_scan_path = pathlib.Path(__file__).parent / "sample_results.json"
    with sample_scan_path.open() as inf:
        raw = json.load(inf)
    model.Scan.parse(raw)
