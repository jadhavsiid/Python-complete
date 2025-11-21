# - Ask user for it's weight
# - Make him choose between the unit in which he gave wieght
# - If the user gave it's weight in kg then convert it to pounds and print it.
# - If the user gave it's weight in pounds then convert it to kg and print it.

weight = input("Enter Your Weight: "  )
pound_or_kilo = input("You entered weight in Pounds(l) or Kilograms (k) ? "  )
if pound_or_kilo == 'k' or pound_or_kilo == 'K':
    weight = int(weight)*2.205
    print(f"Your Weight in Pounds (lbs) is: {weight}")
elif pound_or_kilo == 'l' or pound_or_kilo == 'L':
    weight = int(weight)/2.205
    print(f"Your Weight in Kilograms (kg) is: {weight}")
else:
    print("Invalid Input of unit")