# This program was made by Harris Domangue for CMSC-201 on Oct. 3rd 2024
# This program is a 401k simulator

# Global variables
MAXAGE = 65

#Variables for program
Initial_amount = float(input("Please enter how much you want to start with: $"))
Yearly_amount = float(input("Please enter your yearly contributions: $"))
Intrest = float(input("Enter intrest percentage: %"))
Age = int(input("Please enter your current age: "))
print('\u2013' * 40)  # Dashes to separate stuff

ITERATION = MAXAGE - Age
total_amount = Initial_amount
total_contributions = Initial_amount
total_interest_earned = 0.0

for year in range(ITERATION):
    # Add yearly contribution
    total_amount += Yearly_amount
    total_contributions += Yearly_amount

    # Calculate interest for the current year
    interest_for_year = total_amount * (Intrest / 100)
    
    # Add interest to the total amount
    total_amount += interest_for_year
    
    # Update total interest earned
    total_interest_earned += interest_for_year

print(f"You contributed a total of ${total_contributions:,.2f}")
print(f"You earned ${total_interest_earned:,.2f} in interest")
print(f"Your 401k is now worth ${total_amount:,.2f}")
    

