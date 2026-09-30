# This program was made by Harris Domangue for CMSC-201 on Oct. 3rd 2024
# This program is the fizzzbuzz challenge

# if %3 'fizz'
# if %5 'buzz'
# if %3 and %5 'fizzbuzz'


# use a for loop to count 1-100
for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print('fizzbuzz')
    elif num % 3 == 0:
        print('fizz')
    elif num % 5 == 0:
        print('buzz')
    else:
        print(num)
