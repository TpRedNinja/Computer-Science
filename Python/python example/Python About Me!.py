# import everything from tkinter module 
from tkinter import *

# import messagebox from tkinter module 
import tkinter.messagebox 

# tkinter root window 
root = tkinter.Tk() 
  
# Window title and dimension 
root.title("Python Introduce Yourself!") 
root.geometry('300x300') 
  
# These are functions which dislay the pop-up boxes "we will learn more about functions later in the course 
def onClickName(): 
    tkinter.messagebox.showinfo("Hi my name is","Harris.D") #Make your first edit here!
def onClickWhy(): 
    tkinter.messagebox.showinfo("I am taking CMSC-201-65 because","I want to learn python and more about coding in general") #Make your second edit here!
def onClickFact(): 
    tkinter.messagebox.showinfo("A fun fact about myself is,","I've made autosplitters for some games I speedrun. I code them in ASL(Auto Splitting Language) which is base off of C# if im not mistaken.") #Make your third edit here!
  
# These create button objects which store the label of the button and the function used
button1 = Button(root, text="What is my name?", command=onClickName, height=5, width=15)
button2 = Button(root, text="Why am I Here?", command=onClickWhy, height=5, width=15)
button3 = Button(root, text="A fun fact about me!", command=onClickFact, height=5, width=15) 
  
# This using a .pack method which places the buttons on the screen
button1.pack()
button2.pack()
button3.pack()
# This keeps the program running 
root.mainloop() 
