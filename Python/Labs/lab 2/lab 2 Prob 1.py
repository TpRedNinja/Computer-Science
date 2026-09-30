# This program was made by Harris Domangue for CMSC-201 on Sept. 19th 2024
# This program will detect values in your name

# global constants
VOWEL1 = "a"
VOWEL2 = "e"
VOWEL3 = "i"
VOWEL4 = "o"
VOWEL5 = "u"

# user display
print("This program will tell you what vowels are in your name and tells how many all together there are")

# variable to keep track of total vowels
vowel_count = 0

# asks user for their name
User_Name= input("Enter your name: ")

# Counst the number of distinct vowels in users name
vowel_count = 0

if VOWEL1 in User_Name:
    vowel_count += 1
if VOWEL2 in User_Name:
    vowel_count += 1
if VOWEL3 in User_Name:
    vowel_count += 1
if VOWEL4 in User_Name:
    vowel_count += 1
if VOWEL5 in User_Name:
    vowel_count += 1

print("The total number of distinct vowels in your name is", vowel_count)


    
