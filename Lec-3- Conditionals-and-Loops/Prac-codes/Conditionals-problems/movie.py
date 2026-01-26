"""
Suppose you are building the "Brain" of a new streaming service. You need to recommend a movie based on the user's current mood and the amount of time they have.

Take time (in minutes) and mood (happy, sad, adventurous) as inputs from user using input() function.

If the user has less than 90 minutes, recommend a "Stand-up Comedy Special."

If the user has more than 90 minutes:

If their mood is "Happy", recommend a "Superhero Blockbuster."

If their mood is "Sad", recommend a "Feel-good Animation."

If their mood is "Adventurous", recommend a "Sci-Fi Thriller."

If the input doesn't match any mood, recommend a "Classic Documentary." 
"""

time = input('How many minutes you can watch ? ')
mood = input('How are you feeling (happy, sad or adventurous) ? ').lower()

if int(time) < 90:
    print("Here's a Standup Comedy Special for you !")
else:
    if mood == 'happy':
        print("Here's a Superhero Blockbuster to make you more happy !")
    elif mood == 'sad':
        print("Here's a animated movie to cheer you up !")
    elif mood == 'adventurous':
        print("Here's a Thrilling Science fiction to give you more thirll !")
    else:
        print("Here's a Classic documentary, have a good Watch !!")
