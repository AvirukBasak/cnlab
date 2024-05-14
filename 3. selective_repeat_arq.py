MAX_SEQ_NUM = 100  # Maximum sequence number

num_frames = int(input("Number of frames to send: "))
window_size = int(input("Window size: "))

# Initialize variables
base = 1  # Sequence number of the oldest unacknowledged frame
sent = [False] * (MAX_SEQ_NUM + 1)  # Array to track sent frames
acked = [False] * (MAX_SEQ_NUM + 1)  # Array to track acknowledged frames

while base <= num_frames:
    # Send frames within the window size
    for seqno in range(base, min(base + window_size, num_frames + 1)):
        if not sent[seqno] or not acked[seqno]:
            print(f"Frame {seqno}: SENT")
            sent[seqno] = True

    # Simulate receiving ACKs or TIMEOUTs
    for seqno in range(base, min(base + window_size, num_frames + 1)):
        if sent[seqno] and not acked[seqno]:
            choice = int(input(f"Frame {seqno}: \n"
                               "Enter 1 to send ACK\n"
                               "      2 to trigger TIMEOUT\n"
                               "Choice: "))

            if choice == 1:
                print(f"Frame {seqno}: ACK")
                # Mark frame as acknowledged
                acked[seqno] = True
            elif choice == 2:
                print(f"Frame {seqno}: TIMEOUT")
            else:
                print("Invalid choice")
                # Retry reception of the current frame
                seqno -= 1

    # Slide the window
    while acked[base] and base <= num_frames:
        base += 1

print("Transmission complete")


''' OUTPUT:
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
'''
