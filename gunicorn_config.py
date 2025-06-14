import multiprocessing

# Server socket
bind = "unix:/var/www/sarthaksinghgaur.me/sarthaksinghgaur.github.io/run/resume-portfolio.sock"
backlog = 2048

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"
worker_connections = 1000
timeout = 30
keepalive = 2

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Process naming
proc_name = "portfolio_app"

# Server mechanics
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

# ASGI specific settings
wsgi_app = "asgi:app" 