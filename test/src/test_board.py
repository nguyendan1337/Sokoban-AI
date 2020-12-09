from unittest import TestCase
from parameterized import parameterized_class
from board import Board


@parameterized_class(('file', 'dimensions'), [
    ("/Users/brookeryan/PycharmProjects/CS271/test/input/levels/level0.txt", (3, 14)),
    ("/Users/brookeryan/PycharmProjects/CS271/test/input/levels/level1.txt", (11, 19)),
    ("/Users/brookeryan/PycharmProjects/CS271/test/input/levels/level2.txt", (10, 14)),
    ("/Users/brookeryan/PycharmProjects/CS271/test/input/levels/level47.txt", (17, 31))
])
class TestBoard(TestCase):

    def setUp(self):
        self.board = Board(self.file)
        self.height = self.dimensions[0]
        self.width = self.dimensions[1]

    # Simply checks to make sure the board and its attributes are set
    def test_board_not_None(self):
        self.assertIsNotNone(self.board)
        self.assertIsNotNone(self.board.__getattribute__('height'))
        self.assertIsNotNone(self.board.__getattribute__('width'))
        self.assertIsNotNone(self.board.__getattribute__('board'))

    # Tests that the dimensions of the generated board are correct
    def test_dimensions(self):
        self.assertEqual(self.height, self.board.__getattribute__('height'))
        self.assertEqual(self.width, self.board.__getattribute__('width'))

        arr = self.board.__getattribute__('board')
        self.assertEqual(self.dimensions, arr.shape)

    # Tests that the individual characters in the board are translated correctly
    def test_translation(self):
        _characters = {
            ' ': 0,  # free space
            '@': 1,  # player
            '#': 2,  # wall
            '$': 3,  # box
            '.': 4,  # goal
        }
        arr = self.board.__getattribute__('board')
        with open(self.file) as f:
            read_data = f.read()
            self._lines = read_data.split("\n")

            for i in range(self.height):
                line = self._lines[i]
                for j, string in enumerate(line):
                    textFileCharacterAtCoordinate = line[j]
                    boardValueAtCoordinate = arr[i, j]
                    self.assertEqual(arr[i, j], _characters[line[j]],
                                     "At coordinate [{i}, {j}]: board = {v}.  text file = {x}. \n{board}\n{text}".format(
                                         i=i, j=j, v=boardValueAtCoordinate, x=textFileCharacterAtCoordinate, board=arr,
                                         text=line))
