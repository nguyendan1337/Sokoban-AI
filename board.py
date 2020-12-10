import numpy as np


class Board:
    _characters = {
        ' ': 0,  # free space
        '@': 1,  # player
        '#': 2,  # wall
        '$': 3,  # box
        '.': 4,  # goal
    }

    def __init__(self, filename):

        with open(filename, 'r') as f:

            read_data = f.read()
            self._lines = read_data.split("\n")

            self.width = max(list(map(lambda x: len(self._lines[x]), range(len(self._lines)))))
            self.height = len(self._lines)

            self.board = np.zeros((self.height, self.width), dtype=int)

            for i in range(len(self._lines)):
                line = self._lines[i]
                for j, character in enumerate(line):
                    self.board[i][j] = self._characters[character]
