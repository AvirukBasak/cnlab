import socket

# Broadcast address and port
PORT = 8080

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', PORT))

# Receive data and print it
print(f"Listening for messages on broadcast port {PORT}...")
while True:
    data, addr = sock.recvfrom(1024)
    print(f"Received {addr}: {data.decode()}")

# Close the socket
sock.close()

''' OUTPUT:
Listening for messages on broadcast port 8080...
Received ('192.168.83.119', 46743): hi
Received ('192.168.83.119', 46743): hello
Received ('192.168.83.119', 46743): it's alive!
^C
'''
