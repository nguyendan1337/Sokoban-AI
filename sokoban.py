from pathlib import Path

import numpy as np

from helper import *


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


#
# Factory pattern, given a path to file and a specified mode, will use proper board initializing protocols via the child class
#
class Sokoban:

    def __init__(self):
        # Member variables, initialized in child classes
        self.num_cols = 0
        self.num_rows = 0
        self.board = None
        self.agent = None
        self.goals = []
        self.boxes = []
        self.corners = []

    def build(self, path_to_file, mode):
        if mode == "visual":
            return Visual(path_to_file)
        if mode == "kask":
            return Kask(path_to_file)

    # Print no colors in Dan-sanctioned format
    def print(self):
        translation = {39: None}
        np.set_printoptions(edgeitems=30, linewidth=100000, formatter=dict(float=lambda x: "%.3g" % x))
        print(str(self.board).translate(translation))

    # Print with colors in Dan-sanctioned format
    # Optionally, pass in the most recently moved box coordinates to have it highlight green.
    def pprint(self, action=None):
        # if action is not None:
        #     print(action)

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if action == (row, col):
                    print(Color.GREEN + self.board[row][col] + Color.END, end=' ')
                else:
                    if self.board[row][col] is AGENT:
                        print(Color.PURPLE + AGENT + Color.END, end=' ')
                    elif self.board[row][col] is BOX_ON_GOAL:
                        print(Color.BLUE + BOX_ON_GOAL + Color.END, end=' ')
                    elif self.board[row][col] is BOX:
                        print(Color.YELLOW + BOX + Color.END, end=' ')
                    elif self.board[row][col] is GOAL:
                        print(Color.CYAN + GOAL + Color.END, end=' ')
                    elif self.board[row][col] is WALL:
                        print(Color.BOLD + WALL + Color.END, end=' ')
                    else:
                        print(self.board[row][col], end=' ')
            print()


#
# Processes the Kask-format input file and initializes the corresponding components of the Sokoban board.
#
class Kask(Sokoban):

    # Initialization of the board requires the path to the sokoban__.txt file
    def __init__(self, path_to_file):

        file = open(path_to_file)

        # Each line of the file is an element in the list
        file_contents = file.readlines()
        lines = list(map(lambda x: x.replace('\n', '').split(' '), file_contents))

        # List is converted to numpy array of integers for ease of extracting data
        data = np.array([np.array(x, dtype=np.int8) for x in lines], dtype=object)

        # Member variables
        self.num_cols = data[BOARD_DIMENSIONS_LINE][0]
        self.num_rows = data[BOARD_DIMENSIONS_LINE][1]
        self.board = np.full((self.num_rows, self.num_cols), SPACE, dtype=object)
        self.agent = ()
        self.goals = []
        self.boxes = []
        self.corners = []

        # Decrement each element by one once constants have been extracted for proper array indexing
        data = data - 1

        # Get the coordinates of the walls, boxes, goals, and agent and set appropriately in the 2D string list
        self.init_wall_squares(data[WALL_SQUARES_LINE][1:])
        self.init_goals(data[GOALS_LINE][1:])
        self.init_boxes(data[BOXES_LINE][1:])
        self.init_agent(data[AGENT_LINE])
        self.init_corners()

        file.close()

    # Number of wall squares is the first number on the second line
    def init_wall_squares(self, line):
        for i in range(0, len(line), 2):
            row = line[i]
            col = line[i + 1]
            self.board[row][col] = WALL

    def init_goals(self, line):
        for i in range(0, len(line), 2):
            row = line[i]
            col = line[i + 1]
            self.board[row][col] = GOAL
            self.goals.append((row, col))

    def init_boxes(self, line):
        for i in range(0, len(line), 2):
            row = line[i]
            col = line[i + 1]
            if self.board[row][col] is GOAL:
                self.board[row][col] = BOX_ON_GOAL
            else:
                self.board[row][col] = BOX
            self.boxes.append((row, col))

    # Agent coordinates (x,y) are the first and second elements on the fifth line
    def init_agent(self, line):
        row = line[0]
        col = line[1]
        self.board[row][col] = AGENT
        self.agent = (row, col)

    def init_corners(self):
        # Initialize corners
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if is_corner(row, col, self.board):
                    self.corners.append((row, col))

    # Outputs the board in the same format as Kask ~ for testing purposes
    def output_board_to_file(self, path_to_directory):
        p = Path(path_to_directory)
        if not p.exists():
            p.touch()
        file = p.open(mode='w')
        line = ''

        for x in self.board:
            for y in x:
                line += y
            file.write(line)
            line = '\n'

        file.close()
        return p


#
# Converts the visual/ASCII representation of the board
#
class Visual(Sokoban):

    def __init__(self, path_to_file):

        with open(path_to_file, 'r') as f:

            read_data = f.read()
            _lines = read_data.split("\n")

            # Member variables
            self.num_cols = max(list(map(lambda x: len(_lines[x]), range(len(_lines)))))
            self.num_rows = len(_lines)
            self.board = np.full((self.num_rows, self.num_cols), SPACE, dtype=object)
            self.agent = ()
            self.goals = []
            self.boxes = []
            self.corners = []

            # Initialize characters of board
            for row in range(self.num_rows):
                line = _lines[row]
                for col, character in enumerate(line):
                    self.board[row][col] = character
                    if character is AGENT:
                        self.agent = (row, col)
                    elif character is GOAL:
                        self.goals.append((row, col))
                    elif character is BOX:
                        self.boxes.append((row, col))
                    elif character is BOX_ON_GOAL:
                        self.boxes.append((row, col))
                        self.goals.append((row, col))

            # Initialize corners
            for row in range(self.num_rows):
                line = _lines[row]
                for col, character in enumerate(line):
                    if is_corner(row, col, self.board):
                        self.corners.append((row, col))
