# This program was made by Harris Domangue for CMSC-201 on Sept. 10th 2024
# This program will  ask for 3 test score grades and display the final average grade

# name of constants
NUMBER_OF_TESTS = 3
# display to user
print("enter your three testscore and determine your average")

# get the scores of each test
test1 = float(input("test 1 score : "))
test2 = float(input("test 2 score : "))
test3 = float(input("test 3 score : "))

# find the final grade based on the average
finalGrade = (test1 + test2 + test3)/ NUMBER_OF_TESTS

# display the final grade
print(f"final grade: {finalGrade: .0f}%")
