
""" * Tuples in Python
----> Represented by ()
----> They are Immutable
"""

masala_spices = ("cardamom", "cloves","cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cinnamon_ratio = 2,1
print(f"Ginger ratio: {ginger_ratio} and Cinnamon ratio: {cinnamon_ratio}")

ginger_ratio, cinnamon_ratio = cinnamon_ratio, ginger_ratio
print(f"Ginger ratio: {ginger_ratio} and Cinnamon ratio: {cinnamon_ratio}")

# * Membership Testing
print(f"Is ginger present in masala_spices: {'ginger' in masala_spices}")
print(f"Is cloves present in masala_spices: {'cloves' in masala_spices}")