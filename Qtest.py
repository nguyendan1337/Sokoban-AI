import Q
import BFS
import numpy as np
import board as b
import pprint

#
# TESTS
#
# FROM SOKOBAN INPUT FILES
# sokoban = sb.Sokoban("test/input/sokoban/sokoban00.txt")
# sokoban = sb.Sokoban("test/input/sokoban/sokoban01.txt")
# sokoban.print()
# boxes = BFS.get_reachable_boxes(sokoban.board, sokoban.agent_location)
# pprint.pprint(boxes)

# FROM TEXT LEVELS
np.set_printoptions(edgeitems=30, linewidth=1000,formatter=dict(float=lambda x: "%.3g" % x))
# b = b.Board("test/input/levels/level0.txt")
# b = b.Board("test/input/levels/level1.txt")
# b = b.Board("test/input/levels/level2.txt")
b = b.Board("test/input/levels/level47.txt")
board = b.board
agent = b.agent
translation = {39: None}
print(str(board).translate(translation))
boxes = BFS.get_reachable_boxes(board, agent)
pprint.pprint(boxes)

#TEST GET NEXT ACTION
q_table = {(5, 16): {'Up': 1, 'Down': 2, 'Left': 3, 'Right': 4}}
# q_table = {}
action = Q.get_next_action(boxes, .9, q_table)
print(action)