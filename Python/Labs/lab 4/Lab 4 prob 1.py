# This program was made by Harris Domangue for CMSC-201 on Oct. 17th 2024
# This program will calculate the Pythagorean theorem

import math

def intro(): # displays to user what this program does
    print("This program will calculate the Pythagorean theorem")

def menu(): # gets user input
    Calculate = int(input("Press 1 to put in your values and press 2 to exit the program: "))
    if Calculate == 1:
        A = float(input("Enter the first value: "))
        B = float(input("Enter the Second value: "))
        return A, B
    elif Calculate < 1 or Calculate > 2:
        print("Error please enter 1 or 2")
        Calculate = int(input("Press 1 to put in your values and press 2 to exit the program: "))
    else:
        print("Good Bye :)")
    
def calc_pyth(A, B): # calculates c^2
    A_square = math.pow(A,2) #squaring A for the formula
    B_square = math.pow(B,2) #squaring B for the formula
    C_squared = A_square + B_square # adds a^2 and b^2
    C = math.sqrt(C_squared) # takeing the square root of C_square
    print(f"The length of c^2 is: {C:.2f} in^2")

def main():
    intro()
    A, B = menu()
    calc_pyth(A, B)

if __name__ == '__main__':
    main()
