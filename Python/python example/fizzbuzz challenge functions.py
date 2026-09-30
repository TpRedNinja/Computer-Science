# This program will do the fuizzbuzz challenge but use a function

# intro void function
def intro():
    print("This program is the fizzbuzz challenge!")

def fizz_or_buzz_void(num): # general void function
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)

def fizz_or_buzz_return(num): # general void function
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return num

def menu():
    print('\nEnter 1 to solve using a void function')
    print('Enter 2 to solve using a value return function')
    print('Enter 3 to exit')
    # get user choice
    choice = int(input('Choice: '))

    # call the right function based on right input
    if choice == 1:
        for number in range(1,101):
            fizz_or_buzz_void(number)# call our fizzbuzz function
        # call back the menu
        menu() # this loops back the menu again
    elif choice == 2:
        for number in range(1,101):
            line = fizz_or_buzz_return(number)# call our fizzbuzz function
            print(line)
        menu() # this loops back the menu again
    elif choice == 3:
        print('goodbye')
    else:
        print('invalid input')
        menu()

#MAIN function
def main():
    intro()
    menu() # call menu function
    
# call main
main()
