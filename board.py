import numpy as np
from constants import *


class Board:

    def __init__(self, filename):

        with open(filename, 'r') as f:

            read_data = f.read()
            self._lines = read_data.split("\n")

            self.corners = []
            self.num_cols = max(list(map(lambda x: len(self._lines[x]), range(len(self._lines)))))
            self.num_rows = len(self._lines)
            self.board = np.full((self.num_rows, self.num_cols), ' ', dtype=object)

            for row in range(self.num_rows):
                line = self._lines[row]
                for col, character in enumerate(line):
                    self.board[row][col] = character
                    if is_corner(row, col, self):
                        # self.board[row][col] = "X"
                        self.corners.append((row, col))
                    if character == '@':
                        self.agentRow = row
                        self.agentCol = col


# Initialize corners in the board
def is_corner(row, col, sokoban):
    if sokoban.board[row][col] is WALL:
        return False
    return is_upper_left_corner(row, col, sokoban) or \
           is_upper_right_corner(row, col, sokoban) or \
           is_bottom_left_corner(row, col, sokoban) or \
           is_bottom_right_corner(row, col, sokoban)


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
    if (row + 1 < sokoban.num_rows) and (col + 1 < sokoban.num_cols):
        return True if (sokoban.board[row + 1][col] is WALL and sokoban.board[row][col + 1] is WALL) else False
