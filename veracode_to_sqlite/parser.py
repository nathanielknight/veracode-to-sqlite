import json
import typing

from . import model


def _parsefinding(rawscan: typing.Mapping[str, typing.Any]) -> model.Finding:
    return model.Finding(**rawscan)


def parse(scanfile: typing.TextIO) -> model.Scan:
    raw = json.load(scanfile)
    findings = [_parsefinding(r) for r in raw["findings"]]
    return model.Scan(
        scan_id=raw["scan_id"],
        scan_status=raw["scan_status"],
        message=raw["message"],
        modules=raw["modules"],
        findings=findings,
    )
