""" List in Python
----> Represented by []
----> Lists in python are mutable objects"""

ingrediants = ["water", "milk", "black tea"]
print(f"The ingrediants are: {ingrediants}")

# * append() --> Add's an item to the end of the list
ingrediants.append('sugar')
print(f"The ingrediants are: {ingrediants}")

# * remove() --> Removes an item from the list
ingrediants.remove('milk')
print(f"The ingrediants are: {ingrediants}")

spice_options = ['ginger', 'cardamom']
chai_ingrediants = ['water', 'milk']

# * extend() --> Used to combine/extend one list with another list
spice_options.extend(chai_ingrediants)
print(f"The new spice_options list is: {spice_options}")


homemade_spices = ["Red Chilli Powder","Mango Pickle","Lemon Pickle"]
print(f"Homemade spices: {homemade_spices}")

# * insert() --> Used to insert an item to the particular index on the list.
homemade_spices.insert(1,"Udad Papad")
print(f"Homemade spices: {homemade_spices}")

# * pop() --> Used to remove an item from the last index of the list.
last_added = homemade_spices.pop()
print(f"Last Added: {last_added} ")
print(f"Homemade spices: {homemade_spices}")


numlist = [26, 19, 12, 96, 74]
print(f"Numlist: {numlist}")

# * reverse() --> Used to reverse the order of items in the list.
numlist.reverse()
print(f" Reversed Numlist: {numlist}")

wordslist = ['Siddhesh','John',"Mike","Alexa","Benjamin","Emily"]
print(f"Wordlist: {wordslist}")

# * sort() --> Used to sort the order of items in the list in ascending order
wordslist.sort()
print(f"Sorted Wordlist: {wordslist}")
numlist.sort()
print(f"Sorted Numist: {numlist}")


# * max() --> Used to fetch max number from the list
print(f"Max number in numlist: {max(numlist)}")
# * sort() --> Used to fetch min number from the list
print(f"Max number in numlist: {min(numlist)}")

# * Operator Overloading
base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

liquid_mix = base_liquid + extra_flavor
print(f"liquid_mix: {liquid_mix}")

strong_brew = ["black tea","water"]*3
print(f"strong_brew: {strong_brew}")

# * ByteArray
raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}")