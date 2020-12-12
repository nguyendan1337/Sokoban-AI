from unittest import TestCase
from parameterized import *
from board import Board
import numpy as np


# The board.py file gives the "intuitive" height and width where h and w are at least 1
@parameterized_class(('file', 'dimensions'), [
    ("/Users/brookeryan/PycharmProjects/CS271/test/input/levels/level0.txt", (3, 14)),
    ("/Users/brookeryan/PycharmProjects/CS271/test/input/levels/level1.txt", (11, 19)),
    ("/Users/brookeryan/PycharmProjects/CS271/test/input/levels/level2.txt", (10, 14)),
    ("/Users/brookeryan/PycharmProjects/CS271/test/input/levels/level47.txt", (17, 31))
])
class TestBoard(TestCase):

    def setUp(self):
        self.board = Board(self.file)
        self.num_rows = self.dimensions[0]
        self.num_cols = self.dimensions[1]

    def test_print_board(self):
        np.set_printoptions(edgeitems=30, linewidth=100000, formatter=dict(float=lambda x: "%.3g" % x))
        print(self.board.board)
        print(self.board.corners)

    # Simply checks to make sure the board and its attributes are set
    def test_board_not_None(self):
        self.assertIsNotNone(self.board)
        self.assertIsNotNone(self.board.__getattribute__('num_rows'))
        self.assertIsNotNone(self.board.__getattribute__('num_cols'))
        self.assertIsNotNone(self.board.__getattribute__('board'))

    # Tests that the dimensions of the generated board are correct
    def test_dimensions(self):
        self.assertEqual(self.num_rows, self.board.__getattribute__('num_rows'))
        self.assertEqual(self.num_cols, self.board.__getattribute__('num_cols'))

        arr = self.board.__getattribute__('board')
        self.assertEqual(self.dimensions, arr.shape)

    # Tests that the individual characters in the board are translated correctly
    def test_translation(self):
        _characters = {
            ' ': ' ',  # free space
            '@': "@",  # player
            '#': '#',  # wall
            '$': '$',  # box
            '.': '.',  # goal
            '_': '_'  # corner
        }
        arr = self.board.__getattribute__('board')
        with open(self.file) as f:
            read_data = f.read()
            self._lines = read_data.split("\n")

            for i in range(self.num_rows):
                line = self._lines[i]
                for j, string in enumerate(line):
                    textFileCharacterAtCoordinate = line[j]
                    boardValueAtCoordinate = arr[i, j]
                    self.assertEqual(arr[i, j], _characters[line[j]],
                                     "At coordinate [{i}, {j}]: board = {v}.  text file = {x}. \n{board}\n{text}".format(
                                         i=i, j=j, v=boardValueAtCoordinate, x=textFileCharacterAtCoordinate, board=arr,
                                         text=line))
