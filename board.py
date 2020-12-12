import numpy as np


class Board:

    def __init__(self, filename):

        with open(filename, 'r') as f:

            read_data = f.read()
            self._lines = read_data.split("\n")

            self.width = max(list(map(lambda x: len(self._lines[x]), range(len(self._lines)))))
            self.height = len(self._lines)

            self.board = np.full((self.height, self.width), '', dtype=object)

            for row in range(len(self._lines)):
                line = self._lines[row]
                for col, character in enumerate(line):
                    self.board[row][col] = character
                    if character == '@':
                        self.agent = (row, col)
