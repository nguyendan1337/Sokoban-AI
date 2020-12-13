from preprocess import *
from board import *
from BFS import *
from Q import *
from actionfunction import actionf

# dictionary of q values
# state: box coordinates
# actions: UP, DOWN, LEFT, RIGHT
q_table = {}


#################
# MAIN FUNCTION #
#################
game_original = Board("/Users/Jillian/develope2/Sokoban-AI/test/input/levels/level1.txt")
game_original.print()
rewards = preprocess(game_original)

# define training parameters
epsilon = 0.9  # the percentage of time when we should take the best action (instead of a random action)
discount_factor = 0.9  # discount factor for future rewards
learning_rate = 0.9  # the rate at which the AI agent should learn
r = 1
explored=[]
# run through 1000 training episodes
for episode in range(r):

    #initial game state
    game=game_original
    agent = game.agent
    board = game.board
    boxes = game.boxes
    terminal = False

    # continue moving boxes until we reach a terminal state
    for episode in range(1):
        # get a dictionary of reachable boxes, their available moves, and the path to those moves
        reachable_boxes = get_reachable_boxes(board, agent)
        board[agent]=SPACE  ###added
        # choose which box and move to make
        action = get_next_action(reachable_boxes, epsilon, q_table)
        agent, boxes, explored,new_box_position = actionf(action, reachable_boxes, boxes, explored)  ####added
        board[agent]=AGENT ##Added
        board[new_box_position]=BOX
        game.board=board
        game.print()
        #update Q values in Q Table
        q_table = update_q_table(q_table, rewards, new_box_position, action, discount_factor, learning_rate)

        #terminal, status = is_terminal_state(board, boxes)

    #print(status)

