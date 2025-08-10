#!/bin/sh
set -euo pipefail
curl -sf http://localhost/healthz >/dev/null
curl -sf http://localhost/api/v1/sample | grep -q "ok"
echo "smoke OK"
