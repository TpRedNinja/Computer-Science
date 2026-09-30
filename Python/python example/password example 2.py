# This program was made by Harris Domangue for CMSC-201 on Sept. 19th 2024
# This porgeam will set a password for you!

# user display
print("Create a Password!")

# global constants


# get password from teh user
password = input("Enter a password: ")
password2 = input("Confirm password: ")

# variables to store boolean values
passwords_match = password == password2
is_eight_in_length = len (password) >= 8

if not passwords_match:
    print("Passwords do not match!")
    
if not is_eight_in_length:
    print("Password is not 8 characters long")

if passwords_match and is_eight_in_length:
    print("Password is set!")
