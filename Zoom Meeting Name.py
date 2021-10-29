
meeting_name = input("Enter your Zoom username: ")

if len(meeting_name) > 14:
    print("This name will be viewed on your Zoom meeting name: " + ">> " + meeting_name[:14] + "..." + " <<")
else:
    print("This name will be viewed on your meeting name: " + ">> " + meeting_name + " <<")
