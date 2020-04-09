# from room import Room

# Declare all the rooms

# room = {
#     'outside':  Room("Outside Cave Entrance",
#                     "North of you, the cave mount beckons"),

#     'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
# passages run north and east."""),

#     'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm."""),

#     'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
# to north. The smell of gold permeates the air."""),

#     'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south."""),
# }


# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# prompts user upon the game being activated
# this variable is also declared in global scope so playGame() can access it
cardinalDirection = input("Please enter the direction you'd like to travel (n, e, s, w, q to quit): ")

def playGame():
    # keeps the game running after the player does something
    gameIsRunning = True

    while gameIsRunning == True:
        global cardinalDirection

        # exits playGame() function/logic
        if cardinalDirection == 'q':
            return
        elif cardinalDirection == 'n':
            print(f"You moved {cardinalDirection}")
            cardinalDirection = input("Please enter the direction you'd like to travel (n, e, s, w, q to quit): ")
        elif cardinalDirection == 'e':
            print(f"You moved {cardinalDirection}")
            cardinalDirection = input("Please enter the direction you'd like to travel (n, e, s, w, q to quit): ")
        elif cardinalDirection == 's':
            print(f"You moved {cardinalDirection}")
            cardinalDirection = input("Please enter the direction you'd like to travel (n, e, s, w, q to quit): ")
        elif cardinalDirection == 'w':
            print(f"You moved {cardinalDirection}")
            cardinalDirection = input("Please enter the direction you'd like to travel (n, e, s, w, q to quit): ")
        else:
            print("Please enter a valid movement command")
            cardinalDirection = input("Please enter the direction you'd like to travel (n, e, s, w, q to quit): ")

    # show this message when the game first loads
    print("Current Room: , Room Description: ")

# game logic triggers everytime the player does something
playGame()