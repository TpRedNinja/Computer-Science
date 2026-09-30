# This program will take the first letter of your name and last letter and swap them
# This program was made by Harris Domangue for CMSC-201 on 11/14/2024

# get the name from the user
name = input("Name: ")

name = name.upper()

# get the first letter and last letter
last_index = len(name)-1

temp_name = ""
# iterate over each letter
for num in range(len(name)):
    if num == 0:
        temp_name += name[last_index]
    elif num == last_index:
        temp_name += name[0]
    else:
        temp_name += name[num]

print(f'Name swapped to {temp_name}')
