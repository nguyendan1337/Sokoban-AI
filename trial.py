from datetime import datetime

from output_format import output
from preprocess import *
from Q import *
from actionfunction import perform_action
import copy
from sokoban import Sokoban


class Trial:
    def __init__(self, file, mode, epsilon=0.8, discount_factor=0.9, learning_rate=0.9, r=500, logging=False):

        # Training parameters
        self.epsilon = epsilon                  # percentage of time when we should take the best action (instead of a random action)
        self.discount_factor = discount_factor  # discount factor for future rewards
        self.learning_rate = learning_rate      # rate at which the AI agent should learn
        self.r = r

        # Logging helper for debugging statements, i.e. replace all print(..) calls with log(..)
        self.logging = logging

        # dictionary of q values
        # state: box coordinates
        # actions: UP, DOWN, LEFT, RIGHT
        self.q_table = {}

        # Data structures used throughout the course of multiple training episodes
        self.game_original = Sokoban().build(file, mode=mode)
        self.rewards = preprocess(self.game_original)

        print("\n-------------------------------------------------")
        print("Initialized Trial with parameters:")
        print("-------------------------------------------------")
        print("File = {f}".format(f=file))
        print("Mode = {m}".format(m=mode))
        print("Epsilon = {e}".format(e=epsilon))
        print("Discount factor = {d}".format(d=discount_factor))
        print("Learning rate = {l}".format(l=learning_rate))
        print("Training episodes = {r}".format(r=r))
        print("Logging = {l}".format(l=logging))
        print("-------------------------------------------------\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Initial Game State: ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        self.game_original.pprint()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    # Essentially just print(..), but only executes when the logging option is set to True
    def log(self, message):
        if self.logging:
            print(message)

    def run(self):
        print("\n-------------------------------------------------")
        print("Commencing trial at {t}".format(t=datetime.now().time()))
        print("-------------------------------------------------")
        # run through "r" number of training episodes
        for episode in range(self.r):

            # initial game state
            game = copy.deepcopy(self.game_original)
            agent = game.agent
            board = copy.deepcopy(game.board)
            boxes = game.boxes
            explored = []
            state_history = []
            terminal = False
            self.log("EPISODE NUMBER {e}".format(e=episode))
            game.pprint(logging=self.logging)

            # continue moving boxes until we reach a terminal state
            while not terminal:

                # get a dictionary of reachable boxes, their available moves, and the path to those moves
                reachable_boxes = get_reachable_boxes(board, agent)
                if not reachable_boxes:
                    terminal = True
                    game.pprint(logging=self.logging)
                    self.log("No reachable boxes!")
                    break

                state_history += [list(reachable_boxes.keys())]

                # choose which box and move to make
                action = get_next_action(reachable_boxes, self.epsilon, self.q_table, state_history, board, self.rewards)

                # perform the action, which updates box positions, agent position, explored path, board
                agent, boxes, explored, new_box_position, board = \
                    perform_action(action, reachable_boxes, boxes, explored, board, agent, self.rewards)

                # show move taken
                game.board = board
                game.pprint(action=new_box_position, logging=self.logging)

                # update Q values in Q Table
                self.q_table = update_q_table(self.q_table, self.rewards, new_box_position, action, self.discount_factor, self.learning_rate)

                # check if in terminal state
                terminal, status = is_terminal_state(boxes, self.rewards)
                self.log(status)

                # Regardless of logging settings, if it is successful, print
                if status is GOAL_STATUS:
                    game.pprint()
                    print("SUCCESS at EPISODE = {e}".format(e=episode))
                    output(explored)  # print solution to maze

            # print the path the agent took, print the q table
            self.log("EPISODE OVER")

        print("Trial completed at {t}".format(t=datetime.now().time()))
