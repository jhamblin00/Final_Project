#This is the Intro to Python Final Project
#Jackson Hamblin
#LIS 4930

#This game allows the user to get a taste of what it is like to fish...
#in Tampa Bay all from the comfort of your computer.

#This program allows the user to enter different commands in order to:
#Catch a fish
#Use the help function to get a list of all legal commands
#See what there current score is
#See what types of fish they have the chance of catching in the game
#Allows them to terminate the code and exit the program with the quit command


import random   #This library allows for us to generate a random result based on probabilities given
import sys      #This library gives us the quit function allowing for the user to exit the program


random.seed()   #Given to us from the random library this gives us the random number...
                #generator used to determine what fish is caught

points = 0      #Here we define the points to be zero to give the program a reference


#This function is for the help command that gives the user a list of the legal commands
def help():
    print('''
    Cast :  This is the command used to try and catch fish.
    Quit :  This is the command that allows you to terminate the program.
    Score :  This command brings up your current score.
    Type :  This command shows you a list of fish to catch
    Help :  This is the only help you are getting from me!
          ''')


#This is the function for the command that allows the user to fish
def cast():
    global points
    (fish, Score) = results()
    print('You have caught ', end='')
    if fish == None:
        print(name_of_fish(fish) + '.')
        return
    print('a ' + name_of_fish(fish) + '!')
    print('This fish is worth ' + str(Score) + ' points.')
    points += Score


#This function chooses the random fish using the random.range function    
def results():
    catch = random.randrange(100)
    for (fish, percent, Score) in creatures: 
        catch -= percent
        if catch < 0:
            return (fish, Score) 
    assert False


#This function is in place so that the wording is accurate if you catching 'nothing' versus catching 'a' fish
def name_of_fish(fish):
    if fish ==None:
        return "nothing"
    return "a " + fish 


#Using the system library the sys.exit(0) allwos for the user to terminate and quit the program    
def quit():
    print('I hope you enjoyed fishing from the comfort of your computer!')
    sys.exit(0)


#This function allows for the user to see their current score    
def score():
    print('This is your current score', str(points))


#The following is the type of fish with its probability and score which
#the other functions call from to determine the outcomes for everything
creatures = (
        (None, 20, 0),
        ('Redfish', 7.5, 300),
        ('Trout', 9, 150),
        ('Snook', 7.5, 250),
        ('Sheepshead', 18, 100),
        ('Tarpon', 5, 400),
        ('Grouper', 5, 350),
        ('Snapper', 20, 50),
        ('Mackerel', 8, 200)
        )


#Shows the possible types of fish to be caught in the game    
def type():
    print('''
    These are the types of fish you can catch in Tampa Bay:

    Redfish
    Trout
    Snook
    Sheepshead
    Tarpon
    Grouper
    Snapper
    Mackerel

    Just like real life the chance of not catching \n    anything is also possible and MOST likely to occur. ;)
          ''')


#This is where the main loop looks to in order to check if input is a valid command    
commands = {
            'help' : (0,help),
            'quit' : (0,quit),
            'type' : (0,type),
            'cast' : (0,cast),
            'score' : (0,score)
            }


#This is the main loop!
#We have defined all of the functions that make this program work and this
#loop allows for everything to work together given the user's input
print('Welcome to my Fishing from Home game.')
print('The game you are playing is based on the fishery that Tampa Bay has to offer.')
print()
print('To begin fishing use the "Cast" command.')
print('For list of all commands please type "Help".')
while True:
    words = []
    while words == []:
        try:
            cmd = input("> ")
            cmd = cmd.lower()     #This allows for the user's input to be accepted regardless of capitalization
        except EOFError:
            print("quit")
            cmd = "quit"
        words = cmd.split()
    if words[0] in commands:
        (nargs, cmd_fun) = commands[words[0]]
        if len(words) - 1 != nargs:
            print("Oops! That isn't a command. Please try again")
            continue
        if nargs == 0:
            cmd_fun()
        elif nargs == 1:
            cmd_fun(words[1])
        else:
            assert False
        continue
    print("Unknown fishing command. Please try again or make sure Commands are spelled as they are displayed.")



    
