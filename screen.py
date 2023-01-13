"""
Group Members: # H Grasso & Dan To & Amelia Doe.
"""

# DO NOT CHANGE OR REMOVE THE FOLLOWING LINES
import dungeon
import player
import werewolf
# DO NOT CHANGE OR REMOVE THE PRECEDING LINES


# CONSTANTS --- DO NOT CHANGE THESE VALUES ANYWHERE
SCREEN_MAP_RADIUS = 3
SCREEN_MAP_WIDTH_HEIGHT = SCREEN_MAP_RADIUS * 2 + 1
SCREEN_INVENTORY_WIDTH = 22


def write(text: str):
    """
    Display text on the screen. Does not start a new line.
    :param text: str, text to display
    """
    print(text, end='')


def write_multiple_times(string: str, times: int):
    """
    Write the given text the given number of times.
    :param string: str, text to repeat
    :param times: int, number of times to repeat the text string
    """
    write(string * times)


def write_new_line():
    """
    For the purpose of displaying text on the screen, start a new line.
    """
    print()


def clear_screen():
    """
    Displays 10 new lines on the screen.
    """
    for i in range(10):
        write_new_line()


def draw_screen(last_message: str):
    """
    Displays onto the screen the dungeon map, player inventory, and messages to the user.
    :param last_message: str, message to display to the user
    """
    FRAME_TOP_CORNER: str = ','
    FRAME_BOTTOM_CORNER: str = '\''
    FRAME_SIDE_HORIZONTAL: str = '-'
    FRAME_SIDE_VERTICAL: str = '|'

    # Draw top of frame.
    write(FRAME_TOP_CORNER)
    write_multiple_times(FRAME_SIDE_HORIZONTAL, SCREEN_MAP_WIDTH_HEIGHT)
    write(FRAME_TOP_CORNER)
    write_multiple_times(FRAME_SIDE_HORIZONTAL, SCREEN_INVENTORY_WIDTH)
    write(FRAME_TOP_CORNER)
    write_new_line()

    # Draw frame, map, and inventory.
    for row in range(SCREEN_MAP_WIDTH_HEIGHT):
        write(FRAME_SIDE_VERTICAL)
        write(dungeon.draw_map_row(player.x, player.y, row, SCREEN_MAP_RADIUS, player.get_symbol(), werewolf))
        write(FRAME_SIDE_VERTICAL)
        write(player.draw_inventory_row(row, SCREEN_INVENTORY_WIDTH))
        write(FRAME_SIDE_VERTICAL)
        write_new_line()

    # Draw bottom of frame.
    write(FRAME_BOTTOM_CORNER)
    write_multiple_times(FRAME_SIDE_HORIZONTAL, SCREEN_MAP_WIDTH_HEIGHT)
    write(FRAME_BOTTOM_CORNER)
    write_multiple_times(FRAME_SIDE_HORIZONTAL, SCREEN_INVENTORY_WIDTH)
    write(FRAME_BOTTOM_CORNER)
    write_new_line()

    # Show text below frame.
    write_new_line()
    write(last_message)
    write_new_line()
    write_new_line()
    write(f'You are at ({player.x}, {player.y}). ')
