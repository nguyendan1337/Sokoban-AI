from Q import *
from BFS import *
import numpy as np
from sokoban import Sokoban
import sokoban as sb
import pprint
import collections
from actionfunction import perform_action

#
# TESTS
#
game = Sokoban().build("test/input/kask_input/sokoban01.txt", mode="kask")
board = game.board
agent = game.agent
boxlist=game.boxes
game.pprint()
boxes = get_reachable_boxes(board, agent)
pprint.pprint(boxes)
# state_history = []
# state_history += [list(boxes.keys())]
# print(state_history)
#####SAUCE#########
reachable_boxes = list(boxes.keys())
state_history = [list(boxes.keys())]
state_history += [[(5, 4), (4,6)]]
old_box = (4,5)
new_box = (4,6)
print(state_history)
new_state = [new_box if box == old_box else box for box in reachable_boxes]
print(new_state)
for state in state_history:
    print(collections.Counter(new_state) == collections.Counter(state))
# print(collections.Counter(new_state) == collections.Counter(state_history))
###################

#TEST GET NEXT ACTION
q_table = {(5, 16): {'Up': 1, 'Down': 2, 'Left': 3, 'Right': 4}}
# q_table = {}
action = get_next_action(boxes, .9, q_table, list(boxes.keys()))
# print(action)

#perform action; needs to be fed an explored list that needs to be init in main...
# explored=[]#need to get rid of
# agent, board_boxes,explored,_,_=perform_action(action, boxes, boxlist, explored, board, agent)
# print('original:',boxlist)
# print('\n',agent,'\n', 'new:',board_boxes,'\n', explored)


###


#TEST UPDATE Q TABLE
# rewards = np.zeros((board.shape[0], board.shape[1]))
# rewards[action[0][0], action[0][1]] = -1
# updated_box = action[0]
# if action[1] == UP:
#     updated_box = (updated_box[0]-1, updated_box[1])
# if action[1] == DOWN:
#     updated_box = (updated_box[0]+1, updated_box[1])
# if action[1] == LEFT:
#     updated_box = (updated_box[0], updated_box[1]-1)
# if action[1] == RIGHT:
#     updated_box = (updated_box[0]-1, updated_box[1]+1)
# rewards[updated_box[0], updated_box[1]] = 100
# # print(rewards)
# print(q_table)
# q_table = update_q_table(q_table, rewards, updated_box, action, .9, .9)
# print(q_table)