"""
Group Members: # Dan To Amelia Doe & H Grasso
"""

# DO NOT CHANGE OR REMOVE THE FOLLOWING LINES
import random
import dungeon
import player
import screen
import utilities
import werewolf

# DO NOT CHANGE OR REMOVE THE PRECEDING LINES


# CONSTANTS --- DO NOT CHANGE THESE VALUES ANYWHERE
KEYBOARD_UP: str = 'w'
KEYBOARD_DOWN: str = 's'
KEYBOARD_LEFT: str = 'a'
KEYBOARD_RIGHT: str = 'd'
KEYBOARD_LOOK: str = 'l'
KEYBOARD_TAKE: str = 't'
KEYBOARD_USE: str = 'u'
KEYBOARD_QUIT: str = 'Q'
KEYBOARD_LOAD_GAME: str = 'L'
KEYBOARD_SAVE_GAME: str = 'S'
KEYBOARD_SHOW_HELP: str = 'h'

# MEMBER VARIABLES --- DO NOT CHANGE INITIAL VALUES, BUT YOU CAN ASSIGN NEW VALUES ELSEWHERE IN CODE
last_message: str = ''  # The message to show the user from their last action.


def get_user_command() -> str:
    """
    Asks the user for a command. Repeats asking until user enters valid command. Returns command.
    :return: str, single character valid command
    """
    while True:
        user_input = input('Enter a command: ')
        if user_input in [
            KEYBOARD_UP,
            KEYBOARD_DOWN,
            KEYBOARD_LEFT,
            KEYBOARD_RIGHT,
            KEYBOARD_LOOK,
            KEYBOARD_TAKE,
            KEYBOARD_USE,
            KEYBOARD_QUIT,
            KEYBOARD_LOAD_GAME,
            KEYBOARD_SAVE_GAME,
            KEYBOARD_SHOW_HELP,
        ]:
            break
        screen.write('Bad input. Try again. ')
    return user_input


def do_command(command: str) -> bool:
    """
    Performs the command.
    :param command: str, single character representing a user's command
    :return: bool, True if game should keep going, False if user wants to quit
    """
    global last_message  # DO NOT REMOVE --- ALLOWS YOU TO ACCESS MEMBER VARIABLES DEFINED ABOVE
    if player.is_alive():
        # These commands can only be done if the player is alive:
        if command == KEYBOARD_UP:
            player.set_symbol(player.LOOKING_UP)
            if player.is_open_space(player.x, player.y - 1):
                player.y -= 1
        elif command == KEYBOARD_DOWN:
            player.set_symbol(player.LOOKING_DOWN)
            if player.is_open_space(player.x, player.y + 1):
                player.y += 1
            # Doneish: Update the player's symbol so it is facing down.
            # Doneish: If the player can move down one square, then move the player down one square.
        elif command == KEYBOARD_LEFT:
            player.set_symbol(player.LOOKING_LEFT)
            if player.is_open_space(player.x - 1, player.y):
                player.x -= 1
            # Doneish: Update the player's symbol so it is facing left.
            # Doneish: If the player can move left one square, then move the player left one square.
            pass
        elif command == KEYBOARD_RIGHT:
            player.set_symbol(player.LOOKING_RIGHT)
            if player.is_open_space(player.x + 1, player.y):
                player.x += 1
            # Doneish: Update the player's symbol so it is facing right.
            # Doneish: If the player can move right one square, then move the player right one square.
            pass
        elif command == KEYBOARD_LOOK:
            do_look(player.x, player.y, player.get_symbol())
        elif command == KEYBOARD_TAKE:
            do_take(player.x, player.y, player.get_symbol())
        elif command == KEYBOARD_USE:
            do_use(player.x, player.y, player.get_symbol())

    # Okay to do alive or dead:
    if command == KEYBOARD_QUIT:
        return False
    elif command == KEYBOARD_LOAD_GAME:
        werewolf.skip_turn = True
        # TODOish: Mark the werewolf's turn to be skipped.
        do_load_game()
    elif command == KEYBOARD_SAVE_GAME:
        werewolf.skip_turn = True
        # TODOish: Mark the werewolf's turn to be skipped.
        do_save_game()
    elif command == KEYBOARD_SHOW_HELP:
        werewolf.skip_turn = True
        # TODOish: Mark the werewolf's turn to be skipped.
        do_show_help()

    # Handle the werewolf after doing user command.
    werewolf.do_next_move(player.x, player.y)
    do_check_for_player_damage()
    return True


