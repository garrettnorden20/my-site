#!/bin/sh
set -euo pipefail
DEST=/mnt/usb/website_backups
mkdir -p "$DEST"
TS=$(date +%Y%m%d%H%M%S)
TAR="$DEST/backup_$TS.tar.gz"
if [ -f data.db ]; then
  tar czf "$TAR" data.db app/static
  sha256sum "$TAR" > "$TAR.sha256"
  echo "Backup written to $TAR"
else
  echo "No database found" >&2
fi
