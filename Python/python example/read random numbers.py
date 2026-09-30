# This program was made by Harris Domangue for CMSC-201 on Oct 24th 2024
# This program will read 100 random numbers from a file.

file = open("numbers.txt","r") # open our file

# read each number from the file
total = 0

for line in file: # get each line from the file
    line = line.rstrip('\n') # remove the new line character
    total += int(line) # add the number as an int to total

file.close() # close the file

print(f"All the numbers add up to {total}")
