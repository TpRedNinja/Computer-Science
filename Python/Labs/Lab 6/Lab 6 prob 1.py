# This program is a grocery store total profits program thing?
# This program was made by Harris Domangue on Nov 7th 2024 for CMSC-201

days_of_week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
sales = []

for days in days_of_week:
    sales_for_day = float(input("Enter the sales for " + days + ":"))
    sales.append(sales_for_day)
        
total_sales = sales[0]+sales[1]+sales[2]+sales[3]+sales[4]+sales[5]+sales[6]
min_value = min(sales)
max_value = max(sales)
maxindex = sales.index(max_value)
minindex = sales.index(min_value)
average_sales = total_sales / 7
print(f'The total amount of sales made is ${total_sales:.2f}')
print(f'The min value was ${min_value:.2f} on {days_of_week[minindex]}. While the max value was ${max_value:.2f} on {days_of_week[maxindex]}')
print(f'The average number of sales is ${average_sales:.2f}')

