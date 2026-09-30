# This program will show u how we can create dictonaries in python
# This dictonary is a simple key and value pair using
# Course ID's as keys and Course Names as values
def add_new(courses,key, add = None):
    if add == None:
        add = int(input("Do you want to add this course? 1 for yess 2 for no: "))
    if add == 1:
        courses[key] = input("Enter the course title: ")
    return courses

def database(courses):
    look_up = input("course code to look up: ")
    
    try:
        print(f'{look_up}: {courses[look_up]}')
    except KeyError:
        print(f'{look_up} could not be found')
        add_new(courses,look_up)

def main():
    # dictonary
    courses = {"CMSC-201":"Computer Science 1","CMSC-202":"Computer Science 2", "CMSC-203":"Discrete Structures"}
    choice = None
    while choice != 5:
        print("Menu")
        print("Enter 1 to search\nEnter 2 to Add\nEnter 3 to Delete\nEnter 4 to View\nEnter 5 to exit")
        choice = int(input("Enter  your choice here:"))
        if choice == 1:
            database(courses)
        elif choice == 2:
            add_new(courses,input("Course ID: "),1)
        elif choice == 3:
            courses = delete(courses)
        elif choice == 4:
            print(courses)
        elif choice == 5:
            print("Exiting...")
        print()


def delete(courses):
    code = input("Enter the course id you want to delete: ")
    try:
        del courses[code]
    except KeyError:
        print("Invalid course code")
    return courses
main()
