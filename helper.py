from constants import *


# Static helper functions that can be accessed elsewhere in the program.

# Initialize corners in the board
def is_corner(row, col, sokoban):
    if sokoban.board[row][col] is WALL:
        return False
    return is_upper_right_corner(row, col, sokoban) or is_upper_left_corner(row, col, sokoban) or is_bottom_left_corner(
        row, col, sokoban) or is_bottom_right_corner(row, col, sokoban)


def is_upper_left_corner(row, col, sokoban):
    if row - 1 >= 0 and col - 1 >= 0:
        return True if (sokoban.board[row - 1][col] is WALL and sokoban.board[row][col - 1] is WALL) else False


def is_upper_right_corner(row, col, sokoban):
    if row - 1 >= 0 and col + 1 < sokoban.num_cols:
        return True if (sokoban.board[row - 1][col] is WALL and sokoban.board[row][col + 1] is WALL) else False


def is_bottom_left_corner(row, col, sokoban):
    if row + 1 < sokoban.num_rows and col - 1 >= 0:
        return True if (sokoban.board[row + 1][col] is WALL and sokoban.board[row][col - 1] is WALL) else False


def is_bottom_right_corner(row, col, sokoban):
    if row + 1 < sokoban.num_rows and col + 1 < sokoban.num_cols:
        return True if (sokoban.board[row + 1][col] is WALL and sokoban.board[row][col + 1] is WALL) else False
