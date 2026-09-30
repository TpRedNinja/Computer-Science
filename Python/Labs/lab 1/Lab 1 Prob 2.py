# This program was made by Harris Domangue for CMSC-201 on Sept. 10th 2024
# This program will show you your Gross and net pay

# Global constant
TAX_RATE = 0.153

# Displays to user what this program does
print("This program calculates your gross pay and net pay")

# Ask's the user how much income they have made
User_Income = input("How much income have you made this year?: ") # taken as a string incase the user enters a , or $
User_Income = User_Income.replace(",","") # replace the , with nothing
User_Income = User_Income.replace("$","") # replace the $ with nothing
User_Income = float(User_Income) # converts to string so can be used in calculations

# Ask's the user how much was in deductions
User_Deductions = input("How much was in deductions?: ")
User_Deductions = User_Deductions.replace(",","") # replace the , with nothing
User_Deductions = User_Deductions.replace("$","") # replace the $ with nothing
User_Deductions = float(User_Deductions) # converts to string so can be used in calculations

# Calculates the user's net pay and how much they owe in taxes
NetPay_BeforeTax = float(User_Income - User_Deductions)
NetPay_WithTax = float(NetPay_BeforeTax * TAX_RATE )
NetPay = float(NetPay_BeforeTax - NetPay_WithTax)

# Displays the Netpay, Grosspay, and deductions to the user
print(f" Your grosspay is:${User_Income:.2f}")
print(f" Your net pay this year is:${NetPay:.2f}")
print(f" You owe:$ {NetPay_WithTax:.2f}in taxes")


