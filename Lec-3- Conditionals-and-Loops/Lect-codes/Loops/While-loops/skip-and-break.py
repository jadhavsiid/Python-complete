""" Some Chai flavors are out of stock
You want to skip those and stop entirely if
someone requests a restricted flavor.
Task:
- Skip if flavor is "Out of Stock"
- Break if flavor is "Discontinued"
"""
flavours = ["Ginger","Out of Stock","Lemon","Discontinued", "Tulsi"]

for flavour in flavours:
    if flavour == "Out of stock":
        continue
    elif flavour == "Discontinued":
        break
    print(f"Here's your item: {flavour}")
print("Outside the loop, Discontinued item found")