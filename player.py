"""
Group Members: # Dan To & Amelia Doe & H Grasso.
"""

# DO NOT CHANGE OR REMOVE THE FOLLOWING LINE
import dungeon
# DO NOT CHANGE OR REMOVE THE PRECEDING LINE


# CONSTANTS --- DO NOT CHANGE THESE VALUES ANYWHERE
import utilities

LOOKING_UP: str = '^'
LOOKING_DOWN: str = 'v'
LOOKING_LEFT: str = '<'
LOOKING_RIGHT: str = '>'
LOOKING_DEAD: str = 'X'
SLINGSHOT_DISTANCE: int = 4
SLINGSHOT_MAX_DAMAGE: int = 3


# MEMBER VARIABLES --- DO NOT CHANGE INITIAL VALUES, BUT YOU CAN ASSIGN NEW VALUES ELSEWHERE IN CODE
looking_direction: str = None
x: int = -1
y: int = -1
inventory: dict = {}
inventory_order: list = [
    dungeon.MAP_SQUARE_KEY,
    dungeon.MAP_SQUARE_ROPE,
    dungeon.MAP_SQUARE_PLANK,
    None,
    (dungeon.MAP_SQUARE_SLINGSHOT, dungeon.MAP_SQUARE_PEBBLE),
    None,
    None,
    None,
    dungeon.MAP_SQUARE_HEALTH,
] # This list just describes which inventory item to show on which row of the screen.


def get_looking_at_location(current_x: int, current_y: int, current_symbol: str) -> tuple:
    """
    Returns a (x, y) location tuple describing the square that is directly in front of location (current_x, current_y)
    where the direction being looked at is defined by current_symbol.
    :param current_x: int, horizontal index in the map
    :param current_y: int, vertical index in the map
    :param current_symbol: str, single character describing the direction of sight (up, down, left, right)
    :return: tuple of (x, y) location that is immediately adjacent to location (current_x, current_y)
    """
    if current_symbol == LOOKING_UP:
        return current_x, current_y - 1
    elif current_symbol == LOOKING_DOWN:
        return current_x, current_y + 1  # TODOish: replace the keyword pass with the correct return statement
    elif current_symbol == LOOKING_LEFT:
        return current_x - 1, current_y  # TODOish: replace the keyword pass with the correct return statement
    elif current_symbol == LOOKING_RIGHT:
        return current_x + 1, current_y   # TODOish: replace the keyword pass with the correct return statement
    return current_x, current_y

# correct left and right after run code


def do_player_hit(hit_points: int):
    """
    Process what happens when the player is hurt with hit_points worth of damage.
    :param hit_points: int, number of damage points done to the player
    """
    global inventory   # DO NOT REMOVE --- ALLOWS YOU TO ACCESS MEMBER VARIABLES DEFINED ABOVE
    health = inventory.get(dungeon.MAP_SQUARE_HEALTH, 0)
    health = health - hit_points
    if health > 0:
        inventory[dungeon.MAP_SQUARE_HEALTH] = health
    else:
        inventory[dungeon.MAP_SQUARE_HEALTH] = 0

    # TODOish: Get the player's health from their inventory.
    # TODOish: Decrease the player's health by hit_points point.
    # TODOish: The player's health cannot go below zero. Negative health is silly.
    # TODOish: Store the player's new health value in their inventory.

# def do_player_hit(hit_points: int):  # get help
#     """
#     Process what happens when the player is hurt with hit_points worth of damage.
#     :param hit_points: int, number of damage points done to the player
#     """
#     global inventory   # DO NOT REMOVE --- ALLOWS YOU TO ACCESS MEMBER VARIABLES DEFINED ABOVE
#     inventory.get(dungeon.MAP_SQUARE_HEALTH)
#     health = health - hit_points
#     if health > 0:
#         print(health)
#     else:
#         Print('Game Over: ')


