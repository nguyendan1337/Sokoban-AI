import numpy as np
from constants import *


# Takes a board as input to process, returns a board (numpy array) of equivalent size with reward values in the coordinates
def preprocess(sokoban):
    # Initialize all coordinates to the default reward value
    rewards = np.full((sokoban.num_rows, sokoban.num_cols), DEFAULT_REWARD, dtype=int)

    for row in range(sokoban.num_rows):
        for col in range(sokoban.num_cols):
            # Initialize reward for goals first, since it could also be a corner.
            if (row, col) in sokoban.goals:
                rewards[row][col] = GOAL_REWARD
            elif (row, col) in sokoban.corners:
                rewards[row][col] = CORNER_REWARD

    return rewards
