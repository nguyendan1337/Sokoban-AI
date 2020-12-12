import random
import numpy as np
import BFS
import sokoban as sb
import board as b
import pprint

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
def is_terminal_state(board, boxes, rewards):

    #if all boxes are in goals, terminal will remain true
    for box in boxes:
        # if the reward for this box's location is -100, then it is in a corner terminal state
        if rewards[box[0], box[1]] == -100:
            return True, DEAD
        # if the box is not at a goal, then it is not in a terminal state
        if rewards[box[0], box[1]] == -1:
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
    box_move = {box[0]: move}

    # if a randomly chosen value between 0 and 1 is less than epsilon,
    # then of the reachable boxes, choose box with the move with the highest q value
    # else return the random box and move
    r = np.random.random()
    # print(r)
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


#
# TESTS
#
# FROM SOKOBAN INPUT FILES
# sokoban = sb.Sokoban("test/input/sokoban/sokoban00.txt")
# sokoban = sb.Sokoban("test/input/sokoban/sokoban01.txt")
# sokoban.print()
# agent = sb.Agent(sokoban.agentX, sokoban.agentY)
# boxes = get_reachable_boxes(sokoban.board, agent)
# pprint.pprint(boxes)

# FROM TEXT LEVELS
# np.set_printoptions(edgeitems=30, linewidth=1000,formatter=dict(float=lambda x: "%.3g" % x))
# b = b.Board("test/input/levels/level0.txt")
# b = b.Board("test/input/levels/level1.txt")
# b = b.Board("test/input/levels/level2.txt")
# b = b.Board("test/input/levels/level47.txt")
# board = b.board
# translation = {39: None}
# print(str(board).translate(translation))
# agent = sb.Agent(b.agentX, b.agentY)
# boxes = BFS.get_reachable_boxes(board, agent)
# pprint.pprint(boxes)

#TEST GET NEXT ACTION
# q_table = {(4, 7): {'Up': 1, 'Down': 2, 'Left': 3, 'Right': 4}}
# q_table = {}
# action = get_next_action(boxes, .9, q_table)
# print(action)