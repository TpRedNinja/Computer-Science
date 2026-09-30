# This program was made by Harris Domangue for CMSC-201 on Sept. 26th 2024
# This program will tell you your pay grade base off your rank and how many years you have served

# user display
print("This program will tell you your pay grade base off your rank and how many years you have served")

# Global thing for pay
BASIC = 2017.20
AIRMAN = 2261.10
FIRSTCLASS = 2680.20

# asks for users rank and years served
User_rank = int(input("What is your rank?: E-"))
Years_served = int(input("How many years have you served?: "))
    

if User_rank == 1: # this rank no matter the years has the same monthly pay
    print(f"Your rank is Airman basic you will make no matter your years of service: ${BASIC:,.2f} monthly")
elif User_rank == 2: # this rank no matter the years has the same monthly pay 
    print(f"Your rank is Airman you will make no matter your years of service: ${AIRMAN:,.2f} monthly")
elif User_rank == 3:
    if Years_served < 2:
        print("Your rank is Airman first class you make $ monthly")
    elif Years_served == 2:
        print("Your rank is Airman first class you make $ monthly")
    elif Years_Served > 2:
        print(f"Your rank is Airman first class you make ${FIRSTCLASS:.,2f} monthly after 3 or more years of service")
elif User_rank == 4:
    if Years_served < 2:
        print("Your rank is Senior Airman you will make $2,633.70 monthly")
    elif Years_served == 2:
        print("Your rank is Senior Airman you will make $2,768.40 monthly")
    elif Years_served == 3:
        print("Your rank is Senior Airman you will make $2,918.40 monthly")
    elif Years_served >= 4:
        print("Your rank is Senior Airman you will make $3,066.30 monthly")
elif User_rank == 5:
    if Years_served < 2:
        print("Your rank is Staff Sergent you will make $2,872.20 monthly")
    elif Years_served == 2:
        print("Your rank is Staff Sergent you will make $3,065.70 monthly")
    elif Years_served == 3:
        print("Your rank is Staff Sergent you will make $3,214.20 monthly")
    elif Years_served >= 4:
        print("Your rank is Staff Sergent you will make $3,365.70 monthly")
else:
    print("Error please enter a number between 1 and 5") # displays error if rank is less than 1 or greater than 5

if Years_served > 1:
    print("Error please enter a number more than 0")