def do_look(from_x: int, from_y: int, looking_direction: str):
    """
    Updates last_message with a description of the map square that you would be looking at
    if you were at location (from_x, from_y) with the given direction.
    :param from_x: int, horizontal index in the map
    :param from_y: int, vertical index in the map
    :param looking_direction: str, single character representing which way you're looking
    """
    global last_message   # DO NOT REMOVE --- ALLOWS YOU TO ACCESS MEMBER VARIABLES DEFINED ABOVE

    # if looking_direction == player.LOOKING_RIGHT:
    #     object_x = from_x + 1
    # if looking_direction == player.LOOKING_LEFT:
    #     object_x = from_x - 1
    # if looking_direction == player.LOOKING_UP:
    #     object_y = from_y - 1
    # if looking_direction == player.LOOKING_DOWN:
    #     object_y = from_y + 1
    object_x, object_y = player.get_looking_at_location(from_x, from_y, looking_direction)

    # TODOish: Set the values of object_x and object_y so they match the location of the square that you would be
    # looking at given the parameter values. See description.
    if object_x == werewolf.x and object_y == werewolf.y:  # TODOish: Replace False with a condition that checks if
        # (object_x, object_y) matches the werewolf's location.
        if werewolf.is_alive():  # TODOish: Replace False with a condition that checks if werewolf is alive.
            if werewolf.is_stunned():  # TODOif: Replace False with a condition that checks if werewolf is stunned.
                last_message = "The werewolf is temporarily stunned, but it will wake soon."
            else:
                last_message = "Putrid saliva drips from the werewolf's fangs. It can smell your fear."
        else:
            last_message = "The werewolf's death brings little comfort. What other nightmares lurk in this dungeon?"
    else:
        # map_square = object_x and object_y  # TODOish: Replace the None with code that gets the map square at location
        # (object_x, object_y).
        map_square = dungeon.dungeon_map[object_y][object_x]
        default = "You're not sure what it is. You've never seen anything like it before."
        last_message = {
            dungeon.MAP_SQUARE_CHASM: "The chasm in front of you is too wide to jump across. Perhaps there's another way across?",
            dungeon.MAP_SQUARE_EMPTY: "You see nothing of interest.",
            dungeon.MAP_SQUARE_HEALTH: "Two breadsticks, one laying across the other. Did someone leave this for you? Strange.",
            dungeon.MAP_SQUARE_KEY: "There is a shiny key on the ground. But what is it for?",
            dungeon.MAP_SQUARE_LOCK: "The door in front of you is locked.",
            dungeon.MAP_SQUARE_PEBBLE: "You see a large pebble on the ground. Stepping on it would hurt.",
            dungeon.MAP_SQUARE_PEBBLES: "You see two large pebbles on the ground. Stepping on them would hurt.",
            dungeon.MAP_SQUARE_PLANK: "There is a long plank of wood on the ground. You wonder how it got there.",
            dungeon.MAP_SQUARE_PLANK_SET: "The two sides of the chasm are bridged by a long plank of wood.",
            dungeon.MAP_SQUARE_ROPE: "Someone left a long stretch of rope just lying around. How irresponsible.",
            dungeon.MAP_SQUARE_ROPE_TIED: "A rope dangles above the chasm in front of you. You can just barely reach it.",
            dungeon.MAP_SQUARE_ROCK: "The rock wall in front of you is dusty with age. Try not to sneeze.",
        }.get(map_square, default)


