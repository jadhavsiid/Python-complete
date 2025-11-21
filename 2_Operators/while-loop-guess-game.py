# Write a python code to create a number guessing game using while loop
# Decide a number eg 9 and the user has to guess this number
# Ask user to guess and take user's input
# Give the user 3 chances to guess the number, if user did'nt guessed in the provided 3 chances print the message- "Game Over, You Are Out Of Your Chances!!"
# If the user guessed it correctly within the 3 given chance print the message- "You Won!!"

number = 8
chance = 1
while chance <=3:
    usersGuess = input("Guess the hidden number: "  )
    if int(usersGuess) == number:
        print('You Won!!')
    else:
        print("Try Again!!")
    chance+=1
print("Game Over, You Are Out Of Your Chances!!")
