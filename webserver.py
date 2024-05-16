import socket
import sys
import threading
import os
import time

HOST = "127.0.0.1"
PORT = 3000
positive_status = 200
not_found_status = 404

def client_func(conn, addr):
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            decoded_data = data.decode("utf-8").split()
            request_path = decoded_data[1]
            version = decoded_data[2]

            send_str = ""
            if request_path == "/" or os.path.exists(sys.path[0] + '/www/' + request_path):
                with open('www/' + request_path) as f:
                    send_str += f.read()
                data = str.encode(f"{version} {positive_status} Threading id: {len(threading.enumerate()-1)} OK\r\n\r\n{send_str}")
            else:
                data = str.encode(f"{version} {not_found_status} Not Found")

            time.sleep(20) # Checking if threading works
            conn.sendall(data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        print(f"Connected: {addr}")
        thread = threading.Thread(target=client_func, args=(conn, addr))
        thread.start()


