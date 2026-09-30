# This program was made by Harris Domangue for CMSC-201 on Nov 5th 2024
# This program will simulate a cash register simulator

# Variables for possible errors b/c im lazy to type them out later
Error1 = "Sale Canceled!"
Error2 = Error1 + " Customer Needs More Cash!"
Error3 = Error1 + " Reguster Does Not Have Enough Change!"

def intro():
    # Ask user for stuff so program can do its thing yo
    print("This program will work like a cash register")
    
def cash_register():
    # Variables that are actually needed for the program to work
    Customer = 1
    Sale = None
    Amount_given = None
    Change = None
    Number_of_items = None
    is_member  = ""
    Total_sales = 0
    Average_sales = None
    Register_left = None
    file = open("customer_data.txt",'w')
    
    Register_Inital = float(input("How much money is in the register to start: $"))
    print('\u2013' * 40) #dashes to seperate stuff

    while Sale != 0:
        Sale = float(input(f"Enter the sale amount for Customer #{Customer}: $ "))
        is_member = input(f"Is customer #{Customer} a rewards member? ")
        Number_of_items = int(input("How many items did the Customer buy? " ))
        

        if Sale == 0:
            Average_sales = Total_sales % Customer
            print(f"total customers {Customer}, total sales ${Total_sales:.2f}, average sales ${Average_sales:.2f}")
            print("done")
            file.close()
            break
        
        Amount_given = float(input(f"Enter the amount the customer gave:$ "))
        Register_left = Register_Inital

        while Amount_given == 0:
            print(Error1)
            print('\u2013' * 40)  # dashes to separate stuff
            is_member = input(f"Is customer #{Customer} a rewards member? ") # re-enter if the customer is a member
            Number_of_items = int(input("How many items did the Customer buy? " )) # Re-enter the number of items being bought
            Sale = float(input(f"Enter the sale amount for Customer #{Customer}: $ "))  # Re-enter sale amount
            Amount_given = float(input(f"Enter the amount the customer gave: $ "))  # Re-enter amount given


        while Amount_given < Sale and Amount_given != 0:
            print(Error2)
            print('\u2013' * 40) #dashes to seperate stuff
            is_member = input(f"Is customer #{Customer} a rewards member? ") # re-enter if the customer is a member
            Number_of_items = int(input("How many items did the Customer buy? " )) # Re-enter the number of items being bought
            Sale = float(input(f"Enter the sale amount for  Customer #{Customer}:$ "))
            Amount_given = float(input(f"Enter the amount the customer gave:$ "))

        if Amount_given >= Sale:
            Change = Amount_given - Sale
            if Change > Register_left:
                print(Error3)
                print('\u2013' * 40) #dashes to seperate stuff
                is_member = input(f"Is customer #{Customer} a rewards member? ") # re-enter if the customer is a member
                Number_of_items = int(input("How many items did the Customer buy? " )) # Re-enter the number of items being bought
                Sale = float(input(f"Enter the sale amount for Customer #{Customer}:$ "))  
                Amount_given = float(input(f"Enter the amount the customer gave:$ "))  
            else:
                Register_left -= Change
                Total_sales += Sale
                print('\u2013' * 40) #dashes to seperate stuff
                print(f"Change for Customer #{Customer} is {Change:.2f}")
                print('\u2013' * 40) #dashes to seperate stuff
                Customer += 1
                file.write(is_member + "\n")
                file.write(str(Number_of_items) + "\n")
                file.write(str(Sale) + "\n")
                file.write("\n")
        else:
            print(Error2)
            is_member = input(f"Is customer #{Customer} a rewards member? ") # re-enter if the customer is a member
            Number_of_items = int(input("How many items did the Customer buy? " )) # Re-enter the number of items being bought
            Sale = float(input(f"Enter the sale amount for Customer #{Customer}: $ "))  # Re-enter sale amount
            Amount_given = float(input(f"Enter the amount the customer gave: $ "))  # Re-enter amount given

        
def main():
    intro()
    cash_register()
    

if __name__ == '__main__':
    main()
