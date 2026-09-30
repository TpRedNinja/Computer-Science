# This program will copy a text file and write the data into a new text file
# This program was made by Harris Domangue on oct 29th 2024 for cscmc-201

# get the file name from the user
filename = input("Enter the file you want to copy: ")
# check if an extension is in the file name
if '.txt' in filename:
    filename = filename.replace('.txt',' ') # remove the extension
    
try: # test our code to see if we have exceptions
    input_file = open(filename + '.txt',"r") # open out file to copy
    
except FileNotFoundError:
    print(filename + "does not exist")

else: # optional this code could just go in the TRY block
    output_file = open("new_file.txt" + '-copy.txt',"w") # open file to write too

    for line in input_file:
        output_file.write(line) # write each line to a file
        print(line,'copied to new_file.')

    # close our files
    input_file.close()
    output_file.close()

finally: # Optional does not even need a block to be honest
    print('Done')
    
    

