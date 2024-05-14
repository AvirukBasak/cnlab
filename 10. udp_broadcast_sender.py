import socket

# Broadcast address and port
BROADCAST_ADDR = '255.255.255.255'
PORT = 8080

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Get data from terminal and send it over broadcast
while True:
    data = input("Send msg (or 'exit' to quit): ")
    if data == 'exit': break
    sock.sendto(data.encode(), (BROADCAST_ADDR, PORT))

# Close the socket
sock.close()

''' OUTPUT:
Send msg (or 'exit' to quit): hi
Send msg (or 'exit' to quit): hello
Send msg (or 'exit' to quit): it's alive!
Send msg (or 'exit' to quit): exit
'''
