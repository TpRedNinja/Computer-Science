# This is an example of looping over a list

grades = ['A','B','C','D','E','F']

# iterate over the list using a basic for loop
print("\nfor loop iteration example:")
total_number_elements = 0
for elements in grades:
    print(elements)
    total_number_elements += 1

print("\nfor loop range example:")
for index in range (0,total_number_elements):
    print(grades[index])

print("\nwhile loop example:")
count = 0
length_list = len(grades)
while count < length_list:
    print(grades[count])
    count +=1
