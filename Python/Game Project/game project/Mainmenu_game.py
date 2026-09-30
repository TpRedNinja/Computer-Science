# Main menu for Bob the Robber

import pygame
from PIL import ImageTk
import tkinter as tk
from tkinter import *
import game1

def mainmenu():
    
    # create a base menu
    root = tk.Tk()
    root.geometry("200x150")# create our window size

    Start = Button(root,text="Start",command = start).pack()
    Exit = Button(root,text="Exit",command = root.destroy).pack()
    
    root.mainloop() # displays the window and runs the buttons and inputs

def start():
    game1.intro()

def main():
    mainmenu()

if __name__ == '__main__':
    main()
