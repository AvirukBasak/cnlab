import socket

HOST = '0.0.0.0'
PORT = 8080
MAX_MSG_SIZE = 1024

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(3)

# accept a connection
client_socket, client_address = server_socket.accept()

while True:
    data = client_socket.recv(MAX_MSG_SIZE)
    if not data:
        print("Client disconnected")
        break

    data = data.decode('utf-8')
    print("Received:", data, end='')
    if data[-1] != '\n': print()

    client_socket.send(data.encode('utf-8'))
    print("Echoed back:", data, end='')
    if data[-1] != '\n': print()

client_socket.close()
server_socket.close()

''' OUTPUT:
# server output
Received: hi
Echoed back: hi
Received: hello
Echoed back: hello
Received: hello there!
Echoed back: hello there!
Received: general kenobi!
Echoed back: general kenobi!
Client disconnected

# client output
$ nc localhost 8080
hi
hi
hello
hello
hello there!
hello there!
general kenobi!
general kenobi!
^C
'''
