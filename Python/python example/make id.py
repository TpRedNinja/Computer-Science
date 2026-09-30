# This program will create a program id number
# This program was made by Harris Domangue for CMSC-201 on 11/14/2024

full_name = input('Enter your first and last name: ')
while len(full_name.split()) != 2:
    full_name = input('Error: Enter your first and last name: ')
first_name,last_name = full_name.split() # This take the first letter ofthe users first and last name

todays_date = input('Enter todays date using "/": ')
todays_date = todays_date.split('/')

while len(todays_date) != 3:
    todays_date = input('Error: Enter todays date using "/": ')
    todays_date = todays_date.split('/')


# start off the ID
new_id = first_name[0] + last_name[0] + '-'
new_id = new_id.upper()
# flag to check if it worked
worked = True
for element in todays_date:
    last = len(element)-1
    if not element.isdigit():
        print("ID could not be made")
        worked = False
        break
    else:
        new_id += element[last]
if worked:
    print(f"Your ID is {new_id}")
