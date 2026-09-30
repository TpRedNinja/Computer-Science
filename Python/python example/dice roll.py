# This program is a dice rolling program which will randomly roll dice

def display(totals):
    print()
    for number in totals:
        bar = ""
        for num in range(number):
            bar += "|"
        print(bar)
import random

sides = int(input("How many sides does the dice have?: "))
# list of totals
totals = [ 0 for i in range (sides) ]

# randomly roll dice
for roll in range(100):
    num = random.randint(1,sides)
    totals[num-1] += 1


MAX = max(totals)
MIN = min(totals)

min_index = totals.index(MIN)
max_index = totals.index(MAX)

print("Min Roll:", MIN, 'The number that', min_index+1,"was rolled the least.")
print("Max Roll:", MAX, 'The number that', max_index+1,"was rolled the most.")
#print("Average Roll:", sum(totals) / len(totals))

display(totals)
