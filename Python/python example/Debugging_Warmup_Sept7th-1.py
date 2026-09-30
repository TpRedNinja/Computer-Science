# This program was made as a warm up for CMSC201
# debug the following code: (Note: There is a total of 4 errors)

# This code should ask the user for the number of employees
# ask for the companies salary budget and find the average pay for
# the company

# Get the user's input for the number of employees and budget
employees = int(input("How many Employees work for you?: "))
budget = float(input('What is the companies budget? '))

# Find the average salary based on the number of employees and the budget
average_pay = budget/employees

# Display this to the user. 
print(f'The average salary for all employees is ${average_pay:,.2f}')