def is_alive() -> bool:
    """
    Tells whether the player is alive, as defined by having health points (in the inventory!).
    :return: True if player has greater than zero health, or False if not
    """
    health = inventory.get(dungeon.MAP_SQUARE_HEALTH, 0)
    if health > 0:
        return True
    else:
        return False  # deleted players_health
      # TODOish: Replace False with the correct condition. See description.
 # return False


def get_symbol() -> str:
    # correct

    """
    Get the player's symbol, which is the looking_direction if the player is alive or LOOKING_DEAD if they are dead.
    :return: str, single character - looking_direction if the player is alive or LOOKING_DEAD if they are dead
    """
    global inventory
    if is_alive():
        return looking_direction
    else:
        return LOOKING_DEAD


def set_symbol(symbol: str):
    """
    Sets the looking_direction for the player.
    :param symbol: str, single character representing which way the player is facing (up, down, left, right)
    """
    global looking_direction   # DO NOT REMOVE --- ALLOWS YOU TO ACCESS MEMBER VARIABLES DEFINED ABOVE
    looking_direction = symbol


def is_open_space(location_x: int, location_y: int) -> bool: # get help
    """
    Tells whether location (x, y) is an open space for the player.
    An open space is a type of square that the player can walk over or through.
    The player can walk through empty squares, walk across set planks, and swing across tied ropes.
    :param location_x: int, horizontal index in map
    :param location_y: int, vertical index in map
    :return: bool, True if player can walk over or through the location (location_x, location_y)
    """
    space = dungeon.get_map_square(location_x, location_y)
    return space == dungeon.MAP_SQUARE_EMPTY or space == dungeon.MAP_SQUARE_PLANK_SET or \
           space == dungeon.MAP_SQUARE_ROPE_TIED
    # space_player_can_walk_through = dungeon.MAP_SQUARE_EMPTY, 'set_planks', 'tied_ropes')
    # if location_x == space_player_can_walk_through and location_y == space_player_can_walk_through):
    #     return True
    # space_player_can_walk_through = (dungeon.MAP_SQUARE_EMPTY, 'set_planks', 'tied_ropes')
    #     if len(space_player_can_walk_through) > 0:
    #         return True


def can_see_past(x: int, y: int) -> bool:
    """
    Tells whether location (x, y) contains a square that the player can see past (or see over).
    The player can see past (or see over) chasms, empty squares, a pebble, pebbles, free planks,
    set planks, free ropes, tied ropes, and slingshots.
    :param x: int, horizontal index in the map for the location in question
    :param y: int, vertical index in the map for the location in question
    :return: True if player can see past (or see over) location (x, y), or False if not
    """
    see_past = dungeon.get_map_square(x, y)
    return see_past == dungeon.MAP_SQUARE_CHASM or see_past == dungeon.MAP_SQUARE_EMPTY or \
            see_past == dungeon.MAP_SQUARE_PEBBLE or see_past == dungeon.MAP_SQUARE_PEBBLES or see_past == dungeon.MAP_SQUARE_PLANK\
            or see_past == dungeon.MAP_SQUARE_PLANK_SET or see_past == dungeon.MAP_SQUARE_ROPE or see_past == dungeon.MAP_SQUARE_ROPE_TIED\
            or see_past == dungeon.MAP_SQUARE_SLINGSHOT

    # TODOish: Return the correct value given the description.


