# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(b"Hello, world.... sent by client")

#receive data from server and print it
data = s.recv(1024)
print(f"Received {data!r}")

host=127.0.0.1
port=6000
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
s.send(b"clienyt side")
data=client.recv(1024)
print(f"cc{data!r}")