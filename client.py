import socket
import os

receive_location = os.path.join("received_files")

HOST = "0.0.0.0"
PORT = 9090

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
filename = input("ENTER WANTED FILE NAME: ")
client.send(filename.encode())
wanted_file = client.recv(1024)
wanted_file_name = client.recv(1024).decode()
with open(os.path.join(receive_location, wanted_file_name), "w") as f:
    for line in wanted_file.decode():
        f.write(line)
        
client.close()