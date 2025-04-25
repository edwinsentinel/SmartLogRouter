import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 5140))

print("Syslog listening on UDP 5140")
while True:
    data, addr = sock.recvfrom(4096)
    print(f"[{addr}] {data.decode()}")
