# This program was made by Harris Domangue for CMSC-201 on Sept. 14th 2024
# This program will draw a very bad looking gary the snail

import turtle as t

# displays to user the purpose of the program
print("This program will draw a very bad looking gary the snail")
input("Press enter to begin...")

# garys shell
t.pencolor("pink")
t.speed(100)
t.begin_fill()
t.fillcolor("pink")
t.pensize(15)
for pixel in range(70):
    t.circle(pixel,-20)
t.end_fill()

#get to position for body
t.right(125)
t.penup()
t.forward(10)
t.left(85)
t.back(100)

#garys body
t.pensize(10)
t.pencolor("blue")
t.fillcolor("blue")
t.pendown()
t.begin_fill()
t.left(-45)
t.forward(50)
t.left(45)
t.forward(100)
t.left(45)
t.forward(50)
t.right(45)
t.back(170)
t.end_fill()

#get into position for 1st eye
t.penup()
t.forward(170)
t.left(90)

#garys 1st eye
t.pencolor("black")
t.fillcolor("orange")
t.pendown()
t.forward(100)
t.begin_fill()
t.pensize(1)
t.circle(-15)
t.end_fill()
t.right(45)
t.forward(10)
t.begin_fill()
t.fillcolor("red")
t.circle(-10)
t.end_fill()
t.begin_fill()
t.fillcolor("black")
t.circle(-5)
t.end_fill()

#get into position for 2nd eye
t.back(10)
t.left(45)
t.penup()
t.back(100)
t.right(90)
t.back(20)
t.left(90)
t.pensize(10)

#garys 2nd eye
t.pencolor("black")
t.fillcolor("orange")
t.pendown()
t.forward(100)
t.begin_fill()
t.pensize(1)
t.circle(-15)
t.end_fill()
t.right(45)
t.forward(10)
t.begin_fill()
t.fillcolor("red")
t.circle(-10)
t.end_fill()
t.begin_fill()
t.fillcolor("black")
t.circle(-5)
t.end_fill()

#program done
t.hideturtle()
print("Gary has been drawn")
t.done()

