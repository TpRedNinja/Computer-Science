# This program will cipher your code in ceasears code
# This program was made by Harris Domangue on Nov 12th 2024 for CMSC-201

import random

Message = input("Enter your message here: ")
total_words = len(Message.split())
while total_words < 4:
    Message = input("Error: Enter your message here: ")

Message = Message.lower()


key = "abcdefghijklmnopqrstuvwxyz"
shift = random.randint(1,26)
message = ""
for letter in Message:
    if letter in key:
        message += key[key.index(letter) - shift]
    else:
        if letter == " ":
            message += " "
            
Message = message
print(shift)
print(f'new message is {Message}')

