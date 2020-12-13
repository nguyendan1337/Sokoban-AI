import BFS
import Q
from board import *
from preprocess import *

# Moves
UP = "Up"
DOWN = "Down"
LEFT = "Left"
RIGHT = "Right"

# dictionary of q values
# state: box coordinates
# actions: UP, DOWN, LEFT, RIGHT
q_table = {}


#################
# MAIN FUNCTION #
#################
sokoban = Board("test/input/levels/level1.txt")
sokoban.print()
rewards = preprocess(sokoban)

# define training parameters
epsilon = 0.9  # the percentage of time when we should take the best action (instead of a random action)
discount_factor = 0.9  # discount factor for future rewards
learning_rate = 0.9  # the rate at which the AI agent should learn
r = 1

# run through 1000 training episodes
for episode in range(r):

    #initial game state
    agent = sokoban.agent
    board = sokoban.board
    boxes = sokoban.boxes
    terminal = False

    # continue moving boxes until we reach a terminal state
    while not terminal:
        # get a dictionary of reachable boxes, their available moves, and the path to those moves
        reachable_boxes = BFS.get_reachable_boxes(board, agent)

        # choose which box and move to make
        action = Q.get_next_action(reachable_boxes, epsilon, q_table)

        #perform the action
        #update agent and box locations
        #append path to history
        #board_boxes

        #update Q values in Q Table
        # q_table = Q.update_q_table(q_table, rewards)

        # terminal = Q.is_terminal_state(board, boxes)

