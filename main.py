from preprocess import *
from board import *
from BFS import *
from Q import *


# dictionary of q values
# state: box coordinates
# actions: UP, DOWN, LEFT, RIGHT
q_table = {}


#################
# MAIN FUNCTION #
#################
game = Board("test/input/levels/level1.txt")
game.print()
rewards = preprocess(game)

# define training parameters
epsilon = 0.9  # the percentage of time when we should take the best action (instead of a random action)
discount_factor = 0.9  # discount factor for future rewards
learning_rate = 0.9  # the rate at which the AI agent should learn
r = 1

# run through 1000 training episodes
for episode in range(r):

    #initial game state
    agent = game.agent
    board = game.board
    boxes = game.boxes
    terminal = False

    # continue moving boxes until we reach a terminal state
    while not terminal:
        # get a dictionary of reachable boxes, their available moves, and the path to those moves
        reachable_boxes = get_reachable_boxes(board, agent)

        # choose which box and move to make
        action = get_next_action(reachable_boxes, epsilon, q_table)

        #perform the action
        #update agent and box locations
        #append path to history

        #update Q values in Q Table
        q_table = update_q_table(q_table, rewards, new_box_position, action, discount_factor, learning_rate)

        terminal, status = is_terminal_state(board, boxes)

    print(status)

