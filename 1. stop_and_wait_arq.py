num_frames = int(input("Number of frames to send: "))

seqno = 1
while seqno <= num_frames:
    print(f"Frame {seqno}: SENT")

    choice = int(input(""
                       "Enter 1 to send ACK\n"
                       "      2 to trigger TIMEOUT\n"
                       "Choice: "))

    if choice == 1:
        # ACK received, send next frame
        print(f"Frame {seqno}: ACK")
        seqno += 1
    elif choice == 2:
        # TIMEOUT, resend current frame
        print(f"Frame {seqno}: TIMEOUT")
    else:
        print("Invalid choice")
        # Retry sending the current frame
    # End of the switch case

# End of the for loop

print("Transmission complete")

''' OUTPUT:
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
'''
