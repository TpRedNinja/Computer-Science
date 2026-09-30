# Import the GUI module
from tkinter import *

def menu():
    # create a base menu
    root = Tk()
    root.geometry("800x500")# create our window size
    def show(): # show  function
        print(my_input.get())


        
    # create a label for the user
    my_label = Label(root,text = "Enter your name")
    my_label.pack() # add the label to the window

    my_input = Entry(root)
    my_input.pack() # adds the input box

    my_button = Button(root,text='execute',command=show).pack()

    root.mainloop() # displays the window and runs the buttons and inputs

menu()
