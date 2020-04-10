from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons", ['staff']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['torch']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

player = Player('Jaytee', room['outside'])


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

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

commands = ['n', 'e', 's', 'w', 'q', 'grab', 'drop']

def handlePlayerMovement(playerInput):
    if hasattr(player.current_room, f"{playerInput}_to"):
        # update the current_room that the player is in
        linkedRoom = getattr(player.current_room, f"{playerInput}_to")
        player.current_room = linkedRoom

    else:
        print("\nCan't travel that direction")

# handles all interactions of items between the player and current room they're in
def handleItems(playerAction, itemName):
    if playerAction == 'grab':
        # check if the item currently exists in the room
        if itemName in player.current_room.inventory:
            player.inventory.append(itemName)
            player.current_room.inventory.remove(itemName)
            print(f"\nYou picked up: {itemName}")
        else:
            print("\nThat item doesn't exist")

    elif playerAction == 'drop':
        # check if the item currently exists in player's inventory
        if itemName in player.inventory:
            player.inventory.remove(itemName)
            player.current_room.inventory.append(itemName)
            print(f"\nYou dropped: {itemName}")
        else:
            print("\nThat item doesn't exist")


def checkPlayerInput(playerInput):
    # if playerInput is a single value, it is a movement value, make sure it's a valid movement
    if len(playerInput) == 1:
        # check if the input exists in commands list
        if playerInput[0] in commands:
            if playerInput[0] == 'q':
                quit()
            elif playerInput[0] == 'grab' or playerInput[0] == 'drop':
                print("\nPlease specify the name of the item you want to pick up after a 'grab' or 'drop' command")
            else:
                handlePlayerMovement(playerInput[0])
        else:
            print("\nPlease enter a valid command")

    # 2 input values means the player is trying to grab or drop an item
    elif len(playerInput) == 2:
        # check if the input exists in commands list
        if playerInput[0] in commands:
            handleItems(playerInput[0], playerInput[1])
        else:
            print("\nPlease enter a valid command")

    else:
        print("\nPlease enter a valid command")

def playGame():
    # keeps the game running after the player does something
    gameIsRunning = True

    while gameIsRunning == True:
        # show the player's current location
        print(f"\nCurrent location: {player.current_room.name},\n{player.current_room.desc}\n")

        # if the player has anything in their inventory, display their inventory
        if len(player.inventory) > 0:
            print(f"Player Inventory: {player.inventory}\n")

        # if there is an item in the room, display it
        if(len(player.current_room.inventory) > 0):
            print(f"This room has stuff you can grab: {player.current_room.inventory}\n")

        # get player input from prompt
        playerInput = input("What would you like to do? [n/e/s/w/grab/drop/q to quit]: ").lower().split(' ')

        # check for validity of player's input
        checkPlayerInput(playerInput)

# game logic triggers everytime the player does something
playGame()