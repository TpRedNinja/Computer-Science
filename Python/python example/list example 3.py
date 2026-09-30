# This program was made on Nov 7th 2024 for CMSC-201
# This program is an example of creating a list in python

# create a list called database
database = []

name = None
while name != '':
    name = input('Enter employee name: ')
    if name != '':
        salary = input('Enter employee salary: ')
        info = name + '$' + salary # cancat the string together
        database.append(info)

# display employees
#print(database)
print('-------------------')
for employee in database:
    employee = employee.split("$")

    print(f'Name: {employee[0]}')
    print(f'Salary: {employee[1]}')
