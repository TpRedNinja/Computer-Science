
def example_one():
    my_list = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
    my_set = set( )

    for num in my_list:
        my_set.add(num)

    print(my_set)

def example_two():
    my_list = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
    my_set = set(my_list)

    print(my_set)

def example_three():
    my_list = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
    my_set = set(my_list)

    print("Set Before:",my_set)
    my_set.remove(0) # remove 0
    my_set.remove(9) # remove 9
    print("Set_After:",my_set)

def example_four():
    my_list = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 3, 5, 7, 9]
    my_set = set( )

    for num in my_list:
        my_set.add(num)

    print("The List:",my_list)
    print("The Set:",my_set)


def example_five():
    setA = set([1,2,3,4,5,6])
    setB = set([4,5,6,7,8,9])
    print(setA | setB)
    print(setA.union(setB))

def example_six():
    setA = set([1,2,3,4,5,6])
    setB = set([4,5,6,7,8,9])

    print(setA & setB)
    print(setA.intersection(setB))
    
def example_seven():
    setA = set([1,2,3,4,5,6])
    setB = set([4,5,6,7,8,9])

    print(setA - setB)
    print(setA.difference(setB))

def example_eight():
    setA = set([1,2,3,4,5,6])
    setB = set([4,5,6,7,8,9])

    print(setA ^ setB)
    print(setA.symmetric_difference(setB))
    
# call the function here
example_eight()
