"""
Group Members: # Dan To & Amelia Doe & H Grasso.
"""

# DO NOT CHANGE OR REMOVE THE FOLLOWING LINE
import random
import dungeon
import utilities

# DO NOT CHANGE OR REMOVE THE PRECEDING LINE


# CONSTANTS --- DO NOT CHANGE THESE VALUES ANYWHERE
WEREWOLF_SYMBOL_NORMAL: str = 'W'
WEREWOLF_SYMBOL_STUNNED: str = 'w'
WEREWOLF_SYMBOL_DEAD: str = 'm'
WEREWOLF_MAX_DAMAGE: int = 5
WEREWOLF_POST_ATTACK_MIN_TELEPORT_DISTANCE: int = 6
WEREWOLF_PICTURE_WIDTH: int = 36
WEREWOLF_PICTURE_HEIGHT: int = 12

# MEMBER VARIABLES --- DO NOT CHANGE INITIAL VALUES, BUT YOU CAN ASSIGN NEW VALUES ELSEWHERE IN CODE
x: int = -1
y: int = -1
health: int = 0
stunned_count: int = 0
skip_turn: bool = False


def is_alive() -> bool:
    """
    Tells whether the werewolf is alive.
    :return: bool, True if health is greater than zero, or False if not
    """
    return health > 0
     # TODOish: Replace False with the necessary condition. See description.


def is_stunned() -> bool:
    return stunned_count > 0

    # """
    # Tells whether werewolf is stunned.
    # :return: bool, True if stunned_count is greater than zero, or False if not
    # """
    # return False  # TODOish: Replace False with the necessary condition. See description.


def get_symbol() -> str:
    if not is_alive():
        return WEREWOLF_SYMBOL_DEAD
    elif is_alive() and is_stunned():
        return WEREWOLF_SYMBOL_STUNNED
    elif is_alive() and not is_stunned():
        return WEREWOLF_SYMBOL_NORMAL
    """
    Returns the symbol that should be used to represent the werewolf's physical state.
    If the werewolf is dead, returns WEREWOLF_SYMBOL_DEAD.
    If the werewolf is alive and stunned, returns WEREWOLF_SYMBOL_STUNNED.
    If the werewolf is alive and not stunned, returns WEREWOLF_SYMBOL_NORMAL.
    :return: str, single character representing werewolf's physical state
    """
    # TODOish: Return the correct value. See description.


def do_hit(points_of_damage: int) -> int:
    """
    Applies damage to werewolf's health, increases stun count, and returns the health value.
    :param points_of_damage: int, points of damage to remove from health
    :return: int, health after damage is applied
    """
    global stunned_count, health

    health = health - points_of_damage
    stunned_count = stunned_count + 2
    if health < 0:
        health = 0
    return health

    # get help
    # TODOish: Decrease the werewolf's health by points_of_damage.
    # TODOish: Make sure the werewolf's health is not below 0. Negative health is a silly idea.
    # TODOish: Increase the stun count by 2.
    # TODOish: Return the value of the werewolf's health.


def _flip_boolean_coin() -> bool:
    """Randomly returns either True or False."""
    flip = random.getrandbits(1)
    coin = bool(flip)
    return coin
    # TODOish: Replace the keyword pass with code that randomly returns True or False with equal probability


def do_next_move(player_x: int, player_y: int):
    """
    Perform the werewolf's next move.
    :param player_x: int, x coordinate of where the werewolf thinks the player is
    :param player_y: int, y coordinate of where the werewolf thinks the player is
    """
    global x, y, stunned_count, skip_turn  # DO NOT REMOVE --- ALLOWS YOU TO ACCESS MEMBER VARIABLES DEFINED ABOVE
    if health <= 0:
        return
    if skip_turn:
        skip_turn = False
        return
    if is_stunned():
        stunned_count = stunned_count - 1
        return

    # TODOish: If the werewolf is dead, exit this function.
    # TODO: If we should skip the werewolf's turn, set skip to False and exit this function.
    # TODOish: If werewolf is stunned, decrease the stun count by 1 and exit this function.

    delta_x = player_x - x  # distance from werewolf to player in X direction
    delta_y = player_y - y  # distance from werewolf to player in Y direction

    possible_next_x = x + utilities.sign(delta_x)  # one square closer to player in X direction
    possible_next_y = y + utilities.sign(delta_y)  # one square closer to player in Y direction

    is_x_direction_move_possible = delta_x != 0 and is_open_space(possible_next_x, y)
    is_y_direction_move_possible = delta_y != 0 and is_open_space(x, possible_next_y)

    if is_x_direction_move_possible and not is_y_direction_move_possible:
        x = possible_next_x  # If werewolf can only move horizontally, then do so.
    elif not is_x_direction_move_possible and is_y_direction_move_possible:
        y = possible_next_y  # If werewolf can only move vertically, then do so.
    elif is_x_direction_move_possible and is_y_direction_move_possible:
        if abs(delta_x) > abs(delta_y):
            x = possible_next_x
            # If werewolf can move in both directions but is closer horizontally, move horizontally.
        elif abs(delta_x) < abs(delta_y):
            y = possible_next_y  # If werewolf can move in both directions but is closer vertically, move vertically.
        else:
            # If werewolf can move in both directions and is equally close to the player horizontally and vertically,
            # randomly pick whether to move horizontally or vertically.
            randomly_pick_x = _flip_boolean_coin()
            if randomly_pick_x:
                x = possible_next_x
            else:
                y = possible_next_y


def is_open_space(possible_x: int, possible_y: int) -> bool:
    """
    Tells whether the map square at location (possible_x, possible_y) is an open space for the werewolf.
    An open space is a type of square that the werewolf can walk over or through.
    The werewolf can walk through empty squares, step on a key, step on a pebble, step on multiple pebbles,
    walk on a free plank, walk across set planks, and step on free rope.
    :param possible_x: int, horizontal index in map
    :param possible_y: int, vertical index in map
    :return: bool, True if werewolf can walk over or through this location, or False otherwise
    """
    items = [dungeon.MAP_SQUARE_EMPTY, dungeon.MAP_SQUARE_KEY, dungeon.MAP_SQUARE_PEBBLE, dungeon.MAP_SQUARE_PEBBLES,
             dungeon.MAP_SQUARE_PLANK, dungeon.MAP_SQUARE_PLANK_SET, dungeon.MAP_SQUARE_ROPE]
    return dungeon.get_map_square(possible_x, possible_y) in items
    # # if dungeon.get_map_square(possible_x, possible_y) == items:
    # for n in items:
    #     if dungeon.get_map_square(possible_x, possible_y) == n:
    #         return True
    #     else:
    #         return False
    # if possible_x == items and possible_y == items:  # run through list, .find . count
    # if dungeon.get_map_square(possible_x, possible_y) == dungeon.MAP_SQUARE_EMPTY:
    #     return True
    # else:
    #     for range can_walk: #I renamed the items -> can_walk in my code for now
    #         n = 0
    #         if dungeon.get_map_square(possible_x, possible_y) == can_walk[n]:
    #             return True
    #         break
    #     else:
    #             n += 1
    #             continue
    #         return False

    # TODOish: Return the correct value based on the description.
