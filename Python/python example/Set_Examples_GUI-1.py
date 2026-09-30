# This program will make two sets and compare them using Union, Intersection, Difference and Symmetrical Difference
# This program was made by Justin Frock for CMSC-201 on April 18th 2024

from tkinter import *

# import random
import random

# create root window
root = Tk()

# adjust window size
root.geometry("750x750")

def showSets():
    # create two empty sets
    setA = set()
    setB = set()

    # add the random numbers to the sets 
    for num in range(int(dropMenu.get())):
        r_num = random.randint(1,50)
        setA.add(r_num)
        r_num = random.randint(1,50)
        setB.add(r_num)

    setA_label.config(text = f"First Set: {setA}")
    setB_label.config(text = f"Second Set: {setB}")

    # display the stats only if the user wants us too. 
    if CB.get() == 1:
        union_label.config(text = f'Union: {setA | setB}')
        intersection_label.config(text = f'Intersection: {setA & setB}')
        difference_label.config(text = f'Difference: {setA - setB}')
        symetric_label.config(text = f'Symetric Difference: {setA  ^ setB}')

    else:
        union_label.config(text = "")
        intersection_label.config(text = "")
        difference_label.config(text = "")
        symetric_label.config(text = "")

        
# create a drop down menu for numbers to generate
options = ['5','10','15','20','25']

# add a label to explain to user
select_label = Label(root, text = "Select the Number of Numbers to Generate: ")
select_label.pack()

dropMenu = StringVar()
dropMenu.set('10')

# create dropdown menu
drop = OptionMenu(root ,dropMenu, *options)
drop.pack() # add the drop to menu 

# create labels for the sets
setA_label = Label(root,text = 'First Set:')
setB_label = Label(root,text = 'Second Set:')
setA_label.pack()
setB_label.pack()

button = Button(root,text = "Generate Sets", command = showSets).pack()

CB = IntVar() # variable to store the check box

check1 = Checkbutton(root,text = "Show Stats", variable = CB,onvalue = 1,offvalue = 0, height = 2, width = 10).pack()

union_label = Label(root, text = "")
union_label.pack()

intersection_label = Label(root, text = "")
intersection_label.pack()

difference_label = Label(root, text = "")
difference_label.pack()

symetric_label = Label(root, text = "")
symetric_label.pack()


root.mainloop() # loop our window 
