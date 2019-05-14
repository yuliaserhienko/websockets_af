import socket
import statistics


HOST = '127.0.0.1'
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('ws://127.0.0.1:8000/notify/', ))
    # s.connect((HOST, PORT))
    # while True:
    # data = s.recv(1024)
    s.sendall(b'Hello, world')
