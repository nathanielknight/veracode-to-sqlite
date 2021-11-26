import json
import pathlib

from veracode_to_sqlite import model

# Empty scan produced by scanning the in-development code for this tool.
EMPTY_SCAN = """{
  "_links": {
    "root": {
      "href": "/"
    },
    "self": {
      "href": "/scans/0d27fa6a-1018-4b35-ae53-05940d553113/findings"
    },
    "help": {
      "href": "https://help.veracode.com/reader/tS9CaFwL4_lbIEWWomsJoA/ovfZGgu96UINQxIuTqRDwg"
    }
  },
  "scan_id": "0d27fa6a-1018-4b35-ae53-05940d553113",
  "scan_status": "SUCCESS",
  "message": "Scan successful. Results size: 42 bytes",
  "modules": [
    "Python files within veracode-to-sqlite.zip"
  ],
  "modules_count": 1,
  "findings": [],
  "pipeline_scan": "21.11.0-0",
  "dev_stage": "DEVELOPMENT"
}
"""


def test_parsing_an_empty_scan():
    raw = json.loads(EMPTY_SCAN)
    model.Scan.parse(raw)


# Partial scan (some findings elided) produced by scanning Open edX.
def test_sample_scan():
    sample_scan_path = pathlib.Path(__file__).parent / "sample_results.json"
    with sample_scan_path.open() as inf:
        raw = json.load(inf)
    model.Scan.parse(raw)