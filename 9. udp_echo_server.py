import socket

HOST = '0.0.0.0'
PORT = 8080
MAX_MSG_SIZE = 1024

# create a socket object
srv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
srv_sock.bind((HOST, PORT))

while True:
    data, client_address = srv_sock.recvfrom(MAX_MSG_SIZE)
    if not data:
        print("Client disconnected")
        break

    data = data.decode('utf-8')
    print("Received:", data, end='')
    if data[-1] != '\n': print()

    srv_sock.sendto(data.encode('utf-8'), client_address)
    print("Echoed back:", data, end='')
    if data[-1] != '\n': print()

srv_sock.close()

''' OUTPUT:
# server output
Received: hi
Echoed back: hi
Received: hello
Echoed back: hello
^C

# client output
$ nc -u localhost 8080
hi
hi
hello
hello
^C
'''
