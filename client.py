import socket
import sys
import asyncio

HOST = "127.0.0.1"
PORT = 3000
PATH = 'index.html'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    str_send = f"GET {PATH} HTTP/1.1"
    s.sendall(str.encode(str_send))
    data = s.recv(1024)

data = data.decode("utf-8")
print(f"{data}")