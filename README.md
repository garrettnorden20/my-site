# my-site

A self-hosted FastAPI + Caddy stack designed for Raspberry Pi or any Linux host.

## Quickstart

### Development (Linux/x86)

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
make dev
```

### Docker

```sh
make build
make up
```

Visit <http://localhost>.

### Raspberry Pi bootstrap

```sh
curl -fsSL https://example.com/my-site/install_pi.sh | sh
```

## Dynamic DNS

Use DuckDNS:

```sh
ops/scripts/setup_ddns.sh mydomain token
```

## HTTPS

- Public domain: Caddy obtains Let's Encrypt certificates automatically.
- Local: `ops/scripts/cert_self_signed.sh`

## Backups

```sh
make backup
# restore
make restore
```

## Extending

- Add templates in `app/views/`
- Add API routes under `app/api/`
- Create models in `app/models.py` and migration with `alembic revision --autogenerate -m "msg"`
- Scheduled jobs go in `app/tasks/`

## Tests

```sh
make test
make smoke
```
