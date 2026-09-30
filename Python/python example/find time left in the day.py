# This program was made by Harris Domangue for CMSC-201 on Sept. 19th 2024
# This program will  tell you how many hours and minutes you have left in the day.

# named constants
DAY = 23
HOUR = 60

#named variables
isAm = True
error = False

# get the time from the user
# take time in as a string
current_time = (input("Enter the current time: "))

# split the time by ":" and store the two in these variables
current_hour,current_minute = current_time.split(":")
current_minute = current_minute.lower() # sets the characters to lowercase
if "am" in current_minute:
    current_minute = current_minute.replace("am","")
elif "pm" in current_minute:
    is_Am = False
    current_minute = current_minute.replace("pm","")
else:
    error = True

# convert the strings to int values so that we can calculate them.
current_hour = int(current_hour)
current_minute = int(current_minute)


if isAm:
    hour_left = DAY - current_hour # find the number of hours left in day
    minute_left = HOUR - current_minute # find the number of minutes left in day
    if current_hour == 12: # add 12 to midnight time
        hour_left +=12
else:
    hour_left = DAY - current_hour - 12 # find the number of hours left in day
    minute_left = HOUR - current_minute # find the number of minutes left in day
    if current_hour == 12: # add 12 to midnight time
        hour_left +=12
    
    hour_left -= 12 # to counteract pm value

# display time left
if minute_left == 60:
    hour_left +=1
    minute_left =0
print(f" There are {hour_left} hours and {minute_left} minutes left in the day")
