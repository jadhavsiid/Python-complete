snack = input("Enter your preferred snack: ").lower()
print(f"User Entered: {snack}")

if snack == 'cookies' or snack == 'samosa':
    print(f"Great Choice !! We'll serve you your {snack} with Tea.")
else:
    print("Sorry we only serve cookies or samosa with Tea !!")
