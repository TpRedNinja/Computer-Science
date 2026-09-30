# This program was made by Harris Domangue for CMSC-201 on Sept 24th 2024
# This  program will ask the user for their phone number and tell the user how many even numbers are in their number.

# User input
print("This program will get your phone number and tell you how many even numbers")
print("are in your phone number")

# get user phone number
phone = input("Enter your phone number: ")
# replace any '-' the user may place in their number
phone = phone.replace('-',"")


# variable to keep running total
even_count = 0

for num in phone:
    if int(num) % 2 == 0 : # if num == '0' or num == '2' or num == '4' or num == '6' or num == '8':
        even_count += 1
print("The total number of even numbers is", even_count)

# This counts the total number of disinct even numbers
even_count = 0

if '0' in phone:
    even_count += 1
if '2' in phone:
    even_count += 1
if '4' in phone:
    even_count += 1
if '6' in phone:
    even_count += 1
if '8' in phone:
    even_count += 1

print("The total number of distinct even numbers is", even_count)
