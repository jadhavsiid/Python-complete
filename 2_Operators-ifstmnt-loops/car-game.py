# Write a Car Starter progam in python
# Firstly if the user should type 'help' command after execution
# If user typed anything apart from 'help' the program should return- "I don't understand that..."
# If used typed 'help' it should ask user to type between these 3 commands:
# - start : To Start the Car.
# - stop : To Stop the Car.
# - Quit: To Exit.
# Then if user typed 'start', print "Car Started...Ready to go!"
# If user typed 'stop', print "Car Stopped!"
# If user typed 'quit', Break The Loop

while True:
    userInput = input("> "  ).lower()
    if userInput == 'start':
        print("Car Started...Ready to go!")
    elif userInput == 'stop':
        print("Car Stopped!")
    elif userInput == 'quit':
        break
    elif userInput == 'help':
        print("start: To Start the Car.")
        print("stop: To Stop the Car.")
        print("quit: To Exit.")
else:
    print("I don't understand that...")