def do_take(from_x: int, from_y: int, looking_direction: str):
    """
    Takes item from the map square that you would be looking at if you were at
    location (from_x, from_y) with the given direction. Updates last_message.
    :param from_x: int, horizontal index in the map
    :param from_y: int, vertical index in the map
    :param looking_direction: str, single character representing which way you're looking
    """
    global last_message  # DO NOT REMOVE --- ALLOWS YOU TO ACCESS MEMBER VARIABLES DEFINED ABOVE
    # object_x = from_x
    # object_y = from_y
    # if looking_direction == player.LOOKING_RIGHT:
    #     object_x = from_x + 1
    # if looking_direction == player.LOOKING_LEFT:
    #     object_x = from_x - 1
    # if looking_direction == player.LOOKING_UP:
    #     object_y = from_y - 1
    # if looking_direction == player.LOOKING_DOWN:
    #     object_y = from_y + 1
    object_x, object_y = player.get_looking_at_location(from_x, from_y, looking_direction)

    # TODOish: Set the values of object_x and object_y so they match the location of the square that you would be
    #  looking at given the parameter values. See description.
    map_square = dungeon.dungeon_map[object_y][object_x]  # ish: Replace the None with code that gets the map square at
    # location
    # (object_x, object_y).
    responses = {
        dungeon.MAP_SQUARE_HEALTH: "Nom nom! Eating bread makes you feel stronger.",
        dungeon.MAP_SQUARE_KEY: "You pick up the key.",
        dungeon.MAP_SQUARE_PEBBLE: "You pick up a pebble.",
        dungeon.MAP_SQUARE_PEBBLES: "You pick up a couple pebbles.",
        dungeon.MAP_SQUARE_PLANK: "You pick up a plank of wood.",
        dungeon.MAP_SQUARE_ROPE: "You pick up a long rope.",
        dungeon.MAP_SQUARE_SLINGSHOT: "You pick up a slingshot.",
    }
    if map_square in responses:
        last_message = responses[map_square]
        player.inventory_add(map_square)
        dungeon.clear_map_square(object_x, object_y, map_square) # revise
        # TODOish: Add map_square to player's inventory.
        # TODOish: Clear the map at location (object_x, object_y).
    else:
        last_message = "There is nothing to take."


def do_use(from_x: int, from_y: int, looking_direction: str):
    """
    Use item as if you were at location (from_x, from_y) with the given direction. Updates last_message.
    :param from_x: int, horizontal index in the map
    :param from_y: int, vertical index in the map
    :param looking_direction: str, single character representing which way you're looking
    """
    global last_message  # DO NOT REMOVE --- ALLOWS YOU TO ACCESS MEMBER VARIABLES DEFINED ABOVE
    screen.write("What would you like to use? ")
    item = input()
    if item == dungeon.MAP_SQUARE_SLINGSHOT and\
        player.inventory_has(dungeon.MAP_SQUARE_SLINGSHOT) and\
        not player.inventory_has(dungeon.MAP_SQUARE_PEBBLE):
        last_message = "Can't use the slingshot without ammunition."
    elif not player.inventory_has(item):
        last_message = "You don't have any."
    else:
        last_message = None
        # object_x = from_x
        # object_y = from_y
        # if looking_direction == player.LOOKING_RIGHT:
        #     object_x = from_x + 1
        # if looking_direction == player.LOOKING_LEFT:
        #     object_x = from_x - 1
        # if looking_direction == player.LOOKING_UP:
        #     object_y = from_y - 1
        # if looking_direction == player.LOOKING_DOWN:
        #     object_y = from_y + 1
        object_x, object_y = player.get_looking_at_location(from_x, from_y, looking_direction)
        # TODOish: Set the values of object_x and object_y so they match the location of the square that you would be looking at given the parameter values. See description.
        map_square = dungeon.dungeon_map[object_y][object_x]
        if item == dungeon.MAP_SQUARE_PLANK and map_square == dungeon.MAP_SQUARE_CHASM:
            player.inventory_use(item)
            dungeon.dungeon_map[object_y][object_x] = dungeon.MAP_SQUARE_PLANK_SET
            last_message = "You lay the plank of wood over the chasm. It just barely touches both sides."
        if item == dungeon.MAP_SQUARE_ROPE and map_square == dungeon.MAP_SQUARE_CHASM:
            player.inventory_use(item)
            dungeon.dungeon_map[object_y][object_x] = dungeon.MAP_SQUARE_ROPE_TIED
            last_message = "Standing on the tips of your toes, you reach up and tie the rope to a beam above you."
        if item == dungeon.MAP_SQUARE_PEBBLE and map_square == dungeon.MAP_SQUARE_CHASM:
            player.inventory_use(item)
            last_message = "You drop a pebble into the chasm, counting the seconds until it hits the bottom. You hear nothing."
        if item == dungeon.MAP_SQUARE_KEY and map_square == dungeon.MAP_SQUARE_LOCK:
            player.inventory_use(item)
            dungeon.dungeon_map[object_y][object_x] = dungeon.MAP_SQUARE_EMPTY
            last_message = "You turn the key. Hard. Just as the lock opens you feel the key snap in half."

        if item == dungeon.MAP_SQUARE_SLINGSHOT:
            if player.is_looking_at(werewolf.x, werewolf.y) and \
                    utilities.manhattan_distance(player.x, player.y, werewolf.x, werewolf.y) <= player.SLINGSHOT_DISTANCE:
                player.inventory_use(dungeon.MAP_SQUARE_PEBBLE)
                damage_points = random.randint(1, player.SLINGSHOT_MAX_DAMAGE)
                werewolf.do_hit(damage_points)
                last_message = "You hit the werewolf! "
                if werewolf.is_alive():
                    werewolf.stunned_count = werewolf.stunned_count + 2
                    last_message += "The beast is temporarily stunned. The werewolf took "
                    last_message += str(damage_points)
                    last_message += " point" if damage_points == 1 else " points"
                    last_message += " of damage."
                else:
                    last_message += "You have killed the werewolf."
            else:
                pebble_destination_x, pebble_destination_y = player.get_farthest_actionable_location(player.SLINGSHOT_DISTANCE, True)
                distance_shot = utilities.manhattan_distance(player.x, player.y, pebble_destination_x, pebble_destination_y)
                if distance_shot > 0:
                    player.inventory_use(dungeon.MAP_SQUARE_PEBBLE)
                    dungeon.dungeon_map[pebble_destination_y][pebble_destination_x] = dungeon.MAP_SQUARE_PEBBLE #dungeon func
                    last_message = "The pebble you shot lands "
                    last_message += str(distance_shot)
                    last_message += " square" if distance_shot == 1 else " squares"
                    last_message += " away."
                else:
                    last_message = "There is nothing to shoot your slingshot at."
        if last_message is None:
            last_message = "You can't use that here."

