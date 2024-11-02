import json, requests
import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 8080  # Port to listen on (non-privileged ports are > 1023)

def GET(name, tld):
    with open("src/connections.json") as file:
        o = json.load(file)
        for website in o:
            if website == f"{name}.{tld}":
                return requests.get(o[website]["source"]).text
            
        return None






with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    while True:
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr[0]}:{addr[1]}")
            data = conn.recv(1024).decode()
            spl = data.split(".")
            res = GET(spl[0], spl[1])
            if res == None:
                send = "unknown".encode()
            else:
                send = res.encode()
            conn.sendall(send)