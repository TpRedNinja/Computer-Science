# This program will create a bar graph to show you the number of years spent
# at each higher education

import matplotlib.pyplot as MPL

def intro():
    print('This program will create a bar graph teacher spent at each school')
def main():
    intro()
    # Lists of data
    schools = ["Army","McDaniel","Stevenson","FrostBurg"]
    months = [6, 36, 14, 22]

    # title our bar graph
    MPL.title("Number of months in each school")
    MPL.xlabel("Schools")
    MPL.ylabel("Months")

    MPL.bar(schools,months)# create our bar
    MPL.show()


main()    
