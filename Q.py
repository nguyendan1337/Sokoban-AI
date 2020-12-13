import random
import numpy as np

# States
DEAD = "Dead"
ALIVE = "Alive"
GOAL = "Goal"

# Moves
UP = "Up"
DOWN = "Down"
LEFT = "Left"
RIGHT = "Right"

# determine if any boxes are terminal states
def is_terminal_state(boxes, rewards):

    #if all boxes are in goals, terminal will remain true
    #box_coordinates[0] = the box's row
    #box_coordinates[1] = the box's column
    for box_coordinates in boxes:
        # if the reward for this box's location is -100, then it is in a corner terminal state
        if rewards[box_coordinates[0], box_coordinates[1]] == -100:
            return True, DEAD
        # if the box is not at a goal, then it is not in a terminal state
        if rewards[box_coordinates[0], box_coordinates[1]] == -1:
            return False, ALIVE

    #also check history
    #if we are in a repeated state, then we are in a terminal state, return TRUE
    #finish this last

    return True, GOAL

# epsilon greedy algorithm that will choose which box and move to make
def get_next_action(boxes, epsilon, q_table):
    q_values = {}               #dictionary of boxes, their moves, and the moves' q_values that we will get from q_table
    q_move = {}                 #dictionary of boxes and their best moves
    q_max = {}                  #dictionary of boxes and their highest q values

    #if box is not in the q table, add it to the q table
    #get q values for this box from the q table
    for box in boxes.items():
        if box[0] not in q_table:
            q_table[box[0]] = {
                UP      : 0,
                DOWN    : 0,
                LEFT    : 0,
                RIGHT   : 0
            }
        # get this box's available moves
        moves = box[1].keys()
        #get this box's q values for its available moves from the q table
        for m in moves:
            q_values[box[0]] = {m : q_table[box[0]][m]}

    # choose a random box and a random move from the reachable boxes
    box = random.choice(list(boxes.items()))
    move = random.choice(list(box[1].keys()))
    box_move = [box[0], move]

    # if a randomly chosen value between 0 and 1 is less than epsilon,
    # then of the reachable boxes, choose box with the move with the highest q value
    # else return the random box and move
    r = np.random.random()
    print(r)
    if r < epsilon:
        #for each box
        for box in q_values.keys():
            #get the box's move with the highest q value
            max_move = max(q_values[box], key=q_values[box].get)
            #save the q value of this box's move
            q_max[box] = q_values[box][max_move]
            #save this move for this box
            q_move[box] = max_move

        #get the box with the highest q value
        print(q_max)
        box = max(q_max, key=q_max.get)

        #if the max q value is not 0, return the box and its move
        #else return the random box and move
        if q_max[box] != 0:
            box_move = [box, q_move[box]]
            return box_move
        else:
            return box_move
    else:
        return box_move

def update_q_table(q_table, rewards, updated_box, action, discount_factor, learning_rate):
    # receive the reward for moving to the new state, and calculate the temporal difference
    # updated_box[0] = box's new row
    # updated_box[1] = box's new column
    reward = rewards[updated_box[0], updated_box[1]]

    #get the values needed for updating q table
    old_box = action[0]
    move = action[1]
    old_q_value = q_table[old_box][move]

    #if updated box not in q table, add it to the q table
    if updated_box not in q_table:
        q_table[updated_box] = {
            UP: 0,
            DOWN: 0,
            LEFT: 0,
            RIGHT: 0
        }

    temporal_difference = reward + (discount_factor * max(q_table[updated_box].values())) - old_q_value

    # update the Q-value for the previous state and action pair
    new_q_value = old_q_value + (learning_rate * temporal_difference)
    q_table[old_box][move] = new_q_value
    return q_table
