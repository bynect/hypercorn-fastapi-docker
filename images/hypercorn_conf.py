import os
import multiprocessing
import json

tcp_only = os.getenv("TCP_ONLY", None)
ssl_only = os.getenv("SSL_ONLY", None)

assert tcp_only == True and not ssl_only == True

host = os.getenv("HOST", "0.0.0.0")
ssl_port = os.getenv("SSL_PORT", "443")
tcp_port = os.getenv("TCP_PORT", "80")

ssl_bind = "{0}:{1}".format(host, ssl_port)
tcp_bind = "{0}:{1}".format(host, tcp_port)

manual_bind = os.getenv("BIND", None)
manual_insecure_bind = os.getenv("INSECURE_BIND", None)

if tcp_only and not ssl_only:
    if manual_bind:
        use_bind = manual_bind
    else:
        use_bind = tcp_bind

elif ssl_only and not tcp_only:
    if manual_bind:
        use_bind = manual_bind
    else:
        use_bind = ssl_bind

else:
    if manual_bind:
        use_bind = manual_bind
    else:
        use_bind = ssl_bind
    
    if manual_insecure_bind:
        use_insecure_bind = manual_insecure_bind
    else:
        use_insecure_bind = tcp_bind


workers_per_core = os.getenv("WORKERS_PER_CORE", "1")
use_workers_per_core = float(workers_per_core)

web_concurrency = os.getenv("WEB_CONCURRENCY", None)

max_workers = os.getenv("MAX_WORKERS", None)
if max_workers:
    use_max_workers = int(max_workers)
else:
    use_max_workers = None
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


#Hypercorn envs
loglevel = use_log_level
workers = use_web_concurrency
if not tcp_only and not ssl_only:
    insecure_bind = use_insecure_bind
bind = use_bind
errorlog = use_errorlog
accesslog = use_accesslog
graceful_timeout = int(use_graceful_timeout)
ssl_handshake_timeout = int(use_timeout)
keep_alive_timeout = int(use_keepalive)


conf_data = {
    "loglevel": loglevel,
    "workers": workers,
    "bind": bind,
    "insecure_bind": insecure_bind,
    "errorlog": errorlog,
    "accesslog": accesslog,
    "graceful_timeout": graceful_timeout,
    "timeout": ssl_handshake_timeout,
    "keep_alive": keep_alive_timeout,

    "workers_per_core": workers_per_core,
    "max_workers": max_workers,
    "host": host,
    "ssl_port": ssl_port,
    "tcp_port": tcp_port
}

print(json.dumps(conf_data))
