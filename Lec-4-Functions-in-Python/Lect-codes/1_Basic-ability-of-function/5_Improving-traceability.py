"""
Your shop adds a 10% VAT on every order.
You want this to be consistent and traceable.

Task:
- Write add_vat(price, vat_rate).
- Use it to compute final prices for 3 orders.
"""


def add_vat(price, vat_rate):
    return price + price * (vat_rate/100)

"""
--- Basic Formula of calculating VAT---

VAT   = Net Price X VAT Rate/100
amount   
     
"""
orders = [100, 150, 200]
for order in orders:
    print(f'Original price: {order}')
    final_price  = add_vat(order,10)
    print(f'The final price is: {final_price}')

