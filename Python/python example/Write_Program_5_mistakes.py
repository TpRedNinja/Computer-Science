# This program will generate 5 random numbers and then write them to a text file
# called random_numbers.txt.
import random #import random 
file_object = open('random_numbers.txt','w') #open text file

#intro function
def intro(): # ERROR 1 no indentation
    print('This program will generate 5 random numbers and then write them to a text file called random_numbers.txt')

def main(): # ERROR 2 forgot ':'
    intro() # call intro function 
    input('Press enter to begin')
    for i in range(1,6): #for loop # ERROR 6 would make 6 numbers instead of 5 numbers
        random_num() # calls random number # ERROR 3 mising '_'
    file_object.close() #closes file 

def random_num():
    number = random.randint(1,1000) #randomly generates numbers # ERROR 4 num to number
    print('The number',number,'has been written to text file')
    file_object.write(str(number) + "\n") #write to text file # ERROR 5 convert int to string

#main function
if __name__ == '__main__':
    main()
