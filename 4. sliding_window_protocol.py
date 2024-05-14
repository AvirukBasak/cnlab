num_frames = int(input("Number of frames to send: "))
window_size = int(input("Window size: "))

# Sequence number of the oldest unacknowledged frame
base = 1

# No of frames acknowledged
frames_acked = 0

while base <= num_frames:
    # Move the window by the number of frames acknowledged
    base += frames_acked

    # Send frames within the window size
    for seqno in range(base, min(base + window_size, num_frames + 1)):
        print(f"Frame {seqno}: SENT")

    frames_acked = 0

    # Simulate receiving ACKs or TIMEOUTs
    for seqno in range(base, min(base + window_size, num_frames + 1)):
        choice = int(input(f"Frame {seqno}: \n"
                           "Enter 1 to send ACK\n"
                           "      2 to trigger TIMEOUT\n"
                           "Choice: "))

        if choice == 1:
            print(f"Frame {seqno}: ACK")
            # Count the number of frames acknowledged
            frames_acked += 1
        elif choice == 2:
            print(f"Frame {seqno}: TIMEOUT")
            break
        else:
            print("Invalid choice")
            # retry reception of the current frame
            seqno -= 1

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
'''