def do_check_for_player_damage():
    """
    If the player and the werewolf are at the exact same location AND the werewolf is
    alive AND the werewolf is not stunned, THEN the werewolf does damage to the player.
    Updates last_message.
    """
    global last_message  # DO NOT REMOVE --- ALLOWS YOU TO ACCESS MEMBER VARIABLES DEFINED ABOVE
    if player.x == werewolf.x and player.y == werewolf.y and werewolf.is_alive() and not werewolf.is_stunned():
        damage_points = random.randint(1, werewolf.WEREWOLF_MAX_DAMAGE)
        player.do_player_hit(damage_points)
        if player.is_alive():
            new_werewolf_location = dungeon.get_random_empty_location(player.x, player.y,
                                                                werewolf.WEREWOLF_POST_ATTACK_MIN_TELEPORT_DISTANCE)
            if new_werewolf_location is not None:
                werewolf.x, werewolf.y = new_werewolf_location
            last_message = ''.join([
                "You have been ",
                random.choice(["scratched", "clawed", "kicked", "bitten"]),
                " by the werewolf. The beast dealt ",
                str(damage_points),
                " point" if damage_points == 1 else " points",
                " of damage.\n",
                "It has been teleported to a random location in the dungeon." if new_werewolf_location else\
                    "The dungeon is too small to teleport the werewolf somewhere else."
            ])
        else:
            last_message = "You have been killed by a werewolf."


def do_load_game():
    """
    Asks the user which game slot to load a game from.
    Call's the dungeon's load_game() function and, if it was successful, updates the player and werewolf data.
    Updates last_message.s
    """
    global last_message  # DO NOT REMOVE --- ALLOWS YOU TO ACCESS MEMBER VARIABLES DEFINED ABOVE
    screen.write("Enter a digit 0-9 to load a saved game.\nEnter any other character to cancel.\nGame slot: ")
    slot_number = input()
    if len(slot_number) != 1 and not slot_number.isdigit():
        last_message = "Must enter 0-9 to load a saved game."
    else:
        filename = f'gameSlot{slot_number}.txt'
        player_data = dungeon.load_game(filename)
        if player_data:
            do_update_after_load_game(player_data)
            last_message = f'Loaded game {slot_number}.'
        else:
            last_message = f"Could not load '{filename}'. File is corrupt or does not exist."


