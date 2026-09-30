# This program was made by Harris Domangue for CMSC-201 on Sept. 26th 2024
# This program will tell you your pay grade base off your rank and how many years you have served

# user display
print("This program how much tell you how much you made this week plus any bonus pay")

#Global stuff
HOURLY_PAY = 15.00
TEN = 10
THIRTY = 30
NINETY = 90

# Asks user how many hours the user has worked
Hours_Worked = float(input("How many hours have you worked this week? "))# made it a float sense sometimes people work 10 and a half hours so wanted to give them the option
Pay_Before_Bonus = HOURLY_PAY * Hours_Worked

if Hours_Worked <= 0:
    print(f"Sorry you you didnt work any hours cant calculate pay")
elif Hours_Worked >= 10 and Hours_Worked <= 19:
    Total_Pay = Pay_Before_Bonus + TEN
    print(f"You made ${Total_Pay:,.2f}")
elif Hours_Worked >= 20 and Hours_Worked <= 29:
    Total_Pay = Pay_Before_Bonus + THIRTY
    print(f"You made ${Total_Pay:,.2f}")
elif Hours_Worked >= 30 and Hours_Worked <= 39:
    Total_Pay = Pay_Before_Bonus + NINETY
    print(f"You made ${Total_Pay:,.2f}")
elif Hours_Worked >=40:
    Total_Pay = Pay_Before_Bonus
    print(f"your total pay is ${Total_Pay}")

