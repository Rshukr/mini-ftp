from utils import find_ranked_matches

import socket
import os

HOST = "0.0.0.0"
PORT = 9090
files_location = os.path.join("fake-filesystem")

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
connection, addr = server.accept()
while True:
    filename = connection.recv(1024).decode()
    try:
        all_files = "\n".join(os.listdir(files_location))
        selected_file_name = find_ranked_matches(all_files, filename)[0][0]
        print(selected_file_name)
        selected_file = open(os.path.join(files_location, selected_file_name), mode="rb")
        connection.sendfile(selected_file)
        selected_file.close()
        connection.send(selected_file_name.encode())
        connection.close()
        break
    except (OSError, IndexError) as e:
        connection.send("FILE DOES NOT EXIST".encode())
        connection.close()
        print(e)
        break
    
    