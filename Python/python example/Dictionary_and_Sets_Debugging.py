# Dictionary Debugging Warm-Up:
# There is a total of 4 errors in this code.
# This code will create a dictionary of for union, intersection, difference &
# symmetric difference where the term will be used as the key
#and the value will be the symbol which can be used to find that value
# between two sets.

# lists of keys and values
listA = ['union','intersection','difference','symmetric']
listB = ['|','&','-','^']

dictionary = {} # dictionary # Error 2: used straight brackets not curly brackets

current_index = 0 # count index
# for loop to load the key and values 
for element in listA:
    dictionary[element] = listB[current_index] # Error 4: Swapped element and current_index 
    current_index += 1 # add the index values 


key = input("Enter a key ('union','intersection','difference','symmetric'): ") # get user input of key

try: # try to display the dictionary key value
    print('Symbol to use:',dictionary[key]) # Error 3: added a s to "key" by mistake

except KeyError: # Error 1: forgot except before key error
    print(key,"not in dictionary") # display if key is not in dictionary
