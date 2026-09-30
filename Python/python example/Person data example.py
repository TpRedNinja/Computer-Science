# This program was made by Harris Domangue for CMSC-201 on Dec. 5th 2024
# This is a person_info class

ID_COUNT = 0
import random

# this is our person class
class PersonInfo:
    def __init__(self,name,address,phone):
        global ID_COUNT
        ID_COUNT += 1
        self.ID = str(ID_COUNT) + '_' + str(random.randint(1000,9999))
        self.__name = name
        self.__address = address
        self.__phone_number = phone

    def get_name(): # gets the name
        return self.__name

    def get_address(): # gets the address
        return self.__address

    def get_phone(): # gets the phone number
        return self.__phone_number

    def set_name(self,name): # sets the name
        self.__name = name

    def set_address(self,address): # sets the address
        self.__address = address

    def set_phone(self,phone): # sets the phone number
        self.__phone_number = phone

    def __str__(self): # string function
        return f"Person Info:\nNAME: {self.__name}\nHOME: {self.__address}\nPHONE: {self.__phone_number}\nID: {self.ID}\n"
#create a sub-class called student info
class StudentInfo(PersonInfo):
    def __init__(self,name,address,phone,year,gpa):
        # call our superclass
        PersonInfo.__init__(self,name,address,phone)
        self.__year = year
        self.__gpa = gpa
    def get_year(self):
        return self.__year
    def get_gpa(self):
        return self.__gpa
    def set_year(self,year):
        self.__year = year
    def set_gpa(self,gpa):
        self.__gpa = gpa
    def __str__(self):
        return PersonInfo.__str__(self) + f"YEAR: {self.__year}\nGPA: {self.__gpa}"
        

# create an instance of our person

me = PersonInfo("Harris Domangue",'1 street drive','123-456-7890')
print(me)

me = StudentInfo("Harris Domangue",'1 street drive','123-456-7890','3rd year of college',3.7)
print(me)


    
        
