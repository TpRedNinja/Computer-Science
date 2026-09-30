import time
# This is a loan program which will tell you how much you qualify for a personal loan.
# This program was made by Harris Domangue for CMSC-201 on Sept. 17th 2024

max_percent = .35

# user display
print("This program will help you get a loan")

# ask the  user for their salary and for their debt amount
salary = float(input("enter your salary: "))
debt = float(input("enter your current debt: "))

# start the watch to get the length of time this program rand
START = time.time()

# try to test if the user can get a loan
if salary > 35000:
    debt_to_income = salary * max_percent
    if debt_to_income < debt:
        print("You do not qualify for the loan")
    else:
        print(f"You qualify for a loan of {debt_to_income - debt:,.2f}")
else:
    print("You dont make enough to qualify for the loan.")

END = time.time()
print(f"This program executed in {END-START} seconds")
