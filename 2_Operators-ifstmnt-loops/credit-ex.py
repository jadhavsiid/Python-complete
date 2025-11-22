# Suppose the price of a house is $1M
# If a buyer has good credit,
# they need to put down 10%
# Otherwise, they need to put down 20%
# print the down payment

price = 1000000
goodcredit = False
if goodcredit:
    print(f"The downpayment will be: ${(price/100)*10}")
else:
    print(f"The downpayment will be: ${(price/100)*20}")
