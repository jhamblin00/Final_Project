# Final_Project
This is the final project for the Intro to Python LIS 4930 course
#Jackson Hamblin

For my final I made a fishing game. In this game you input a command to get a random output which in this case is casting a line to potentially catch a fish.

I have several commands that the user may input in order to interact with the game.

The user may input: cast, type, help, score, and quit.
One point I made sure to hit was usnig the .lower function to make it so whatever capitalization the user uses the program will still read it correctly.
This allows for a better user experience.

I used the system library in order to give the option of terminating and exiting the program.
I also used the random library for the purpose of getting a function that randomly chooses a catch based on the probabilities I entered.

I first decided what type of commands I would want to use.
After doing that I then decided what fish the user can catch along with the points and probabiliy associated with that fish. 
The next step was to go and figure out the main loop that everything would revolve around. The goal of the main loop was to accept the legal commands and then if none were detected, produce a certain repsonse prompting the user to try again.
From that point I wa able to go and add each command and the neccessary functions one at a time making it easy to attack this project piece by piece.

I have tested my game many times and thus far have not gotten any sort of error or problem to show itself.
