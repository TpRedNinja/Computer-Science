# This program will read a text file
try:
    file = open("C:/Users/jjdom/OneDrive/python stuff/earth.txt", 'r') # open file

    # read the file
    data = file.read()

    print(data)

    file.close() # close the file
except FileNotFoundError as e:
    print("This file does not exist")
