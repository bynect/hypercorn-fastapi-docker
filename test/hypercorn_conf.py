import os
import multiprocessing
import json

workers_per_core = os.getenv("WORKERS_PER_CORE", "1")
use_workers_per_core = float(workers_per_core)

web_concurrency = os.getenv("WEB_CONCURRENCY", None)

max_workers = os.getenv("MAX_WORKERS", None)
if max_workers:
    use_max_workers = int(max_workers)
else:
    use_max_workers = None

host = os.getenv("HOST", "0.0.0.0")
ssl_port = os.getenv("SSL_PORT", "443")
tcp_port = os.getenv("TCP_PORT", "80")

bind_env = os.getenv("BIND", None)
if bind_env:
    use_bind = bind_env
else:
    use_bind = "{0}:{1}".format(host, ssl_port)

insecure_bind_env = os.getenv("INSECURE_BIND", None)
if insecure_bind_env:
    use_insecure_bind = insecure_bind_env
else:
    use_insecure_bind = "{0}:{1}".format(host, tcp_port)

use_log_level = os.getenv("LOG_LEVEL", "info")

cores = multiprocessing.cpu_count()
default_web_concurrency = use_workers_per_core * cores
if web_concurrency:
    use_web_concurrency = int(web_concurrency)
    assert web_concurrency > 0
else:
    use_web_concurrency = max(int(default_web_concurrency), 2)
    if use_max_workers:
        use_web_concurrency = min(use_web_concurrency, use_max_workers)

accesslog_var = os.getenv("ACCESS_LOG", "-")
use_accesslog = accesslog_var or None

errorlog_var = os.getenv("ERROR_LOG", "-")
use_errorlog = errorlog_var or None

use_graceful_timeout = os.getenv("GRACEFUL_TIMEOUT", "120")

use_timeout = os.getenv("TIMEOUT", "120")

use_keepalive = os.getenv("KEEP_ALIVE", "5")

#env
loglevel = use_log_level
workers = use_web_concurrency
bind = use_insecure_bind
errorlog = use_errorlog
accesslog = use_accesslog
graceful_timeout = int(use_graceful_timeout)
ssl_handshake_timeout = int(use_timeout)
keepalive = int(use_keepalive)

log_data = {
    "loglevel": loglevel,
    "workers": workers,
    "bind": bind,
    "graceful_timeout": graceful_timeout,
    "timeout": ssl_handshake_timeout,
    "keepalive": keepalive,
    "errorlog": errorlog,
    "accesslog": accesslog,
    
    "workers_per_core": workers_per_core,
    "use_max_workers": use_max_workers,
    "host": host,
    "port": tcp_port
}

print(json.dumps(log_data, indent = 4), flush=True)
