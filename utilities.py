"""
Group Members: # H Grasso & Dan To & Amelia Doe.
"""


def sign(x: int) -> int:
    x = int(float(x))
    if x == 0:
        return 0
    if x > 0:
        return 1
    if x < 0:
        return -1

    """
    Returns 0, 1, or -1 to represent the sign of the number x.
    :param x: int or float, a number
    :return: int, 0 if x is 0, 1 if x is positive, or -1 if x is negative
    """
    # DONEish: Implement as described.


def manhattan_distance(from_x: int, from_y: int, to_x: int, to_y: int) -> int:
    """
    Returns the "Manhattan Distance" between two points:
    the difference in their x-coordinates plus the difference in their y-coordinates.
    This is the equivalent of picking two squares on a chessboard and
    counting the number of squares between them (without diagonals).
    :param from_x: x-coordinate of starting point
    :param from_y: y-coordinate of starting point
    :param to_x: x-coordinate of destination point
    :param to_y: y-coordinate of destination point
    :return: distance from (from_x, from_y) to (to_x, to_y)
    """
    return abs(to_x - from_x) + abs(to_y - from_y)
