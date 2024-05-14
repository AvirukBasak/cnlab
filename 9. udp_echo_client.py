import socket

HOST = 'localhost'
PORT = 8080
MAX_MSG_SIZE = 1024

# Create a socket object
cli_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Get user input
    message = input("Enter message to send (or 'exit' to quit): ")
    # Check for exit command
    if message == 'exit': break
    # Send the message to the server
    cli_sock.sendto(message.encode('utf-8'), (HOST, PORT))
    # Receive response from the server
    data, _ = cli_sock.recvfrom(MAX_MSG_SIZE)
    # Print the echoed message from the server
    print("Received: ", data.decode('utf-8'))

# Close the socket
cli_sock.close()

''' OUTPUT:
Enter message to send (or 'exit' to quit): hi
Received:  hi
Enter message to send (or 'exit' to quit): hello
Received:  hello
Enter message to send (or 'exit' to quit): exit
'''
