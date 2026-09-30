# This program was made by Harris Domangue on Nov 21st, 2024 for CMSC-201
# This program will randomly generate 2 sets and will find the union,
# intersection, differemce, and semetric difference.

import random # import random

# create 2 empty sets
setA = set()
setB = set()

for num in range(20):
    setA.add(random.randint(1,50))
    setB.add(random.randint(1,50))

print("setA length:",len(setA))
print("setB length:",len(setB))

print("Union between setA | setB:",setA.union(setB))
print("Intersection between setA & setB:",setA.intersection(setB))
print("Difference between setA - setB:",setA.difference(setB))
print("Difference between setB - setA:",setB.difference(setA))
print("Symmetric Difference between setA ^ setB:",setA.symmetric_difference(setB))
