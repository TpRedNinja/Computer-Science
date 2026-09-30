# This program was made by Harris Domangue for CMSC-201 on oct 31st 2024
# This program will count between two numbers and it will time how long it takes at each method

# import the time function
from time import time # ONLY importing the time function from the time modules

def intro():
    print("This program will count between 2 numbers")
    print(time())

def CountThis(min_value,max_value):
    if min_value <= max_value:
        print(min_value)
        CountThis(min_value +1,max_value)

def main():
    min_value = int(input("What is the min value: "))
    max_value = int(input("What is the max value: "))

    while max_value - min_value > 1000:
        min_value = int(input("What is the min value: "))
        max_value = int(input("What is the max value: "))

    # open a file to store the different time
    f = open("LoopTimes.txt",'w')

    START = time()
    CountThis(min_value,max_value)
    END = time()

    f.write(f'Recursion Time: {END-START:.2f} seconds \n')

    START = time()
    for num in range(min_value,max_value +1):
        print(num)
    END = time()

    f.write(f'For loop Time: {END-START:.2f} seconds \n')

    START = time()
    count = min_value
    while count <= max_value:
        print(count)
        count += 1
    END = time()

    f.write(f'While loop Time: {END-START:.2f} seconds \n')

    f.close()


if __name__ == '__main__':
    main()
