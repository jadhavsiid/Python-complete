"""
Suppose during a "Flash Drop," your server is getting hammered with thousands of requests per millisecond. To keep the database from crashing, you need to use the fastest logic possible to determine a user's Shipping Priority. You need a one-liner to reward your most loyal "Hype-Elite" members.

Ask user how many loyalty points they have in a wallet using input() function and storing the points in loyalty_Points variable.

If the loyalty_Points are greater than or equal to 500, the shipping type is "Overnight Express Shipping" 

Otherwise, the shipping type is "Standard Ground Shipping"

store the result in shipping_Type variable
"""

loyalty_Points = int(input("Loyalty Points: "))

shipping_Type =  "Overnight Express Shipping" if loyalty_Points > 500 else "Standard Ground Shipping"
print(shipping_Type)
