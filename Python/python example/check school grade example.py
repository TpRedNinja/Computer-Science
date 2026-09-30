# This example will demonstrate the use of nested if-else

#test if the user is in elemetry school, middle, or high school

print("enter your grade and the program will tell you what type of school you are in")
grade = int(input('Enter your grade: '))

if grade <= 12:
      print("you are in school")
      if grade < 9:
          if grade < 6:
              print("Elementry School!")
          else:
              print("Middle School!")
      else:
          print("High School!")
else:
    print("Error!")
