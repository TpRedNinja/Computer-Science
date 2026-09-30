# This program was made by Harris Domangue for CMSC-201 on Sept. 12th 2024
# This program will  convert Celsius to Fahrenheit.

print("This program will convert celsiusto fahrenheit") # display to user

# ask the user for the tempature in degrees
celsius = input("Enter the temperture in celsius: ") # taken as a string incase the user enters a ,
celsius = celsius.replace(",","") # replace the , with nothing
celsius = float(celsius) # convert the numner to a float so we can use it in our calculations

# calculate the equivalent Farhenheit
# F = (9/5)C + 32
fahrenheit = (9/5) * celsius + 32

# display result to user
print(f"The equivalent temperature om Fahrenheit is {fahrenheit:.2f}")
