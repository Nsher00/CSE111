import math
from datetime import datetime

current_date = datetime.now(tz=None)
###day_of_week = current_date.weekday()
###This next line is for testing it out for other days. Just uncomment it out and comment out the outher date of week to do a test. 
day_of_week = 2
discount_amount = 0
user_input = float(input("Please enter the subtotal: "))
if day_of_week == 1 or 2 and user_input > 50:
    discount_amount = user_input * 0.1
    user_input = user_input - discount_amount
    print("Discount:" , round(discount_amount, 2))
sales_tax = user_input * 0.06
total_amount = user_input + sales_tax

if day_of_week == 1 or 2 and user_input < 50:
    amount_for_discount = 50 - user_input
    print("To qualify for a discount you only have to spent:" , amount_for_discount)


print("Sales Tax:" , round(sales_tax, 2))
print("Total Amount:" , round(total_amount, 2))