#UDP client example in python
#use ServerUDP for test

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket Create OK")

target_host = '127.0.0.1'
target_port = '5433'
message = "Hello!!!"

try:
    print('Client: ' + message)
    s.sendto(message.encode(), (target_host, int(target_port)))
    data, serv = s.recvfrom(4096)
    data = data.decode()
    print('Client: ' + data)
finally:
    print("Close client")
    s.close()