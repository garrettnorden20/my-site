#!/bin/sh
set -euo pipefail

sudo apt-get update
sudo apt-get install -y docker docker-compose-plugin git
sudo usermod -aG docker "$USER" || true

REPO_DIR=${1:-$HOME/my-site}
if [ ! -d "$REPO_DIR" ]; then
  git clone https://example.com/my-site.git "$REPO_DIR"
fi
cd "$REPO_DIR"

docker compose -f ops/compose.yaml up -d
