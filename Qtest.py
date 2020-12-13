import Q
import BFS
import numpy as np
import board as b
import sokoban as sb
import pprint

# Moves
UP = "Up"
DOWN = "Down"
LEFT = "Left"
RIGHT = "Right"

#
# TESTS
#
# FROM SOKOBAN INPUT FILES
# sokoban = sb.Sokoban("test/input/sokoban/sokoban00.txt")
sokoban = sb.Sokoban("test/input/sokoban/sokoban01.txt")
sokoban.print()
boxes = BFS.get_reachable_boxes(sokoban.board, sokoban.agent)
pprint.pprint(boxes)

# FROM TEXT LEVELS
# b = b.Board("test/input/levels/level0.txt")
# b = b.Board("test/input/levels/level1.txt")
# b = b.Board("test/input/levels/level2.txt")
# b = b.Board("test/input/levels/level47.txt")
# board = b.board
# agent = b.agent
# translation = {39: None}
# print(str(board).translate(translation))
# boxes = BFS.get_reachable_boxes(board, agent)
# pprint.pprint(boxes)

#TEST GET NEXT ACTION
q_table = {(5, 16): {'Up': 1, 'Down': 2, 'Left': 3, 'Right': 4}}
# q_table = {}
action = Q.get_next_action(boxes, .9, q_table)
print(action)

#TEST UPDATE Q TABLE
# rewards = np.zeros((b.height, b.width))
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
# print(rewards)
# print(q_table)
# q_table = Q.update_q_table(q_table, rewards, updated_box, action, .9, .9)
# print(q_table)