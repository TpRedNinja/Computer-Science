# This program will tell you what time your final exam is
from tkinter import *
root = Tk() 
root.geometry( "300x300" ) 
data = [['7:30am', '', 'T 8:00am', '', '', ''],['8:00am', 'M 8:00a', 'T 8:00a', '', '', ''], ['8:30am', '', '', '', '', ''], ['9:00am', 'W 8:00a', 'T 10:15a', '', '', ''], ['9:30am', 'W 8:00a', 'T 10:15a', 'W 10:15a', '', 'F 10:15a', ''], ['10:00am', 'W 10:15a', 'T 10:15a', '', '', '', ''], ['10:30am', 'W 10:15a', '', '', '', '', ''], ['10:40am', '', 'TH 10:15a', '', '', ''], ['11:00am', 'M 10:15a', 'T 12:30p', '', '', 'F 12:30p', ''], ['11:30am', 'W 12:30p', 'T 12:30p', '', '', '', ''], ['12:00pm', 'M 12:30p', 'TH 12:30p', '', '', '', ''], ['12:30pm', 'M 12:30p', 'TH 12:30p', 'W 12:30p', '', '', ''], ['1:00pm', 'M 12:30p', 'T 2:45p', '', 'TH 2:45p', '', ''], ['1:30pm', 'M 2:45p', '', '', '', '', ''], ['2:00pm', 'W 2:45p', 'T 2:45p', 'W 2:45p', '', '', ''], ['2:30pm', 'M 2:45p', 'TH 2:45p', '', '', '', ''], ['3:00pm', '', '', '', '', '', ''], ['3:30pm', '', 'TH 5:00p', '', 'TH 5:00p', '', ''], ['4:00pm', '', 'TH 5:00p', '', '', '', ''], ['4:30pm', '', 'T 5:00p', '', '', '', ''], ['5:00pm', 'M 5:00p', 'T 5:00p', '', '', '', ''], ['5:30pm', 'M 5:00p', 'T 5:00p', '', '', '', ''], ['6:00pm', 'M 7:15p', 'T 7:15p', '', '', '', ''], ['6:30pm', 'M 7:15p', 'T 7:15p', '', '', '', ''], ['7:00pm', 'M 7:15p', 'T 7:15p', '', '', ''], ['7:30pm', '', 'T 7:15p', '', '', '']]
times = [d[0] for d in data]
# Change the label text 
def show():
    day = day_click.get().lower()
    time = time_click.get().lower()
    days = ['sunday','monday','tuesday','wednesday','thursday','friday']
    dates = [str(i) for i in range(15,21)]
    the_time = ''
    for r in data:
        if r[0] == time:
            the_time = r[days.index(day)].replace('a','am').replace('p','pm')
    if the_time == "":
        the_time = 'NOT FOUND'
    label.config( text = f'Final Exam Time: {the_time}' ) 
  

options = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
label = Label( root , text = "Class Start Day" ) 
label.pack()

day_click = StringVar() 
day_click.set( "Monday" ) 
drop = OptionMenu( root , day_click , *options ) 
drop.pack()
label = Label( root , text = "Class Start Time" ) 
label.pack() 
time_click = StringVar() 
time_click.set( '9:00am' ) 
drop = OptionMenu( root , time_click , *times ) 
drop.pack()
  
button = Button( root , text = "Exam Time" , command = show ).pack() 
  
label = Label( root , text = " " ) 
label.pack() 
  
root.mainloop() 
