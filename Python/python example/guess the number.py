# This program was made by Harris Domangue for CMSC-201
# This  program will randomly generate a number and the user will need to guess that number.

# rabdom module
import random

# user display
print("This program will randomly generate a number between 1 and 5. You must guess the number!")

# get the users guess
guess = int(input("Enter a number between 1 and 5: "))

# use a while loop for input validation
while guess > 5 or guess < 1:
    print("Error number must be between 1 and 5")
    guess = int(input("Enter a number between 1 and 5: "))
    
# randomly generate a number
computer_number = random.randint(1,5)

if guess == computer_number:
    print("You guess the right number")

# check if the guess was one count away from the generated number
elif guess-computer_number == 1 or computer_number-guess == 1:
    print("So close the number was", computer_number)
else:
    print("You guess the wrong number. The number was", computer_number)
