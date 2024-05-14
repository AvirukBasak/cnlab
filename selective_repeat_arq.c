#include <stdio.h>
#include <stdbool.h>

#define MAX_SEQ_NUM 1024

int main() {
    int num_frames;
    int window_size;

    printf("Number of frames to send: ");
    scanf("%d", &num_frames);

    printf("Window size: ");
    scanf("%d", &window_size);

    // Initialize variables
    int base = 1;                      // Sequence number of the oldest unacknowledged frame
    bool sent[MAX_SEQ_NUM] = {false};  // Array to track sent frames
    bool acked[MAX_SEQ_NUM] = {false}; // Array to track acknowledged frames

    while (base <= num_frames) {
        // Send frames within the window size
        for (int seqno = base; seqno < base + window_size && seqno <= num_frames; ++seqno) {
            if (!sent[seqno] || !acked[seqno]) {
                printf("Frame %d: SENT\n", seqno);
                sent[seqno] = true;
            }
        }

        // Simulate receiving ACKs or TIMEOUTs
        for (int seqno = base; seqno < base + window_size && seqno <= num_frames; seqno++) {
            if (sent[seqno] && !acked[seqno]) {
                int choice;
                printf("Frame %d: \n"
                    "Enter 1 to send ACK\n"
                    "      2 to trigger TIMEOUT\n"
                    "Choice: ", seqno);
                scanf("%d", &choice);

                switch (choice) {
                case 1:
                    printf("Frame %d: ACK\n", seqno);
                    // Mark frame as acknowledged
                    acked[seqno] = true;
                    break;
                case 2:
                    printf("Frame %d: TIMEOUT\n", seqno);
                    break;
                default:
                    printf("Invalid choice\n");
                    // Retry reception of the current frame
                    seqno--;
                    break;
                }
            }
        }

        // Slide the window
        while (acked[base] && base <= num_frames) {
            base++;
        }
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
Frame 9: 
Enter 1 to send ACK
      2 to trigger TIMEOUT
Choice: 2
Frame 9: TIMEOUT
Frame 10: 
Enter 1 to send ACK
      2 to trigger TIMEOUT
Choice: 1
Frame 10: ACK
Frame 8: SENT
Frame 9: SENT
Frame 11: SENT
Frame 12: SENT
Frame 8: 
Enter 1 to send ACK
      2 to trigger TIMEOUT
Choice: 2
Frame 8: TIMEOUT
Frame 9: 
Enter 1 to send ACK
      2 to trigger TIMEOUT
Choice: 2
Frame 9: TIMEOUT
Frame 11: 
Enter 1 to send ACK
      2 to trigger TIMEOUT
Choice: 2
Frame 11: TIMEOUT
Frame 12: 
Enter 1 to send ACK
      2 to trigger TIMEOUT
Choice: 2
Frame 12: TIMEOUT
Frame 8: SENT
Frame 9: SENT
Frame 11: SENT
Frame 12: SENT
Frame 8: 
Enter 1 to send ACK
      2 to trigger TIMEOUT
Choice: ^C
*/
