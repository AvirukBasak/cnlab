#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>

#define PORT 8080
#define MAX_MSG_SIZE 1024

int main() {
    int sockfd;
    struct sockaddr_in servaddr, cliaddr;
    char buffer[MAX_MSG_SIZE];
    int n;
    unsigned int addr_len;

    // Creating socket file descriptor
    if ((sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("socket creation failed");
        exit(EXIT_FAILURE);
    }

    memset(&servaddr, 0, sizeof(servaddr));
    memset(&cliaddr, 0, sizeof(cliaddr));

    // Filling server information
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = INADDR_ANY;
    servaddr.sin_port = htons(PORT);

    // Bind the socket with the server address
    if (bind(sockfd, (const struct sockaddr *)&servaddr, sizeof(servaddr)) < 0) {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }

    addr_len = sizeof(cliaddr);  // len is value/result

    while (1) {
        n = recvfrom(sockfd, (char *)buffer, MAX_MSG_SIZE, MSG_WAITALL, (struct sockaddr *)&cliaddr, &addr_len);
        buffer[n] = '\0';
        const int len = strlen(buffer);

        printf("Received: %s", buffer);
        if (buffer[len-1] != '\n') printf("\n");

        sendto(sockfd, (const char *)buffer, strlen(buffer), MSG_CONFIRM, (const struct sockaddr *)&cliaddr, addr_len);
        printf("Echoed back: %s", buffer);
        if (buffer[len-1] != '\n') printf("\n");
    }

    return 0;
}

/* OUTPUT:
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
*/