def do_load_default_game():
    """
    Call's the dungeon's load_default_game() function and, if it was successful, updates the player and werewolf data.
    Updates last_message.
    """
    global last_message  # DO NOT REMOVE --- ALLOWS YOU TO ACCESS MEMBER VARIABLES DEFINED ABOVE
    player_data = dungeon.load_default_game()
    do_update_after_load_game(player_data)
    last_message = 'Loaded default game.'


def do_update_after_load_game(player_and_werewolf_data):
    """
    Takes the tuple of data and updates the player and werewolf.
    The data in the tuple is in the following order:
        player's x coordinate (int)
        player's y coordinate (int)
        player's looking direction (str, single character)
        player's inventory (dict)
        werewolf's x coordinate (int)
        werewolf's y coordinate (int)
        werewolf's health (int)
        werewolf's stun count (int)
    :param player_and_werewolf_data: tuple of values, see description above
    """
    # TODOish: Unpack the player_and_werewolf_data into local variables and replace all the None in this function.
    player.x = player_and_werewolf_data[0]
    player.y = player_and_werewolf_data[1]
    player.set_symbol(player_and_werewolf_data[2])
    player.inventory_set(player_and_werewolf_data[3])
    werewolf.x = player_and_werewolf_data[4]
    werewolf.y = player_and_werewolf_data[5]
    werewolf.health = player_and_werewolf_data[6]
    werewolf.stunned_count = player_and_werewolf_data[7]


def do_save_game():
    """
    Asks the user which game slot to save a game in.
    Call's the dungeon's save_game() function with player and werewolf data.
    Updates last_message.
    :return:
    """
    global last_message  # DO NOT REMOVE --- ALLOWS YOU TO ACCESS MEMBER VARIABLES DEFINED ABOVE
    screen.write("Enter a digit 0-9 to save game into that slot.\nEnter any other character to cancel.\nGame slot: ")
    slot_number = input()
    if len(slot_number) != 1 and not slot_number.isdigit():
        last_message = "Must enter 0-9 to save a game."
    else:
        filename = f'gameSlot{slot_number}.txt'
        success = dungeon.save_game(filename, player.x, player.y, player.get_symbol(), player.inventory, werewolf)
        # TODOish: Replace all the None on this line with the correct arguments.
        if success:
            last_message = f'Saved game {slot_number}.'
        else:
            last_message = f"Could not save '{filename}'. Data is corrupt or writing files is not allowed."


def do_show_help():
    """
    Displays the list of keyboard commands on the screen. Updates last_message.
    """
    global last_message  # DO NOT REMOVE --- ALLOWS YOU TO ACCESS MEMBER VARIABLES DEFINED ABOVE
    screen.clear_screen()
    screen.write('KEYBOARD COMMANDS\n')
    screen.write(f'   {KEYBOARD_UP}  Move up.\n')
    screen.write(f'   {KEYBOARD_DOWN}  Move down.\n')
    screen.write(f'   {KEYBOARD_LEFT}  Move left.\n')
    screen.write(f'   {KEYBOARD_RIGHT}  Move right.\n')
    screen.write(f'   {KEYBOARD_LOOK}  Look at the square immediately in front of you.\n')
    screen.write(f'   {KEYBOARD_TAKE}  Take object immediately in front of you.\n')
    screen.write(f'   {KEYBOARD_USE}  Use an item from your inventory.\n')
    screen.write(f'   {KEYBOARD_QUIT}  Quit the game.\n')
    screen.write(f'   {KEYBOARD_LOAD_GAME}  Load game from file.\n')
    screen.write(f'   {KEYBOARD_SAVE_GAME}  Save game to file.\n')
    screen.write(f'   {KEYBOARD_SHOW_HELP}  Show this help screen.\n')
    last_message = 'Scroll up to see a list of keyboard commands.'
