# Write a python code to create a number guessing game using while loop
# Decide a number eg 9 and the user has to guess this number
# Ask user to guess and take user's input
# Give the user 3 chances to guess the number, if user did'nt guessed in the provided 3 chances print the message- "Game Over, You Are Out Of Your Chances!!"
# If the user guessed it correctly within the 3 given chance print the message- "You Won!!"

number = 8
chances = 1
noOfChances = 3
while chances <= noOfChances:
    chances+=1
    print("Guess the hidden number:")
    hiddenNo = input()
    if int(hiddenNo) == number:
        print("You Won !!")
        break
else:
    print("Game Over, You Are Out Of Your Chances!!")


