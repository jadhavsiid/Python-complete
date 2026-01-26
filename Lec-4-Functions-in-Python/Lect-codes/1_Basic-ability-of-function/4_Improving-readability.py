"""
You sell different chai sizes
Instead of writing formulas everywhere, create a function.
Task:
- Write calculate_bill(cups, price_per_cup).
- Return total bill.
- Use this function for multiple orders.
"""

def calculate_bill(cups, price_per_cup):
    # ! way-1
    # return cups*price_per_cup
    # ! Way-2
    total_bill = cups*price_per_cup
    print(f"Your's total is : {total_bill}")

# ! way-1
# total_bill = calculate_bill(4,15)
# print(total_bill)
# ! way-2
calculate_bill(5,10)