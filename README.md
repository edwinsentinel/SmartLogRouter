A lightweight Python-based UDP/TCP log router that:

Accepts log messages over UDP and TCP

Parses the message to determine log level

Routes logs to different syslog servers based on log level (e.g., ERROR vs INFO)

Optionally saves a copy to file or prints to console

All wrapped in a Docker Compose setup

🔍 Sample Logic:

Log Level	Routed To
ERROR	syslog1:5140
INFO	syslog2:5140
WARNING	both
UNKNOWN	local storage
🧱 Stack:
Python (socket, re, logging)

Docker

socat for fake syslog receivers (or simple Python echo servers)

Optional: Flask or FastAPI for a log monitoring API

🧪 Features:
Accept UDP on 5140, TCP on 5141

Regex-based log level detection

Round-robin fallback if destination is unreachable

Basic healthcheck endpoint (/health)

Logs saved locally for auditing

Visualization grafana +Loki

