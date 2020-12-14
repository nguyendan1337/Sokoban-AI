from Q import *
from BFS import *
import numpy as np
import board as b
import sokoban as sb
import pprint
from actionfunction import perform_action

#
# TESTS
#
# FROM SOKOBAN INPUT FILES
# sokoban = sb.Sokoban("test/input/sokoban/sokoban00.txt")
#sokoban = sb.Sokoban("test/input/sokoban/sokoban01.txt")
# sokoban.print()
# boxes = BFS.get_reachable_boxes(sokoban.board, sokoban.agent_location)
# pprint.pprint(boxes)

# FROM TEXT LEVELS
# b = b.Board("test/input/levels/level0.txt")
# b = b.Board("test/input/levels/level1.txt")
# b = b.Board("test/input/levels/level2.txt")
b = b.Board("test/input/levels/level47.txt")
board = b.board
agent = b.agent
boxlist=b.boxes
b.print()
boxes = get_reachable_boxes(board, agent)
pprint.pprint(boxes)

#TEST GET NEXT ACTION
# q_table = {(5, 16): {'Up': 1, 'Down': 2, 'Left': 3, 'Right': 4}}
# # q_table = {}
# action = get_next_action(boxes, .9, q_table)

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