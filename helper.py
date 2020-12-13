from constants import *


# Static helper functions that can be accessed elsewhere in the program.

# Takes row, col, and a numpy array
def is_corner(row, col, arr):
    if arr[row][col] is WALL:
        return False
    return is_upper_right_corner(row, col, arr) or is_upper_left_corner(row, col, arr) or is_bottom_left_corner(
        row, col, arr) or is_bottom_right_corner(row, col, arr)


def is_upper_left_corner(row, col, arr):
    if row - 1 >= 0 and col - 1 >= 0:
        return True if (arr[row - 1][col] is WALL and arr[row][col - 1] is WALL) else False


def is_upper_right_corner(row, col, arr):
    num_cols = arr.shape[1]
    if row - 1 >= 0 and col + 1 < num_cols:
        return True if (arr[row - 1][col] is WALL and arr[row][col + 1] is WALL) else False


def is_bottom_left_corner(row, col, arr):
    num_rows = arr.shape[0]
    if row + 1 < num_rows and col - 1 >= 0:
        return True if (arr[row + 1][col] is WALL and arr[row][col - 1] is WALL) else False


def is_bottom_right_corner(row, col, arr):
    num_rows = arr.shape[0]
    num_cols = arr.shape[1]
    if row + 1 < num_rows and col + 1 < num_cols:
        return True if (arr[row + 1][col] is WALL and arr[row][col + 1] is WALL) else False
