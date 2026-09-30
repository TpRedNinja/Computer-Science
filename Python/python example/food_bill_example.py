# This program was made by Harris Domangue for CMSC-210 on Sept 5th 2024
# This program will ask the user how much their bill was and tell them how much they should tip.

# Display purpose  to user
print("This program will tell you how much to tip!")

# Global Constants
GREAT = .2
GOOD = .15
OKAY = .10
BAD = .01

bill = float(input("How much was your bill: $")) # get the cost of the bill

#calculate each tip amount
great_tip = GREAT * bill
good_tip = GOOD * bill
okay_tip = OKAY * bill
bad_tip = BAD * bill

# display amounts
print(f"A 20% tip is: ${great_tip:.2f}")
print(f"A 15% tip is: ${good_tip:.2f}")
print(f"A 10% tip is: ${okay_tip:.2f}")
print(f"A 1% tip is: ${.01 * bill:.2f}") # warning! magic number .12
