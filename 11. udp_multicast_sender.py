import socket

# Multicast address and port
# Uses class D multicast address range
MULTICAST_ADDR = "224.1.1.1"
PORT = 8080

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set the time-to-live for multicast packets (optional)
# ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)

# Get data from terminal and send it over multicast
while True:
    data = input("Send msg (or 'exit' to quit): ")
    if data == 'exit': break
    sock.sendto(data.encode(), (MULTICAST_ADDR, PORT))

# Close the socket
sock.close()

''' OUTPUT:
Send msg (or 'exit' to quit): hi
Send msg (or 'exit' to quit): hello
Send msg (or 'exit' to quit): exit
'''
