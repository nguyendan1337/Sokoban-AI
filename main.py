import sokoban as sb
import numpy as np
import random
import BFS

# Moves
UP = "Up"
DOWN = "Down"
LEFT = "Left"
RIGHT = "Right"

# dictionary of q values
# state: box coordinates
# actions: UP, DOWN, LEFT, RIGHT
q_table = {}

# determine if any boxes are terminal states
def is_terminal_state(board, boxes):

    # for box in boxes:
    #     # if the reward for this box's location is -1, then it is a terminal state
    #     if rewards[box[0], box[1]] != -1.:
    #         return True

    #also check history
    #if we are in a repeated state, then we are in a terminal state, return TRUE
    #finish this last

    return False

# epsilon greedy algorithm that will choose which box and move to make
def get_next_action(boxes, epsilon):
    q_values = {}               #dictionary of boxes, their moves, and the moves' q_values that we will get from q_table
    q_move = {}                 #dictionary of boxes and their best moves
    q_max = {}                  #dictionary of boxes and their highest q values

    #if box is not in the q table, add it to the q table
    #get q values for this box from the q table
    for box in boxes.keys():
        if box not in q_table:
            q_table[box] = {
                UP      : 0,
                DOWN    : 0,
                LEFT    : 0,
                RIGHT   : 0
            }
        q_values[box] = q_table[box]

    # choose a random box and move
    box = random.choice(list(boxes.items()))
    move = random.choice(list(box[1].keys()))
    box_move = {box[0]: move}

    # if a randomly chosen value between 0 and 1 is less than epsilon,
    # then of the reachable boxes, choose box with the move with the highest q value
    # else return the random box and move
    if np.random.random() < epsilon:
        #for each box
        for box in q_values.keys():
            #get the box's move with the highest q value
            max_move = max(q_values[box], key=q_values[box].get)
            #save the q value of this box's move
            q_max[box] = q_values[box][max_move]
            #save this move for this box
            q_move[box] = max_move

        #get the box with the highest q value
        box = max(q_max, key=q_max.get)

        #if the max q value is not 0, return the box and its move
        #else return the random box and move
        if q_max[box] != 0:
            box_move = {box: q_move[box]}
            return box_move
        else:
            return box_move
    else:
        return box_move


#################
# MAIN FUNCTION #
#################
sokoban = sb.Sokoban("test/input/sokoban/sokoban01.txt")
sokoban.print()

# define training parameters
epsilon = 0.9  # the percentage of time when we should take the best action (instead of a random action)
discount_factor = 0.9  # discount factor for future rewards
learning_rate = 0.9  # the rate at which the AI agent should learn

# run through 1000 training episodes
for episode in range(1000):

    #initial game state
    agent = sokoban.agent_location
    board = sokoban.board
    boxes = sokoban.box_locations

    # continue moving boxes until we reach a terminal state
    while not is_terminal_state(board, boxes):
        # get a dictionary of reachable boxes, their available moves, and the path to those moves
        boxes = BFS.getReachableBoxes(board, agent)

        # choose which box and move to make
        action = get_next_action(boxes, epsilon)

        #perform the action
        #update agent and box locations
        #append path to history

