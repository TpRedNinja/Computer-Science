import matplotlib.pyplot as MPL


def get_grade_data():
    temp_list = []
    try:
        file = open("grade data.txt","r")
        for num in file:
            num = int(num)
            temp_list.append(num)
        file.close()
    except FileNotFoundError:
        print("File not found")
        input()
    return temp_list
def intro():
    print("This program will display the grades of a class using a pie chart")

#create a main function
def main():
    intro()
    # Lists of data
    grades = ["A's","B's","C's","D's","F's"]
    students = get_grade_data()

    MPL.title("Student grades")
    MPL.pie(students,labels=grades)
    MPL.show()

if __name__ == '__main__':
    main()
