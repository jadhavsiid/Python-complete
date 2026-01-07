"""
You're preparing an order summary with customer names and their total bill.
Task:
- Use two lists: one for names and one for bills.
- Print: "[Name] paid ₹[amount]"
"""
names = ['Siddhesh','Khushi','John','Mike','Rose']
bills = [50, 80, 20, 100, 220]

for name, amount in zip(names, bills):
    print(f"{name} paid ₹{amount} ")
