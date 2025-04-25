import socket
import re
import logging

DESTINATIONS = {
    "ERROR": ("syslog1", 5140),
    "INFO": ("syslog2", 5140),
    "WARNING": ("syslog1", 5140),  # send to both in prod
}

UDP_PORT = 5140
TCP_PORT = 5141
BUFFER_SIZE = 4096

# Local log storage
logging.basicConfig(filename='/logs/router.log', level=logging.INFO)

def parse_level(message):
    for level in DESTINATIONS:
        if level in message:
            return level
    return "UNKNOWN"

def forward_log(msg, level):
    if level in DESTINATIONS:
        host, port = DESTINATIONS[level]
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(msg.encode(), (host, port))
        print(f"Forwarded to {host}:{port}")
    else:
        print("Log level UNKNOWN. Saving locally.")
    logging.info(msg)

def start_udp_listener():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", UDP_PORT))
    print(f"Listening on UDP {UDP_PORT}")
    while True:
        msg, _ = sock.recvfrom(BUFFER_SIZE)
        msg = msg.decode()
        level = parse_level(msg)
        forward_log(msg, level)

def start_tcp_listener():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("0.0.0.0", TCP_PORT))
    sock.listen(5)
    print(f"Listening on TCP {TCP_PORT}")
    while True:
        conn, _ = sock.accept()
        msg = conn.recv(BUFFER_SIZE).decode()
        level = parse_level(msg)
        forward_log(msg, level)
        conn.close()

if __name__ == "__main__":
    from threading import Thread
    Thread(target=start_udp_listener).start()
    Thread(target=start_tcp_listener).start()
