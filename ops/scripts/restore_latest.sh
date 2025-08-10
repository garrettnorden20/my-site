#!/bin/sh
set -euo pipefail
SRC=/mnt/usb/website_backups
LATEST=$(ls -1 "$SRC"/backup_*.tar.gz 2>/dev/null | sort | tail -n1)
if [ -z "$LATEST" ]; then
  echo "No backups found" >&2
  exit 1
fi
sha256sum -c "$LATEST.sha256"
tar xzf "$LATEST"