def inventory_add(map_square: str):
    """
    Adds the item in map_square to the player's inventory.
    When adding a unit of health, a key, a pebble, a plank, or a rope --- just add 1 of that item.
    When adding pebbles (plural) --- add 2 to the pebble (singular) count in the inventory.
    When adding a slingshot --- the player can only have 1 slingshot, so set the value to 1.
    :param map_square: str, single character - representing an item on the map
    """
    item = convert_map_square_to_inventory_item(map_square)  # USE VALUE IN THIS VARIABLE item
    has_in_inv = inventory.get(item, 0)
    # The parameter map_square will tell you exactly what the user has picked up.
    # The variable item will tell you which item in the inventory map_square goes with.

    if map_square == dungeon.MAP_SQUARE_HEALTH or map_square == dungeon.MAP_SQUARE_KEY or \
            map_square == dungeon.MAP_SQUARE_PEBBLE or \
            map_square == dungeon.MAP_SQUARE_PLANK or map_square == dungeon.MAP_SQUARE_ROPE:
        inventory[item] = has_in_inv + 1
    if map_square is dungeon.MAP_SQUARE_PEBBLES:
        inventory[item] = has_in_inv + 2
    if map_square is dungeon.MAP_SQUARE_SLINGSHOT:
        inventory[item] = 1

    # TODOish: Update the count in the player's inventory for the value of item. See description.
    # for item in map_square:
    #     inventory[].append(item)
    #     inventory[].count(item)
    #     if item == ('unit_of_health', 'key', 'pebble', 'plank', 'rope'):
    #         print(item + 1)
    #     elif item == ('pebbles',):
    #         print(item + 2)
    #     elif item == 'slingshot':
    #         print(item)


def inventory_has(item: str) -> bool:  # get help
    """
    Tells whether the player has any of this item in inventory.
    :param item: str, single character
    :return: True if player has at least 1 of this item in inventory, or False if zero
    """
    global inventory   # DO NOT REMOVE --- ALLOWS YOU TO ACCESS MEMBER VARIABLES DEFINED ABOVE

    item_count = inventory.get(item, 0)
    return item_count > 0

    # for item in inventory:  ###expression expected
    #     if item.count[len(inventory)] > 0:
    #         return True

            # TODOish: Replace False with the correct condition. See description.
  #return False  # TODOish: Replace False with the correct condition. See description.


def inventory_use(item: str) -> bool: # correct
    """
    Uses an item from inventory, subtracting 1 from the count if appropriate.
    :param item: str, single character
    :return: True if player had at least 1 of that item, or False if zero
    """
    global inventory   # DO NOT REMOVE --- ALLOWS YOU TO ACCESS MEMBER VARIABLES DEFINED ABOVE
    count = inventory.get(item, 0)
    success = count > 0
    if success and item != dungeon.MAP_SQUARE_SLINGSHOT:
        inventory[item] = count - 1
    return success


def inventory_set(new_inventory: dict): # get help
    """
    This function causes the player's inventory to exactly match the content of new_inventory,
    with the caveat that the dictionary object assigned to inventory is still the same object
    it was before. This means you cannot use the assignment operator on the dictionary directly.
    :param new_inventory: dictionary with string keys and integer values
    """
    global inventory   # DO NOT REMOVE --- ALLOWS YOU TO ACCESS MEMBER VARIABLES DEFINED ABOVE
    # TODOish: See description.
    inventory.clear()
    inventory.update(new_inventory)




def convert_map_square_to_inventory_item(map_square: str) -> str:
    """
    Converts a map square into an item that can be stored in inventory.
    They mostly match, except that pebble (singular) and pebbles (plural) are counted together
    as just pebble (singular) in the inventory. Note that some map squares cannot be stored in inventory.
    :param map_square: str, single character representing item at that map square
    :return: str, single character of matching inventory item, or None if map_square cannot be stored
    """
    if map_square in [
        dungeon.MAP_SQUARE_HEALTH,
        dungeon.MAP_SQUARE_KEY,
        dungeon.MAP_SQUARE_PEBBLE,
        dungeon.MAP_SQUARE_PLANK,
        dungeon.MAP_SQUARE_ROPE,
        dungeon.MAP_SQUARE_SLINGSHOT,
    ]:
        return map_square
    elif map_square == dungeon.MAP_SQUARE_PEBBLES:
        return dungeon.MAP_SQUARE_PEBBLE
    else:
        return None


