"""
This program was made by Harris Domangue for CMSC-201
This is a program will find if a number is even or ordd
"""
def is_even(num):
    if num == 0: # return true once 0
        return True
    else:
        print("in the even function the number is",num)
        return is_odd(num - 1)

def is_odd(num):
    if num == 0:  # return true once 0
        return False
    else:
        print("in the odd function the number is",num)
        return is_even(num - 1)

# Get user input
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print("is even",is_even(num1))
print()
print("is_odd", is_odd(num2))
