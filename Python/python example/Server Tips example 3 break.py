# This program wasmade by Harris Domangue for CMSC-201 on Oct. 1stn2024
# This program will keep track of a servers tips by tables.

# Running Total of Tips made
total_tips = 0
total_tables = 0
table = None #create our table variable

# empty string is our sentinal here
while table != 0:
    total_tables += 1
    table = input(f"Enter the amount at table {total_tables}: ")
    table = table.replace("$","")
    table = table.replace(",","")
    # check if the table is empty spaced
    if table == "":
        break # break keyword breaks  the loop and skips the other statements
    # convert table to float
    table = float(table)
    # add our table to total tips
    total_tips += table

# display amount to user
print(f"You made a total of ${total_tips:.2f} from {total_tables-1} tables")
    
