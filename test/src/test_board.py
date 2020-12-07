from unittest import TestCase

from board import Board


# TODO: parameterized with different levels, something like this: https://stackoverflow.com/questions/32899/how-do-you-generate-dynamic-parameterized-unit-tests-in-python
# https://docs.python.org/3/library/unittest.html
class TestBoard(TestCase):

    def setUp(self):
        self.board = Board('/Users/brookeryan/PycharmProjects/CS271/test/input/levels/level1.txt')
        self.height = 11
        self.width = 19
        self.dimensions = (self.height, self.width)

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

    # TODO: failing - array index out of bounds
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

        with open('/Users/brookeryan/PycharmProjects/CS271/test/input/levels/level1.txt') as f:
            for i, line in enumerate(f):
                for j, character in enumerate(line):
                    print("[i,j]=", i, j)
                    print("array[i,j]=", arr[i, j])

        for x in arr:
            for y in x:
                print(y)
