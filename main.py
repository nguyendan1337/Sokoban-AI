from preprocess import *
from BFS import *
from Q import *
from actionfunction import perform_action
import copy
from sokoban import Sokoban
import pprint

# dictionary of q values
# state: box coordinates
# actions: UP, DOWN, LEFT, RIGHT
q_table = {}

#################
# MAIN FUNCTION #
#################
game_original = Sokoban().build("test/input/kask_input/sokoban08.txt", mode="kask")
rewards = preprocess(game_original)

# define training parameters
epsilon = 0.8  # the percentage of time when we should take the best action (instead of a random action)
discount_factor = 0.9  # discount factor for future rewards
learning_rate = 0.9  # the rate at which the AI agent should learn
r = 500

# run through 1000 training episodes
for episode in range(r):

    # initial game state
    game = copy.deepcopy(game_original)
    agent = game.agent
    board = copy.deepcopy(game.board)
    boxes = game.boxes
    explored = []
    state_history = []
    terminal = False
    print("NEW EPISODE")
    game.pprint()

    # continue moving boxes until we reach a terminal state
    while not terminal:

        # get a dictionary of reachable boxes, their available moves, and the path to those moves
        reachable_boxes = get_reachable_boxes(board, agent)
        if not reachable_boxes:
            terminal = True
            game.pprint()
            print("No reachable boxes!")
            break
        state_history += [list(reachable_boxes.keys())]

        # choose which box and move to make
        action = get_next_action(reachable_boxes, epsilon, q_table, state_history, board, rewards)
        if not action:
            terminal = True
            game.pprint()
            print("Reachable boxes have no good moves!")
            break

        # perform the action, which updates box positions, agent position, explored path, board
        agent, boxes, explored, new_box_position, board = \
            perform_action(action, reachable_boxes, boxes, explored, board, agent, rewards)

        # show move taken
        game.board = board
        game.pprint(action=new_box_position)

        # update Q values in Q Table
        q_table = update_q_table(q_table, rewards, new_box_position, action, discount_factor, learning_rate)

        # check if in terminal state
        terminal, status = is_terminal_state(boxes, rewards)
        print(status)

    # print the path the agent took, print the q table
    print("EPISODE OVER")
    print("explored " + str(len(explored)))
    print("history " + str(len(state_history)))
    if status == GOAL_STATUS:
        print("episode " + str(episode))
        print(explored)
        break
