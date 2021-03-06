import json
import pathlib
import sqlite3

from veracode_to_sqlite import model, database


def test_db_init() -> None:
    "Test database initialization"
    inmemory_db = sqlite3.connect(":memory:")
    database.Database(inmemory_db)


def test_db_save() -> None:
    "Test loading a sample scan"
    # Load sample scan from test directory
    sample_scan_path = pathlib.Path(__file__).parent / "sample_results.json"
    with sample_scan_path.open(encoding="utf8") as inf:
        sample_scan = json.load(inf)
    scan = model.Scan.parse(sample_scan)

    # Create an in-memory db
    inmemory_db = sqlite3.connect(":memory:")
    db = database.Database(inmemory_db)

    # Save the sample scan to the in-memory db
    db.save(scan)
