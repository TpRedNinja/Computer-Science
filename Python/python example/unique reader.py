# This program was made by Harris Domangue on Nov 21st, 2024 for CMSC-201
# This program will read a text file and display all the unique words that
# are in the file

# open the file
file = open("my_unquie_file.txt","r")
paragraph = file.read()
file.close
print(paragraph)

list_of_words = paragraph.split() # returns a list using empty spaces as delimeter
print("\nAll of the words in the file", len(list_of_words))
for word in list_of_words:
    print(word)

set_of_words = set(list_of_words)
print("\nAll of the unique words in the file", len(set_of_words))
for word in set_of_words:
    print(word)
