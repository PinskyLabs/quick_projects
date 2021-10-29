
meeting_code_input = input("Enter your Meeting ID: ")

def meeting_identifier(meeting_code_input):
    a = meeting_code_input[0:3]
    b = meeting_code_input[3:7]
    c = meeting_code_input[7:10]
    meeting_code_input = a + "-" + b + "-" + c
    if meeting_code_input == "abc-defg-hij":
        print("Your meeting ID is " + str(meeting_code_input) + "\nJoining the meeting...\n")
        successfully_joined()
    else:
        print("Entered Meeting ID is incorrect\nPlease try again...\n")
        failed_to_join()

def successfully_joined():
    print("\033[1mSuccessfully joined the meeting\n")
    print("---------------------------")
    print("|                         |")
    print("|                 /       |")
    print("|                /        |")
    print("|               /         |")
    print("|        \     /          |")
    print("|         \   /           |")
    print("|          \ /            |")
    print("|           V             |")
    print("|                         |")
    print("---------------------------\033[0m")

def failed_to_join():
    print("\033[1mFailed to join the meeting\n")
    print("---------------------------")
    print("|                         |")
    print("|          \   /          |")
    print("|           \ /           |")
    print("|            X            |")
    print("|           / \           |")
    print("|          /   \          |")
    print("|                         |")
    print("---------------------------\033[0m")
    
if len(meeting_code_input) == 10:
    meeting_identifier(meeting_code_input)
elif len(meeting_code_input) > 10:
    print("You might have entered more than 10 characters\nPlease check again")
elif len(meeting_code_input) < 10:
    print("You might have entered less than 10 characters\nPlease check again")
else:
    print("Please enter complete 10 characters of your Meeting ID")
