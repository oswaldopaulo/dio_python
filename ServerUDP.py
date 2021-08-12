#UDP server example in python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket Create OK")

server_host = 'localhost'
server_port = '5433'

s.bind((server_host,int(server_port)))

message = "\n Hello client!!!"

while 1:
    data, end = s.recvfrom(4096)

    if data:
        print("Send message")
        s.sendto(data + (message.encode()),end)
