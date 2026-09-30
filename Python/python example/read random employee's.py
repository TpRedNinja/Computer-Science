# This program was made by Harris Domangue on oct 29th 2024 for CMSC-201
# This program will read the data from employees.txt and display Information

def intro():
    print('this program will read the employee.txt file and display the text')

def read_file(file):
    # create variables to use
    count = 0
    total_years =0
    total_salary = 0
    total_home = 0
    ID = file.readline() # reads the first line of the file
    while ID != '':
        years = file.readline() # read the years
        salary = file.readline() # read the salary
        at_home = file.readline() # read the home status
        space = file.readline() # read the empty space
        ID = file.readline() # move on the nexr person

        # remove the new line characters from the lines of the file.
        ID = ID.rstrip('\n')
        years = years.rstrip('\n')
        salary = salary.rstrip('\n')
        at_home = at_home.rstrip('\n')

        # add upt the values
        try:
            total_years += int(years)
            total_salary += float(salary)
        except:
            print("There is an error with employee e")
        else:
            

        if at_home == 'True':
            at_home = bool(at_home)

        if at_home:
            total_home += 1
        print('ID:',ID)
        print('College:' ,years)
        print('Salary: $',salary)
        print('works at home:' ,at_home)
        print('-------------------')
        count += 1
    print('Summary:')
    print('Employee Count:',count)
    print(f'Average College: {total_years/count:.0f}')
    print(f'Average Salary: ${total_salary/count:,.2f}')
    print("Total at home:", total_home)

def main():
    intro()
    try:
        file= open("employees.txt",'r')
        read_file(file)
        file.close
    except FileNotFoundError:
        print("The file does not exists")

# call main
if __name__ == '__main__':
    main()
