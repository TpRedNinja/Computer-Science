# This program was made by Harris Domangue for CMSC-201 on Oct. 17th 2024
# This program will simulate a fighting game
import fightGame as FG

def intro():
    print("This program will simulate a fighting game")

def main():
    intro()
    answer = input("do you want to start? ")
    while answer == "Yes" or answer == "yes" or answer == "YES":
        FG.play()
        answer = input("do you want to play again? ")

    answer = input("do you want to start now? ")

if __name__ == '__main__':
    main()
