# This example will demonstrate the use of nested if-else

#test if the user is in elemetry school, middle, or high school

print("enter your grade and the program will tell you what type of school you are in")
grade = int(input('Enter your grade: '))

if grade > 8:
    print("High School!")
elif grade > 5:
    print("Middle School!")
else:
    print("Elementry School!")
