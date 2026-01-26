"""Suppose you are the lead engineer for "Chef-Bot 5000," a high-end, AI-powered culinary droid in a 5-star restaurant. You need to program the Robot's arm to react instantly to the Head Chef’s one-word commands. If the robot fumbles, the restaurant loses a Michelin star.

Take chef's command using input() inside a chefCommad variable.

If the command is "Sizzle", the robot must Drop the Wagyu steak on the grill.

If the command is "Plate", the robot must Perform a 5-point artistic sauce drizzle.

If the command is "Raw", the robot must Throw the dish in the bin and apologize profusely.

If the command is "Order" OR "Service", the robot must Ring the bell and shout "Pick up!" (Use the | pipe for this!).

For any other command (like the Chef just venting), the robot should Silently keep chopping onions.

Write a program that takes chef_command as input and uses a single match statement to handle the kitchen chaos."""

chef_Command = input("Chef's command is " ).lower()

match chef_Command:
    case 'sizzle':
        print("Drop the Wagyu steak on the grill.")
    case 'plate':
        print("Perform a 5-point artistic sauce drizzle")
    case 'raw':
        print("Throw the dish in the bin and apologize profusely")
    case 'order' | 'service':
        print('Ring the bell and shout "Pick up!"')
    case _:
        print("keep chopping onions")