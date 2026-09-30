# This program was made by Harris Domangue for CMSC-201 on Sept. 19th 2024
# This porgeam will ask the user how many college credits they have then tell them if they are a freshman, sophemore, junior, or senior

# Global variables
FRESHMAN = 29
SOPHEMORE = 59
JUNIOR = 89
SENIOR = 119

# Displays to user the purpose of this program
print("This program will tell you if you are a college freshman, sophemore, junior, or senior")

# Gets number of credits user has
User_credits = int(input("How many college credits do you have? "))

# Uses  elif to decide what college level the user is
if User_credits <= FRESHMAN:
    print("You are a college freshman")
elif User_credits > FRESHMAN and User_credits <= SOPHEMORE:
    print("You are a college sophemore")
elif User_credits > SOPHEMORE and User_credits <= JUNIOR:
    print("You are a college junior")
elif User_credits > JUNIOR and User_credits <= SENIOR:
    print("You are a college senior")
else:
    print("You have graduated congrats!")
