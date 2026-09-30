# This program was made by Harris Domangue for CMSC-201 on Sept. 10th 2024
# This program will convert inches to centimeters

# global constant
CONVERT_CENT = 2.54

# display purpose to user
print("This programs will convert inches to centimeters")

# display purpose to user
inches = float(input("enter the number of inches: ")) # get user input

# convert the inches to centimeters
centimeter = inches * CONVERT_CENT

# display the answer to the user
print(f"{inches} inches is converted to {centimeter: ,.1f} cm.")
