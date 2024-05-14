import socket

# Multicast address and port
# Uses class D multicast address range
MULTICAST_ADDR = "224.1.1.1"
PORT = 8080

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the multicast address and port
sock.bind(('', PORT))

# Set socket options to join multicast group
mreq = socket.inet_aton(MULTICAST_ADDR) + socket.inet_aton('0.0.0.0')
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# Receive data and print it
print(f"Listening for messages on {MULTICAST_ADDR}:{PORT}...")
while True:
    data, addr = sock.recvfrom(1024)
    print(f"Received {addr}: {data.decode()}")

# Close the socket
sock.close()

''' OUTPUT:
Listening for messages on 224.1.1.1:8080...
Received ('192.168.83.119', 34350): hi
Received ('192.168.83.119', 34350): hello
^C
'''
