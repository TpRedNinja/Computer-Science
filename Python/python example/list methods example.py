# This program is an example of working with a list's methods

# create and empty list
my_list = []

for num in range(1,10):
    my_list.append(num)# add a number at each iteration

print('our list', my_list)
my_list.pop() # remove last element in list
print('our list after the pop() method', my_list)
my_list.insert(4,19) # inserts 19 at index 4
print('our list after the insert() method', my_list)
my_list.remove(3) # remove the number 3 from our list
print('our list after the remove() method', my_list)
my_list.sort() # sorts least to greatest
print('our list after the sort() method', my_list)
my_list.reverse() # reverse the list
print('our list after the reverse() method', my_list)

del my_list[2] # this deletes the element at the specified index
print('our list after the del keyword', my_list)
