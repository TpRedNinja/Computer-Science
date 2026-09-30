# This program was made by Harris Domangue for CMSC-201 on Oct 24th 2024
# This program will write 100 random numbers to a file.

# import random
import random

file = open("numbers.txt","w") # open our file

# write 100 random numbers
for num in range(100):
    number = random.randint(1,1000)
    file.write(str(number) + '\n') # convert int to string

file.close() # close the file

print("done")
