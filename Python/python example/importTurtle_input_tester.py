#Justin Frock CIS_105 September 5, 2022
#The purpose of this program is to allow students to test
#how to use import turtles sizes

#import math for A^2+B^2=C^2 for triangle base.
import math

#Create print statements for user
print("This Program creates a square, circle and triangle.")
print('Line should be a min of 1px and a max of 100px')
print("(Note: Sizes are in turtle pixels)")
print("Shapes should be a min of 10px and a max of 300px")

#Create input statements for sizes of each shape and line. 
sq_size = float(input("Square Sides size in px: "))
radius = float(input("Circle Radius in px: "))
tr_size = float(input("Triangle Sides in px: "))
ln_size = float(input("Line size in px: "))
    
#Square Root of Triangle
tr_ab = (tr_size * tr_size)+(tr_size * tr_size)
#finds length of C using A^2+B^2=C^2
tr_c =  math.sqrt(tr_ab)

#import turtle
import turtle
s=turtle.getscreen()
t=turtle.Turtle()

#Pen size made larger for stripe
t.pensize(ln_size)

#Creates the red Square's angles and length
t.pencolor("red")
t.forward(sq_size)
t.right(90)
t.forward(sq_size)
t.right(90)
t.forward(sq_size)
t.right(90)
t.forward(sq_size)

#Creates the blue Circle's angles and length
t.pencolor("blue")
t.circle(radius)

#Creates the green Triangle's angles and length
t.pencolor("green")
t.right(45)
t.forward(tr_size)
t.right(90)
t.forward(tr_size)
t.right(135)
t.forward(tr_c)



