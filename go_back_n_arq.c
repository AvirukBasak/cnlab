/** Simplified demonstration of Go-Back-N Automatic
Repeat Request (ARQ) Protocol in C */

#include <stdio.h>

int main() {
    int num_frames;
    int window_size;

    printf("Number of frames to send: ");
    scanf("%d", &num_frames);

    printf("Window size: ");
    scanf("%d", &window_size);

    // Sequence number of the oldest unacknowledged frame
    int base = 1;

    // No of frames acknowledged
    int frames_acked = 0;

    while (base <= num_frames) {
        // Move the window by the number of frames acknowledged
        base += frames_acked;

        // Send frames within the window size
        for (int seqno = base; seqno < base + window_size && seqno <= num_frames; ++seqno) {
            printf("Frame %d: SENT\n", seqno);
        }

        frames_acked = 0;

        // Simulate receiving ACKs or TIMEOUTs
        for (int seqno = base; seqno < base + window_size && seqno <= num_frames; seqno++) {
            int choice;
            printf("Frame %d: \n"
                "Enter 1 to send ACK\n"
                "      2 to trigger TIMEOUT\n"
                "Choice: ", seqno);
            scanf("%d", &choice);

            switch (choice) {
            case 1:
                printf("Frame %d: ACK\n", seqno);
                // Count the number of frames acknowledged
                frames_acked++;
                break;
            case 2:
                printf("Frame %d: TIMEOUT\n", seqno);
                goto lbl_break_receiver;
            default:
                printf("Invalid choice\n");
                // retry reception of the current frame
                seqno--;
                break;
            }
        }

        lbl_break_receiver: ;
    }

    printf("Transmission complete\n");
    return 0;
}

/* OUTPUT:
Number of frames to send: 100
Window size: 5
Frame 1: SENT
Frame 2: SENT
Frame 3: SENT
Frame 4: SENT
Frame 5: SENT
Frame 1: 
Enter 1 to send ACK
      2 to trigger TIMEOUT
Choice: 1
Frame 1: ACK
Frame 2: 
Enter 1 to send ACK
      2 to trigger TIMEOUT
Choice: 1
Frame 2: ACK
Frame 3: 
Enter 1 to send ACK
      2 to trigger TIMEOUT
Choice: 1
Frame 3: ACK
Frame 4: 
Enter 1 to send ACK
      2 to trigger TIMEOUT
Choice: 1
Frame 4: ACK
Frame 5: 
Enter 1 to send ACK
      2 to trigger TIMEOUT
Choice: 1
Frame 5: ACK
Frame 6: SENT
Frame 7: SENT
Frame 8: SENT
Frame 9: SENT
Frame 10: SENT
Frame 6: 
Enter 1 to send ACK
      2 to trigger TIMEOUT
Choice: 1
Frame 6: ACK
Frame 7: 
Enter 1 to send ACK
      2 to trigger TIMEOUT
Choice: 1
Frame 7: ACK
Frame 8: 
Enter 1 to send ACK
      2 to trigger TIMEOUT
Choice: 2
Frame 8: TIMEOUT
Frame 8: SENT
Frame 9: SENT
Frame 10: SENT
Frame 11: SENT
Frame 12: SENT
Frame 8: 
Enter 1 to send ACK
      2 to trigger TIMEOUT
Choice: 1
Frame 8: ACK
Frame 9: 
Enter 1 to send ACK
      2 to trigger TIMEOUT
Choice: 1
Frame 9: ACK
Frame 10: 
Enter 1 to send ACK
      2 to trigger TIMEOUT
Choice: 2
Frame 10: TIMEOUT
Frame 10: SENT
Frame 11: SENT
Frame 12: SENT
Frame 13: SENT
Frame 14: SENT
Frame 10: 
Enter 1 to send ACK
      2 to trigger TIMEOUT
Choice: ^C
*/
