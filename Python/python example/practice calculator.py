# This program was made by Harris Domangue for CMSC-201 on Sept. 10th 2024
# This program is a calculator and is able to add, subtract, multiply, and divide 2 numbers

# display to user
print("This program will add, subtract, multiply, and divide.")

num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
opperation = input("enter the opperation (+,-,*,/): ")

if opperation == '+': # check if + was put in
    answer = num1 +  num2
elif opperation == '-': # check if - was put in
    answer = num1 - num2
elif opperarion == '*': # check if * was put in
    answer = num1 * num 2
elif opperarion == '/': # check if / was put in
    answer = num1 / num 2
else:
    answer = "Error"

# display the answer
print(num1,opperation,num2,"=",answer)
