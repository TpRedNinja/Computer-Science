# This program will take in your name and check if a substring exists with in it
# This program was made by Harris Domangue for CMSC-201 on 11/14/2024

# while loop to iterate over each line
name = None
while name != "":
    # get the users name
    name = input("Name: ")
    if name != "":
        word = input("Word: ")

        # check if the word is in users name
        if word in name:
            print(f"{word} is in {name}")
        else:
            print(f"{word} is not in {name}")
