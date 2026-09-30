# This program was made by Harris Domangue for CMSC-201 on Sept. 17th 2024
# This program will test if Justin will wake up in time for class

# user display
print("This program will test if Just will wake up on time")

# get user imput
alarm = input("Did Justin set his alarm clock yes or no?: ")
cat = input("Did Justin feed Anna  the night before yes or no?: ")

# test what happens in the morning when Justin wakes up
if cat == 'no':
    print("Justin wakes up at 5:00am to Anna Meowing!")
elif alarm == 'yes':
    print("Justin wakes up on time at 7:00am to his alarm clock.")
else:
    print("Justin wakes up at 9:00am late")
