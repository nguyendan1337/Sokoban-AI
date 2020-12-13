import numpy as np
from helper import *


class Board:

    def __init__(self, filename):

        with open(filename, 'r') as f:

            read_data = f.read()
            self._lines = read_data.split("\n")

            self.num_cols = max(list(map(lambda x: len(self._lines[x]), range(len(self._lines)))))
            self.num_rows = len(self._lines)
            self.board = np.full((self.num_rows, self.num_cols), SPACE, dtype=object)
            self.goals = []
            self.boxes = []

            for row in range(self.num_rows):
                line = self._lines[row]
                for col, character in enumerate(line):
                    self.board[row][col] = character
                    if character is AGENT:
                        self.agent = (row, col)
                    elif character is GOAL:
                        self.goals.append((row, col))
                    elif character is BOX:
                        self.boxes.append((row, col))

            self.corners = self.init_corners()

    def init_corners(self):
        corners = []

        for row in range(self.num_rows):
            line = self._lines[row]
            for col, character in enumerate(line):
                if is_corner(row, col, self.board):
                    corners.append((row, col))

        return corners

    # Pretty print in Dan-sanctioned format
    def print(self):
        translation = {39: None}
        np.set_printoptions(edgeitems=30, linewidth=100000, formatter=dict(float=lambda x: "%.3g" % x))
        print(str(self.board).translate(translation))
