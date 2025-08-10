#!/bin/sh
set -euo pipefail
DIR=${1:-certs}
mkdir -p "$DIR"
openssl req -x509 -nodes -newkey rsa:2048 -keyout "$DIR/selfsigned.key" -out "$DIR/selfsigned.crt" -subj "/CN=localhost" -days 365
