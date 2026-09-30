# This program was made by Harris Domangue for CMSC-201 on Oct. 3rd 2024
# This program will generate every possible 6 letter code so we can analyze  the time complexity of the program

import time # get the time module

# Get passcode from the user
print("Make sure your passcode is 6 characters in length")
code = input("Passcode: ")

# check that the passcode is 6 characters in length
while len(code) != 6:
    print("Error: Make sure your passcode is 6 characters in length")
    code = input("Passcode: ")
START = time.time() # get starting time

# create a key to user
KEY = 'abcdefghijklmnopqrstuvwxyz1234567890'

# use a nested for loop
for letter1 in KEY:
    for letter2 in KEY:
        for letter3 in KEY:
            for letter4 in KEY:
                for letter5 in KEY:
                    for letter6 in KEY:
                        guess = letter1 + letter2 + letter3 + letter4 + letter5 + letter6
                        if guess == code:
                            END = time.time()
                            print(f"Code Guessed in {END-START:.0F} seconds:", guess)


print("Program ended")
