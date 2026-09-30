# Import the GUI module
from tkinter import *

def menu(courses):
    # create a base menu
    root = Tk()
    root.geometry("800x500")# create our window size
    def search(): # show  function
        key = my_input.get()
        try:
            my_display_label.config(text = f'Output: {key}: {courses[key]}')
        except KeyError:
            my_display_label.config(text = f'Output: {key} does not exist')
    def add():
        key = my_input.get()
        value = my_input_title.get()
        if value != "" and key != "":
            courses[key] = value

    def display():
        my_display_label.config(text = "Output: " + str(courses))
        
        
    # create a label for the user
    my_label = Label(root,text = "Course Code: ")
    my_label.pack() # add the label to the window

    my_input = Entry(root)
    my_input.pack() # adds the input box

    my_label = Label(root,text = "Course Title: ")
    my_label.pack() # add the label to the window
    my_input_title = Entry(root)
    my_input_title.pack() # adds the input box

    my_button = Button(root,text='Search',command=search).pack()
    my_button2 = Button(root,text='Add',command=add).pack()
    my_button3 = Button(root,text='Display',command=display).pack()

    my_display_label = Label(root,text = "Output: ")
    my_display_label.pack()

    root.mainloop() # displays the window and runs the buttons and inputs

def main():
    courses= {}
    menu(courses)
main()
