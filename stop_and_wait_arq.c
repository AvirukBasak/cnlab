/** Simplified demonstration of Stop and Wait Automatic
Repeat Request (ARQ) Protocol in C */

#include <stdio.h>

int main() {
    int num_frames;

    printf("Number of frames to send: ");
    scanf("%d", &num_frames);

    for (int seqno = 1; seqno <= num_frames; ++seqno) {
        printf("Frame %d: SENT\n", seqno);

        int choice;
        printf(""
            "Enter 1 to send ACK\n"
            "      2 to trigger TIMEOUT\n"
            "Choice: ");
        scanf("%d", &choice);

        switch (choice) {
        case 1:
            // ACK received, send next frame
            printf("Frame %d: ACK\n", seqno);
            continue;
        case 2:
            // TIMEOUT, resend current frame
            printf("Frame %d: TIMEOUT\n", seqno);
            // decrement i to resend the current frame
            seqno--;
            break;
        default:
            printf("Invalid choice\n");
            // decrement i to resend the current frame
            seqno--;
        }
    }
    printf("Transmission complete\n");
    return 0;
}

/** OUTPUT:
Number of frames to send: 4
Frame 1: SENT
Enter 1 to send ACK
      2 to trigger TIMEOUT
Choice: 1
Frame 1: ACK
Frame 2: SENT
Enter 1 to send ACK
      2 to trigger TIMEOUT
Choice: 2
Frame 2: TIMEOUT
Frame 2: SENT
Enter 1 to send ACK
      2 to trigger TIMEOUT
Choice: 2
Frame 2: TIMEOUT
Frame 2: SENT
Enter 1 to send ACK
      2 to trigger TIMEOUT
Choice: 1
Frame 2: ACK
Frame 3: SENT
Enter 1 to send ACK
      2 to trigger TIMEOUT
Choice: 1
Frame 3: ACK
Frame 4: SENT
Enter 1 to send ACK
      2 to trigger TIMEOUT
Choice: 1
Frame 4: ACK
Transmission complete
*/
