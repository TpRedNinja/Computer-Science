# This program wasmade by Harris Domangue for CMSC-201 on Oct 1st
# This program uses a while loop to solve the fizzbuzz challenge

# If a number % 3 == 0 print fizz
# If a number % 5 == 0 print buzz
# If a number % 3 == 0 AND number % 5 == 0 print fizzbuzz

# create our counting variable
count = 1
while count <= 100:
    if count % 3 == 0 and count % 5 == 0:
        print("FizzBuzz")
    elif count % 3 == 0:
        print("Fizz")
    elif count % 5 == 0:
        print("Buzz")
    else:
        print(count)
    count += 1
