# This program was made by Harris Domangue for CMSC-201 on Oct. 3rd 2024
# This program will keep track of a server's tops and tell them how much they owe in taxes.

# User display
print("This program will keep track of your tips.")

# get the number of tables
num_of_tables = int(input("How many tables did you serve?: "))

#running total
total_tips = 0

# for loop
for table in range(num_of_tables):
    current = float(input(f"Enter your tip amount ay table #{table+1}: "))
    total_tips += current # add total to tip
    tax = total_tips * .15
    print(f"You have earned ${total_tips:.2f} so far. Taxes ${tax:.2f}")
