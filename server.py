import socket

HOST = ""
PORT = 5050

with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    connection, addr = s.accept()
    with connection:
        print(f"Connected to {addr}")