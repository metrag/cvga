import json
import socket

host = '192.168.1.140'
port = 8080

SERVER_ADDRESS = (host, port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(SERVER_ADDRESS)
server.listen(0)

#cловарь для хранения данных
data = {
    "latitude" : 0,
    "longitude" : 0,
    "charge" : 0
}

while True:
    client, addr = server.accept()
    content = client.recv(1024)
    client.close()

    bag = content.decode("utf-8")
    bag = bag[:-1]

    data["latitude"] = int(bag[0:8]) / 1000000
    data["longitude"] = int(bag[9:17]) / 1000000
    data["charge"] = int(bag[18:])

    print(bag)

    with open("data.json", "w") as f:
        json.dump(data, f)
