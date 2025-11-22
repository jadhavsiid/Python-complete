# Given is a list [5, 2, 5, 2, 2]
# Based on the list items print the number of 'X' in single line
# Eg: XXXXX
#     XX
#     xxxxx
#     xx
#     xx

# a = [5, 2, 5, 2, 2]
# for var in a:
#     print("X"*var)

a = [2, 2, 2, 2, 5]
for x_count in a:
    output = " "
    for count in range(x_count):
        output+= 'x'
    print(output)
