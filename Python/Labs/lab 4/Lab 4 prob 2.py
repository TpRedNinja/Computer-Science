# This program was made by Harris Domangue for CMSC-201 on Oct. 17th 2024
# This program will randomly choose 3 numbers from 0-9 and if u get any 7's u win some money

import random # import random so program can choose between a random number between 0-9

def intro():
    print("This program is a lucky 7's slot machine")
    input("Press Enter to play")

def lucky_seven(total_earned):
    # gets 3 random numbers and assigns them to variables
    Random_1 = random.randint(0,9)
    Random_2 = random.randint(0,9)
    Random_3 = random.randint(0,9)

    # tells the user what they rolled
    print(f"You rolled: {Random_1}, {Random_2}, {Random_3}")
    
    # checks if user rolled any 7's and if they did how much they earned
    if Random_1 == 7 and Random_2 == 7 and Random_3 == 7:
        game_won = True
        earned = 1000
        print("Congradulations you got 3 7's. You have won $1000.")
    elif (Random_1 == 7 and Random_2 == 7) or (Random_2 == 7 and Random_3 == 7) or (Random_1 == 7 and Random_3 == 7):
        game_won = True
        earned = 100
        print("Congradulations you got 2 7's. You have won $100.")
    elif Random_1 == 7 or Random_2 == 7 or Random_3 == 7:
        game_wom = True
        earned = 10
        print("Congradulations you got 1 7. You have won $10.")
    else:
        game_won = False
        earned = 0
        print("You got 0 7's you won $0")

    total_earned += earned
    print(f"Your total earnings so far are: ${total_earned}")
    
    return total_earned

def play(total_earned):
    total_earned = lucky_seven(total_earned)
    
    # Ask the user if they want to play again
    Answer = int(input("Do you want to play again? Press 1 if you do and press any other number if no: ")) 
    
    # Continue playing while the user presses 1
    while Answer == 1:
        total_earned = lucky_seven(total_earned)
        Answer = int(input("Do you want to play again? Press 1 for yes and 2 for no: "))
    
    # Print total earnings and say goodbye when they exit
    print(f"Goodbye! You earned a total of ${total_earned}.")

def main():
    intro()
    total_earned = 0
    play(total_earned)

if __name__ == '__main__':
    main()
