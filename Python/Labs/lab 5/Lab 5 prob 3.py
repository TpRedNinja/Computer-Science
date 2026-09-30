# This program was made by Harris Domangue on Nov 7th 2024 for CSMC-201
# This program will read the customer data file and display whats in the file and display stats

def intro():
    print("This program will read the customer data file and display the stats")

def read_data():
    file = open("customer_data.txt","r")
    total_members = 0
    total_items = 0
    total_profits = 0
    is_member = file.readline()
    while is_member != '':
        if is_member != "No" and is_member != "no":
            total_members += 1
        number_of_items = file.readline() # read the number of items
        sale = file.readline() # read the sale
        space = file.readline() # read the empty space
        

        # remove the new line characters from the lines of the file.
        is_member = is_member.rstrip('\n')
        number_of_items = number_of_items.rstrip('\n')
        sale = sale.rstrip('\n')

        

        total_items += int(number_of_items)
        total_profits += float(sale)

        print('Memeber?:',is_member)
        print('Total items:' ,number_of_items)
        print('Total cost: $',sale)
        print('-------------------')
        is_member = file.readline()

    print('Summary stats:')
    print(f'Total members: {total_members}')
    print(f'number of items sold: {total_items}')
    print(f'total profits: ${total_profits:,.2f}')
    file.close

def main():
    intro()
    read_data()

if __name__ == '__main__':
    main()
