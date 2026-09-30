# This program will add, subtract, multiply, divide, and find the square root and square of numbers
# This program was made by Harris Domangue for CMSC-201 on Oct 8th 2024

import math # import the math module

def intro():
    print('this program can add,subrtract,multiply, and divide 2 numbers')

def menu():
    print('\nEnter 1 to add')
    print('Enter 2 to subtract')
    print('Enter 3 to multiply')
    print('Enter 4 to divide')
    print('Enter 5 to square')
    print('Enter 6 to exit')
    choice = int(input('Enter here: '))
    if choice != 6:
        num1 = float(input('Enter num1 here: '))

        # only if choice is not square root
        if choice != 5:
            num2 = float(input('Enter num 2 here: '))

    # get the choice
    if choice == 1:
        print(num1,"+",num2,"=",add(num1,num2))
    elif choice == 2:
        print(num1,"-",num2,"=",subtract(num1,num2))
    elif choice == 3:
        print(num1,"*",num2,"=",multiply(num1,num2))
    elif choice == 4:
        print(num1,"/",num2,"=",divide(num1,num2))
    elif choice == 5:
        print("The squre root of",num1,'is',math.sqrt(num1))# No function needed uses math module
    elif choice == 6:
        print("Exiting....")
    else:
        print('exit')

    # call back the menu if needed:
    if choice >= 1 and choice <= 5:
        menu()

def add(num1,num2): # return format
    return num1 + num2

def subtrack(num1,num2): # local variable format
    answer = num1 - num2
    return answer

def multiply(num1,num2):
    return num1  * num2

def divide(num1,num2):
    if num2 == 0:
        return "Cannot divide by 0"
    answer = num1 / num2
    return answer

def main():
    intro()
    menu()
    
#call main
if __name__ == '__main__':
    main()
