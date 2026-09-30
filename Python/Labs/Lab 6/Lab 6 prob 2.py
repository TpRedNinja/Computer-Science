# This program will display a graph for the user to display some data about stuff idk what dont ask me
# This program was made by Harris Domangue on Nov 12th 2024 for CMSC-201

import matplotlib.pyplot as MPL

def intro():
    print('This program will display a graph of the user choice')
def main():
    intro()
    # list of the years
    years = [2001,2003,2005,2007,2009,2011,2013,2015,2017,2019]

    # get data from the user and add to a list
    salary = [] # list for the salaries
    file = open("ComputerProgrammers.txt","r")
    for line in file:
        if line != "":
            line = line.replace("$","").replace(",","")
            line = float(line)
            salary.append(line)

    
    the_type = input("Enter 1 to display a bar graph or enter 2 to display a line graph")

    # title our bar graph
    MPL.title("Salaries of computer programmer through the years")
    MPL.xlabel("Years")
    MPL.ylabel("Salaries")

    if the_type == '1':
        MPL.bar(years,salary)# create our bar
        MPL.show()
    else:
        MPL.plot(years,salary)
        MPL.show()

    
    file.close()

    

if __name__ == '__main__':
    main()
