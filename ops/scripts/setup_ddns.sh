#!/bin/sh
set -euo pipefail

if [ $# -lt 2 ]; then
  echo "Usage: $0 <domain> <token>" >&2
  exit 1
fi
DOMAIN=$1
TOKEN=$2
curl "https://www.duckdns.org/update?domains=$DOMAIN&token=$TOKEN&ip="
