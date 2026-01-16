# Deploy (Ubuntu 24.04 LTS) – minimum

## 1) Virtualenv + install

```bash
sudo mkdir -p /opt/techinai-demo/hub
sudo chown -R $USER:$USER /opt/techinai-demo/hub

python -m venv /opt/techinai-demo/hub/.venv
/opt/techinai-demo/hub/.venv/bin/pip install -r requirements.txt
```

## 2) Env

Másold be a `.env.example`-t `.env`-be, állítsd be legalább:

- `SECRET_KEY`
- `ALLOWED_HOSTS`
- a 4 db `*_DEMO_URL` (subdomain vagy path alapján)

## 3) Django

```bash
/opt/techinai-demo/hub/.venv/bin/python manage.py migrate
/opt/techinai-demo/hub/.venv/bin/python manage.py collectstatic --noinput
```

## 4) systemd

- Másold a `deploy/systemd/techinai-hub.service` fájlt ide: `/etc/systemd/system/techinai-hub.service`
- Majd:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now techinai-hub
sudo systemctl status techinai-hub
```

## 5) nginx

- Másold a `deploy/nginx/techinai-hub.conf` fájlt ide: `/etc/nginx/sites-available/techinai-hub.conf`
- Symlink:

```bash
sudo ln -s /etc/nginx/sites-available/techinai-hub.conf /etc/nginx/sites-enabled/techinai-hub.conf
sudo nginx -t
sudo systemctl reload nginx
```

TLS-hez javaslat: certbot (Let's Encrypt).
