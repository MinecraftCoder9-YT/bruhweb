import os, webbrowser
import socket, sys

def opn(text):
    with open("test.html", "w") as h:
        h.write(text)
        path = os.path.abspath("test.html")
        webbrowser.open(path)



HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 8080  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(sys.argv[1].encode())
    data = s.recv(1024).decode()

opn(data)