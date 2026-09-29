#!/usr/bin/env python3
"""Snapshot original halscan SARIF severities before any downstream rewrite."""
import json, sys

def main(path):
    doc = json.load(open(path))
    out = []
    for run in doc.get("runs", []):
        for r in run.get("results", []):
            out.append({"ruleId": r.get("ruleId"), "level": r.get("level"),
                        "message": (r.get("message") or {}).get("text")})
    json.dump(out, sys.stdout, indent=2)

if __name__ == "__main__":
    main(sys.argv[1])
