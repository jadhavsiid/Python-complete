order_amount = int(input("Order Amount: "))

delivery_status = 'Delivery is free' if order_amount > 300 else 'Delivery cost is ₹30/-'
print(delivery_status)