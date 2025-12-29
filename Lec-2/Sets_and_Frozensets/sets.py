essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

# * Union
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

# * Intersection
common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}")

# * Difference
only_in_essential = essential_spices - optional_spices
print(f"Only in essentials: {only_in_essential}")

# * Membership test
print(f"Is 'cloves' in essential spices ? {'cloves' in essential_spices}")
print(f"Is 'cloves' in optional spices ? {'cloves' in optional_spices}")
