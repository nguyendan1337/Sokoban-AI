from unittest import TestCase
from parameterized import *
from board import Board
import numpy as np
from preprocess import *
from helper import *


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
        translation = {39: None}
        np.set_printoptions(edgeitems=30, linewidth=100000, formatter=dict(float=lambda x: "%.3g" % x))
        print(str(self.board.board).translate(translation))

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
            ' ': SPACE,  # free space
            '@': AGENT,  # player
            '#': WALL,  # wall
            '$': BOX,  # box
            '.': GOAL  # goal
        }
        arr = self.board.board

        with open(self.file) as f:
            read_data = f.read()
            self._lines = read_data.split("\n")

            for i in range(self.num_rows):
                line = self._lines[i]
                for j, string in enumerate(line):
                    text_file_character_at_coordinate = line[j]
                    board_value_at_coordinate = arr[i, j]
                    self.assertEqual(arr[i, j], _characters[line[j]],
                                     "At coordinate [{i}, {j}]: board = {v}.  text file = {x}. \n{board}\n{text}".format(
                                         i=i, j=j, v=board_value_at_coordinate, x=text_file_character_at_coordinate,
                                         board=arr,
                                         text=line))

    # TODO: Add some meaningful tests for corner detection.
    def test_corners(self):
        print("corners = ", self.board.corners)

    # TODO: Add some meaningful tests for goal detection.
    def test_goals(self):
        print("goals = ", self.board.goals)

    def test_preprocess(self):
        rewards = preprocess(self.board)
        print(rewards)

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if (i, j) in self.board.goals:
                    self.assertEqual(GOAL_REWARD, rewards[i][j])
                elif (i, j) in self.board.corners:
                    self.assertEqual(CORNER_REWARD, rewards[i][j])
                elif self.board.board[i][j] is WALL:
                    self.assertEqual(WALL_REWARD, rewards[i][j])
                else:
                    self.assertEqual(DEFAULT_REWARD, rewards[i][j])
