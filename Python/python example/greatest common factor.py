# This program will find the greatest common divisor of two numbers.
def gcd(small_num, big_num):
    if big_num == 0: # base case
        print('Base case:', small_num,big_num)
        return small_num
    else: # recursive case
        print('Recursive case:', small_num,big_num)
        return gcd(big_num, small_num % big_num)

# get numbers from the user
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print(f'The greatest common divisor between {num1} and {num2} is {gcd(num1,num2)}')
