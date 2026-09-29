# halscan-helpers

Small utilities for post-processing `halscan` SARIF output in CI: preserve original finding
severities when a downstream step rewrites them, and emit a stable summary.

## Why
In some pipelines a later stage rewrites SARIF `level` fields. These helpers snapshot the original
levels first so the as-produced findings can always be recovered.

## Usage
    python preserve_levels.py scan.sarif > scan.original-levels.json

Maintainer: Daniel Kessler (clearaudit)
