# This program was made by Harris Domangue for CMSC-201 on Sept 24th 2024
# This program will tell you if you need a oil change for your car

print("This program will tell you if you should get an oil change") # user display

# constant
OIL_MILEAGE = 6000

# Get Mileage of car at last oil change
start_mileage = int(input("Enter your cars mileage at its last oil change: "))
end_mileage = int(input("Enter your cars current mileage: "))

if end_mileage - start_mileage >= OIL_MILEAGE:
    print("You should get an oil change")
else:
    miles_left = OIL_MILEAGE - (end_mileage - start_mileage)
    print(f"You are good for another {miles_left} miles.")
