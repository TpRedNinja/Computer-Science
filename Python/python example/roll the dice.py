# This is a random dice which will randomly generate dice rolls and keep track
# This program was made by Harris Domangue for CMSC-201 on Oct 10th 2024

import random

def intro():
    print('This is a dice roll simulation')

def run(times):
    # set variables for each score type
    score1 = 0
    score2 = 0
    score3 = 0
    score4 = score5 = score6 = 0
    for roll in range(times):
        this_roll = random.randint(1,6)# generate random number between 1 and 6
        if this_roll == 1:
            score1 += 1
        elif this_roll == 2:
            score2 +=1
        elif this_roll == 3:
            score3 +=1
        elif this_roll == 4:
            score4 +=1
        elif this_roll == 5:
            score5 +=1
        else:
            score6 +=1
    # pass our scores to the graph function
    graph(score1,score2,score3,score4,score5,score6)

def graph(score1,score2,score3,score4,score5,score6):
    bar1 = bar2 = bar3 = bar4 = bar5 = bar6 = ''
    # use for loops to add '|' to the bar
    for num in range(score1):
        bar1 += '|'
    for num in range(score2):
        bar2 += '|'
    for num in range(score3):
        bar3 += '|'
    for num in range(score4):
        bar4 += '|'
    for num in range(score5):
        bar5 += '|'
    for num in range(score6):
        bar6 += '|'
    # display bars
    print("1", bar1)
    print("2", bar2)
    print("3", bar3)
    print("4", bar4)
    print("5", bar5)
    print("6", bar6)
    

def main(): # main driver
    intro()
    num_of_times = int(input('How many dice do you want to roll? '))
    run(num_of_times)

if __name__ == '__main__':
    main()
