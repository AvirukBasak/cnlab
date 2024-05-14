import socket

HOST = 'localhost'
PORT = 8080
MAX_MSG_SIZE = 1024

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

while True:
    # Get user input
    message = input("Send msg (or 'exit' to quit): ")
    # Check for exit command
    if message == 'exit': break
    # Send the message to the server
    client_socket.send(message.encode('utf-8'))
    # Receive response from the server
    data = client_socket.recv(MAX_MSG_SIZE)
    # Print the echoed message from the server
    print("Received:", data.decode('utf-8'))

# Close the socket
client_socket.close()

''' OUTPUT:
Send msg (or 'exit' to quit): hi
Received: hi
Send msg (or 'exit' to quit): hello
Received: hello
Send msg (or 'exit' to quit): hello there!
Received: hello there!
Send msg (or 'exit' to quit): general kenobi!
Received: general kenobi!
Send msg (or 'exit' to quit): exit
'''
