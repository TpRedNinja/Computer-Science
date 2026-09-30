# This program was made by Harris Domangue for CMSC-201 on Oct. 3rd 2024
# This program is a for loop count down clock

import time
import os

# get user input
print("This is a stop watch program")
seconds = int(input("Enter the seconds: "))

for second in range (seconds,0,-1):
    os.system("cls") # clear the screen
    print(f"{second} Seconds left")
    time.sleep(1) # wait on second
