####################
# Steve Mitchell
# Camel game
# First version
####################


# importing random function for random number amount for user decisions, this is a pseudo random not a real random
import random

# introducing the user into the game with a print statement about the game
print("Welcome to Camel!\nYou have stolen a camel to make your way across the great Mobi desert.\nThe natives want their camel back and are chasing you down! Survive your\ndesert trek and out run the natives.")

# variables for gameplay difficulty
done              = False # assigning the variable done with a value to repeat the main loop
miles_traveled    = 0     # the amount of miles the camel has traveled 
thirst            = 0     # the camels thirsrt 
camel_tiredness   = 0     # how tired the camel is 
natives_distance  = -140   # how far away the natives are from you
drinks_in_canteen = 3     # the amount of drinks you currently have to quench thirst

# main game loop to get user input
while not done: #creates a repetetive loop until done is true

    print()
    print("A. Drink from your canteen.") # choice 1 of 6 for the user
    print("B. Ahead moderate speed.")    # choice 2 of 6 for the user
    print("C. Ahead full speed.")        # choice 3 of 6 for the user
    print("D. Stop for the night.")      # choice 4 of 6 for the user
    print("E. Status check.")            # choice 5 of 6 for the user
    print("Q. Quit.")                    # choice 6 of 6 for the user
    print()

    # give the user a choice of A, B, C, D, E or Q and change the user input to an uppercase
    user1 = input("your choice: ")
    print()
    user1 = user1.upper()         

    # if the user enters "Q" or "q" they will change the variable done to True which will end the loop and end the game so they can quit
    if user1 == "Q": 
        done = True 

    # if the user enters "E" or "e" they will print out the game variables 
    elif user1 == "E":
        print("you have travelled: " + str(miles_traveled) + "miles")
        print("drinks in canteen: " + str(drinks_in_canteen))
        print("the natives are " + str(natives_distance) + " miles behind you")
        print()

    # if the user enters "D" or "d" they will rest for the night which will reset the camels tiredness and move up the natives by 7 to 14
    elif user1 == "D":
        camel_tiredness = 0
        print("The camel is happy")
        print()
        natives_distance += random.randrange(7,15) # this will add a random number between 7 and 14 onto the variable natives_distance

    # is the user enters "C" or "c" they will go full spead ahead which will add a range of numbers onto differant variables
    elif user1 == "C":
        miles_traveled += random.randrange(10,21)  # this will make you travel a random distance between 10 and 20 miles
        thirst += 1                                # this will add +1 onto the variable thirst
        camel_tiredness += random.randrange(1,4)   # this will add a random amount betwen 1 and 3 onto the camels tiredness
        natives_distance += random.randrange(7,15) # this will add a random number between 7 and 14 onto the variable natives_distance
        print ("you have travelled: " + str(miles_traveled) + " miles")
        print()

    # if the user enters "B" or "b" they will go at moderate speed which will add a range of numbers onto differant variables
    elif user1 == "B":
         miles_traveled += random.randrange(5,13)   # this will make you travel a random distance between 5 and 12 miles
         thirst += 1                                # this will add +1 onto the variable thirst
         camel_tiredness += 1                       # this will add +1 onto the variable camel_tiredness
         natives_distance += random.randrange(7,15) # this will add a random number between 7 and 14 onto the variable natives_distance
         print ("you have travelled: " + str(miles_traveled) + " miles")
         print()

    # if the user enters "A" or "a" they will drink from the canteen which will make the players thirst 0 and take -1 onto the variable drinks_in_canteen
    elif user1 == "A" and drinks_in_canteen > 0:
        thirst = 0             # this will change the thrist to 0
        drinks_in_canteen -= 1 # this will take 1 away from the number of drinks in the canteen
        print("you quench your thirst")
    else:
        print("you have no drinks left")

    # this will warn the user that the thirst levels are approaching dangerous levels
    if thirst >= 4 and thirst <= 6:
        print ("you are thirsty")

    # this will check if the thirst is greater than 6 then it will tell the user that they died of thrist and end the loop
    if thirst > 6:
        print("you have died of thirst")
        done = True

    # this will warn the user that the camel is getting tired
    if camel_tiredness > 5 and camel_tiredness <8:
        print("your camel is getting tired")

    # this will check if the camels tiredness is greater than 8 and if it is, it will then tell the user the camel died and then change done to true to end to game loop
    elif camel_tiredness > 8:
        print("your camel is dead")
        done = True

    # this will check if the variable natives_distance is less than 15 and if it is it will warn they user that they are getting closer
    if natives_distance >= -15:
        print("the natives are getting closer!")

    # this will check the variable natives_distance and if it is more than 0 the user will be told that the natives caught up and the game loop will end
    elif natives_distance >= 0:
        print("the natives caught you")
        done = True

    # this will check if the variable miles_traveled is greater than or equal to 200 and if it is then it will print out that they won they stop the main game loop
    if miles_traveled >= 200:
        print("you have won!")
        done = True

    #this will create a random chance of encountering an oasis which will reset the pleayer thirst and rest the camel
    if random.randrange(0,20) == 19:
        print ("you have found an oasis, you get a drink and the camel rests")
        thirst = 0
        camel_tiredness = 0

