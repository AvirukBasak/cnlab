import socket

HOST = '0.0.0.0'
PORT = 8080
MAX_MSG_SIZE = 1024

# create a socket object
srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv_sock.bind((HOST, PORT))
srv_sock.listen(3)

# accept a connection
cli_sock, client_address = srv_sock.accept()

while True:
    data = cli_sock.recv(MAX_MSG_SIZE)
    if not data:
        print("Client disconnected")
        break

    data = data.decode('utf-8')
    print("Received:", data, end='')
    if data[-1] != '\n': print()

    cli_sock.send(data.encode('utf-8'))
    print("Echoed back:", data, end='')
    if data[-1] != '\n': print()

cli_sock.close()
srv_sock.close()

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
