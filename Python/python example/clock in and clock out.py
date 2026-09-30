# This program will keep track of someones pay and salary
# This program is a clock in and clock Out program
# This program was made by Harris Domangue on Oct 17th 2024
import time

CLOCK_IN = "1:07pm"
CLOCK_OUT = "7:19pm"
TOTAL = 0
RATE = 15

def total():
    global CLOCK_IN
    global CLOCK_OUT
    global TOTAL

    temp_clock_in = CLOCK_IN.split(':')
    temp_clock_out = CLOCK_OUT.split(':')
    print(temp_clock_in)
    print(temp_clock_out)
    print()

    if "pm" in CLOCK_IN:
        temp_clock_in[1] = temp_clock_in[1].replace('pm','')
    else:
        temp_clock_in[1] = temp_clock_in[1].replace('am','')
    if "pm" in CLOCK_OUT:
        temp_clock_out[1] = temp_clock_out[1].replace('pm','')
    else:
        temp_clock_out[1] = temp_clock_out[1].replace('am','')

    print(temp_clock_in)
    print(temp_clock_out)
    
def clock_in():
    global CLOCK_IN
    if CLOCK_IN == None:
        CLOCK_IN = input("What time is it?: ")
    else:
        print("You already clocked in")

def clock_out():
    global CLOCK_IN
    if CLOCK_IN == None:
        print("You have clocked in yet")
    else:
        CLOCK_OUT = input("What time is it?: ")
        total()

def summary():
    print(f"Clock in time: {CLOCK_IN}")
    print(f"Hours on Paycheck: ${TOTAL}")
    print(f"Current on Paycheck: ${TOTAL  * RATE:,.2f}") 

def intro():
    print("This is a clock in and clock Out program it will keep track of your")

def menu():
    print()
    print("Enter 1 to clock in")
    print("Enter 2 to clock out")
    print("Enter 3 to view summary")
    print("Enter 4 to exit")
    choice = int(input("Enter Here: "))
    print()

    if choice == 1:
        clock_in()
        menu()
    elif choice == 2:
        clock_out()
        menu()
    elif choice == 3:
        summary()
        menu()
    else:
        print("goodbye")

def main():
    intro()
    menu()

if __name__ == '__main__':
    #main()
    total()
