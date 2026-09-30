# This program will get where each letter of your name exist in the alphabet
# This program was made by Harris Domangue for CMSC-201 on 11/14/2024

key = 'abcdefghijklmnopqrstuvwxyz'

# get the phrase from the user
phrase = input("Enter a sentence here: ")
# set phrase to lower case
phrase = phrase.lower()


for letter in phrase:
    if letter in key:
        index = key.index(letter) + 1
        print(f"The letter {letter} appears at number {index} in the alphabet")
    else:
        print("")


