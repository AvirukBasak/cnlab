#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>

#define PORT 8080
#define MAX_MSG_SIZE 1024

int main() {
    int server_fd, new_socket;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);
    char buffer[MAX_MSG_SIZE] = {0};

    // Creating socket file descriptor
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }

    // Forcefully attaching socket to the port 8080
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt))) {
        perror("setsockopt");
        exit(EXIT_FAILURE);
    }
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    // Forcefully attaching socket to the port 8080
    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address))<0) {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }
    if (listen(server_fd, 3) < 0) {
        perror("listen failed");
        exit(EXIT_FAILURE);
    }
    if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&addrlen))<0) {
        perror("accept failed");
        exit(EXIT_FAILURE);
    }

    while(1) {
        recv(new_socket, buffer, MAX_MSG_SIZE, 0);
        const int len = strlen(buffer);
        if (len == 0) {
            printf("Client disconnected\n");
            break;
        }

        printf("Received: %s", buffer);
        if (buffer[len-1] != '\n') printf("\n");

        send(new_socket, buffer, len, 0);
        printf("Echoed back: %s", buffer);
        if (buffer[len-1] != '\n') printf("\n");

        memset(buffer, 0, sizeof(buffer));
    }

    return 0;
}

/* OUTPUT:
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
*/
