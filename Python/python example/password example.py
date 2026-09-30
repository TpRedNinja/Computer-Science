# This program was made by Harris Domangue for CMSC-201 on Sept. 19th 2024
# This porgeam will set a password for you!

# user display
print("Create a Password!")

# global constants
LENGTH = 8

# get password from teh user
password = input("Enter a password: ")
password2 = input("Confirm password: ")

if password == password2 and len password >= LENGTH:
    print("Password Set!")
else:
    print("Passwords does not meet requirements!")
