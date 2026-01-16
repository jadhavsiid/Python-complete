
# * Traditional Way
# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is: {remainder}")

# * Walrus operator way
value = 13
if(remainder := value % 5):
    print(f"Not divisble, remainder is {remainder}")

# available_sizes = ["small","medium","large"]
# if(requeste_size := input("Enter your chai cup size: ")) in available_sizes:
#     print(f"Serving: {requeste_size}")
# else:
#     print(f"Requested size {requeste_size} not available")

chai_flavors = ["masala","ginger","lemon"]
print(f"Available flavors: {chai_flavors}")

while (flavor := input("Choose your flavor: ")) not in chai_flavors:
    print(f"Sorry, {flavor} is not available")

print(f"Serving your {flavor} chai!!")