# This program was made by Harris Domangue for CMSC-204 on Oct 24th 2024
# This program will convert positive numbers into binary

def intro():
    print("This program will convert positive numbers into binary")
    

def convert(number):
    #for num in number:
    if number % 2 == 1:
        print(1)
    else:
        print(0)
    if number != 1:
        convert(int(number / 2))

def main():
    intro()
    number = int(input("Enter the number you want to convert to binary: "))
    convert(number)

if __name__ == '__main__':
    main()
