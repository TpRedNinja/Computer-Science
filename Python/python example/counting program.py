# This program will count to the number specified by the user

# total count
total = 0

# while loop to iterate over total count
user_input = "y"

while user_input.lower() == "y": # use lower method to convert the string to lower case
    total = total + 1
    # display number and get input from the user.
    print(f"You have counted to {total}")
    user_input = input("would you like to add another number? y for yes and n for no: ")

    while user_input.lower() != "y" and user_input.lower() != "n":
        print("error you can only enter 'y' or 'n'")
        user_input = input("would you like to add another number? y for yes and n for no: ")
print("Program Ended")
