# This program was made by Harris Domangue on oct 29th 2024 for cscmc-201
# This program is a mini database
# This program will generate 100 employee's by id, years in college, salary, and work from home status

#import random
import random

def intro():
    print('this program will create 100 employees into a text file')

def generate_employees(file):
    letters = 'abcdefghijklmnopqrstuvwxyz' # sequence 'string of letters
    letters = letters.upper()
    ID = random.choice(letters) + '-' + str(random.randint(10000,99999)) # randomly generates a id for an employee
    years_in_college = random.randint(0,6) # randomly generates years in college
    salary = random.uniform(35000,80000) # randomly generates salary
    home = random.choice([True,False]) # gets either true or false

    file.write(ID + '\n')
    file.write(str(years_in_college) + '\n')
    file.write(f'{salary:.2f}\n')
    file.write(str(home) + '\n')
    file.write('\n')

def main():
    intro()
    # open pur file here in main
    file = open("employees.txt",'w')
    for i in range(100):
         generate_employees(file)
    file.close() # close our file

# call main
if __name__ == '__main__':
    main()
