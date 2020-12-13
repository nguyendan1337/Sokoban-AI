import numpy as np
from helper import *


class Board:

    def __init__(self, filename):

        with open(filename, 'r') as f:

            read_data = f.read()
            self._lines = read_data.split("\n")

            self.num_cols = max(list(map(lambda x: len(self._lines[x]), range(len(self._lines)))))
            self.num_rows = len(self._lines)
            self.board = np.full((self.num_rows, self.num_cols), ' ', dtype=object)
            self.goals = []

            for row in range(self.num_rows):
                line = self._lines[row]
                for col, character in enumerate(line):
                    self.board[row][col] = character
                    if character is AGENT:
                        self.agent = (row, col)
                    elif character is GOAL:
                        self.goals.append((row, col))

            self.corners = self.init_corners()

    def init_corners(self):
        corners = []

        for row in range(self.num_rows):
            line = self._lines[row]
            for col, character in enumerate(line):
                if is_corner(row, col, self.board):
                    corners.append((row, col))

        return corners
