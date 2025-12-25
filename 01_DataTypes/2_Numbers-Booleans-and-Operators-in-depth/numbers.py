
#! Integer
black_tea_in_gm = 14
ginger_in_gm = 3

total_gms = black_tea_in_gm + ginger_in_gm
print(f"Total gms of base tea is {total_gms}")
remaining = black_tea_in_gm - ginger_in_gm
print(f"Total gms of remaning tea is {remaining}")

milk_ltrs = 7
servings = 4
prod = milk_ltrs *servings
milk_per_serving = milk_ltrs / servings
print(f"Milk per serving: {milk_per_serving}")
milk_per_serving = milk_ltrs // servings
print(milk_per_serving) # ! this will remove the decimal point and number after it
print(f"Product: {prod}")

# ! Modulus
total_Cardamom_pods = 10
pods_per_cup = 3
leftover_pots = total_Cardamom_pods % pods_per_cup
print(f"The leftover pots are: {leftover_pots}")

base_flavor_strength = 2
scale_factor = 3
powerful_flavor = base_flavor_strength ** scale_factor
print(f"The power is: {powerful_flavor}")

# ! Large no in python
noOfSubs = 1_00_00_00
print(f"The number of Subs: {noOfSubs}")

# ! Booleans
isBoiling = True
striCount = 5
total_actions = isBoiling + striCount # ! Called as upcasting
print(f"Total Actions: {total_actions}")

# milk_present = "Siddhesh"
milk_present = None
print(f"Is Milk present: {bool(milk_present)}")

# ! Logical Operations (AND, OR, NOT)
water_hot = True
tea_added = False
# can_serve = water_hot and tea_added
can_serve = water_hot or tea_added
print(f"Can the Tea be served ? {can_serve}")

# ! Real Numbers
ideal_temp = 95.5
# current_temp = 95.49999999
current_temp = 95.49
print(f"ideal temp: {ideal_temp}")
print(f"current temp: {current_temp}")
print(f"difference in temp: {ideal_temp - current_temp}")