# This program will read random_numbers.txt and display its contents and then
# the program will display the average number.

# main function 
def main():
    intro()
    show_num()
    add_lines()

#intro function
def intro():
    print('This program will read random_numbers.txt and display its contents and then the program will display the average number.')

# show number function 
def show_num():
    try: 
        infile = open('random_numbers.txt','r') #opens file # ERROR 1 no modes
        contents = infile.read() #reads entire file 
        print(contents) # print contents
        
    except IOError: # accepts file error 
        print('Oops... The file can not be found')
        
# add up line totals 
def add_lines():
    try: # tries to open file and perform task 
        infile = open('random_numbers.txt','r') #opens file  # ERROR 2 & 4 no modes/missing '_'
        total = 0 #sets total to zero
        num = infile.readline() # reads the first line 
        while num != '':
            total += int(num) # Adds to total 
            num = infile.readline()

    

        # Finds the average of all 5 numbers 
        total /= 5 
        print(f'The average of these 5 numbers is {total}') # ERROR 5 missing 'f' before "'"

    except IOError: #accepts the file not found error 
        print('Oops... The file can not be found')

if __name__ == '__main__': # ERROR 3 this wasnt here
    main()
