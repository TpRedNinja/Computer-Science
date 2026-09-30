NUMBERS = None
def numbers():
    global NUMBERS
    NUMBERS = input("Put in your list of Numbers in any order but least to greatest: ")
    

def sort():
    global NUMBERS
    if "," in NUMBERS:
        List_to_sort = NUMBERS.split(",")
    elif " " in NUMBERS:
        List_to_sort = NUMBERS.split(" ")
    else:
        pass
    print(List_to_sort)

     

def main():
    numbers()
    sort()

if __name__ == '__main__':
    main()
    
    
    
