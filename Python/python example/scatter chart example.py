import matplotlib.pyplot as MPL

def intro():
    print('This program will display a scatter plot')
def main():
    intro()
    x,y = get_data() # this gets the x and y data

    the_type = input("Enter 1 to display a scatter plot or enter 2 to display a line graph")

    MPL.grid() # this set ups a grid for your data
    if the_type == '1':
        display_scatter(x,y)
    else:
        MPL.plot(x,y)
        MPL.show()

# get data from the user and add to a list
def get_data():
    x =[]
    y =[]
    for data in range(1,6):
        print(f'info for data {data}')
        salary = input("Enter your salary: ")
        salary = float(salary.replace("$","").replace(",",""))
        exp = float(input("Enter your years of Experience: "))
        print()
        x.append(exp)
        y.append(salary)

    return x,y

def display_scatter(x,y):
    MPL.scatter(x,y)
    MPL.show()

if __name__ == '__main__':
    main()