def draw_inventory_row(row: int, display_width: int) -> str:
    """
    Returns a string to display on screen for a particular row of the player's inventory display.
    :param row: int, which row to display (top row is 0)
    :param display_width: int, number of characters available for the display
    :return: str, text to display for that row of the inventory; must be display_width characters wide
    """
    global inventory, inventory_order  # DO NOT REMOVE --- ALLOWS YOU TO ACCESS MEMBER VARIABLES DEFINED ABOVE
    display_item = None
    row_item = inventory_order[row] if 0 <= row < len(inventory_order) else None
    if row_item is not None:
        if isinstance(row_item, str):
            display_item = row_item
            count = inventory.get(display_item, 0)
        elif isinstance(row_item, tuple):
            count = inventory.get(row_item[1], 0)
            if inventory_has(row_item[0]):
                display_item = row_item[0]
            elif count > 0:
                display_item = row_item[1]
    if display_item is not None and count > 0:
        extra_space_width = 1
        symbol_width = max(0, min(2, display_width))
        number_width = max(0, min(4, display_width - symbol_width))
        name_width = max(0, display_width - (number_width + symbol_width + extra_space_width))
        names = {
            dungeon.MAP_SQUARE_HEALTH: 'Health',
            dungeon.MAP_SQUARE_KEY: 'Key',
            dungeon.MAP_SQUARE_ROPE: 'Rope',
            dungeon.MAP_SQUARE_PLANK: 'Wood Plank',
            dungeon.MAP_SQUARE_SLINGSHOT: 'Slingshot',
            dungeon.MAP_SQUARE_PEBBLE: 'Pebble',
        }
        result = str(count).rjust(number_width) + ' ' + display_item.ljust(symbol_width) + names[display_item].ljust(name_width)
    else:
        result = ' ' * display_width
    return result


def is_looking_at(location_x: int, location_y: int) -> bool: # get help
    """
    Tells whether player is looking at and can see location (location_x, location_y).
    For this to be true:
        1. Player must be facing (location_x, location_y) directly on a row or column, NOT on a diagonal.
        2. Player must be able to see (location_x, location_y), meaning there are no visual obstacles in the way.
    :param location_x: int, horizontal index in map of location
    :param location_y: int, vertical index in map of location
    :return: bool, True if player is facing and can see (location_x, location_y), or False if not
    """
# below commented out to keep code running, please still grade:

    # get_looking_at_location(location_x, location_y, dungeon.get_map_square(location_x, location_y))
    # if (location_x, location_y) == "row" or (location_x, location_y) == "column":
    #     if can_see_past(is_open_space(
    #         get_looking_at_location(location_x, location_y, dungeon.get_map_square(location_x, location_y)):




    # TODOish: Return the correct value. See description. Use the value of symbol.



def get_farthest_actionable_location(max_action_distance: int, must_be_empty: bool) -> tuple: # get help
    """
    Given the criteria max_action_distance and must_be_empty (see param definitions), how far away can
    the player cause something to happen? For example, what is the farthest square in front of the player
    to which the player can throw an object? Or what is the farthest square in front of the player at
    which the player can cast a spell?
    It may be the case that the farthest square is where the player is standing; for example, if the player
    is adjacent to and facing a wall, then the player cannot act beyond the square on which they are standing.
    So, by default, if there are no squares farther away from the player that are eligible then this
    function will return the player's location as a tuple.
    CRITERIA FOR A SQUARE TO BE ELIGIBLE:
        1. The player must be able to see past (or see over) that square.
        2. The player must be looking at that square.
        3. The square must be within max_action_distance squares of the player's location.
        4. If must_be_empty is True, then the square must be empty to qualify. Ignore this if must_be_empty is False.
    There are MANY ways to implement this function, and I recommend you think about it from the player's perspective.
    :param max_action_distance: int, maximum distance from player that can be acted on (e.g. 2 squares away)
    :param must_be_empty: bool, True if the location has to be empty to be eligible, or False if it does not matter
    :return: tuple of (x, y) location that is the farthest location that the player can act on
    """
# below commented out to keep code running, please still grade:

 #    result_x, result_y = x, y
 #    farthest_empty_x, farthest_empty_y = x, y
    # for i in range(max_action_distance):
    #     if can_see_past() and is_looking_at():
    #         if utilities.manhattan_distance(x, y, column, row) <= max_action_distance:
    #             list = list.append()
    #         else:
    #             location_x == x or location_y == player.y
