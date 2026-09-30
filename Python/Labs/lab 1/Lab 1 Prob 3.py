# This program was made by Harris Domangue for CMSC-201 on Sept. 12th 2024
# This program will convert light years to miles

#Global constants
LYTOMI = 587860000000

# displays to user what this program does
print("This program will convert light years into miles")

# Ask's user for a number of light years
User_LightYears = float(input("Enter a number of light years here: "))

# Calculates the number of miles from light years
Total_Miles = float(User_LightYears * LYTOMI)

# tells the user how many miles equals however much light years they put in
print(f"{User_LightYears:.100f} lightyears equals {Total_Miles:,.100f} Miles")
