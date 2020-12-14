import queue as q
from constants import *

#
# getReachableBoxes()
# parameters: board, agent
# returns: dictionary of boxes
#
def get_reachable_boxes(board, agent):

    frontier = q.Queue()                                            #create frontier queue
    start = agent
    frontier.put((start, []))                                       #put agent's current location onto frontier (node, [path])
    visited = {agent}                                               #create set of reached spaces, add agent's current location
    boxes = {}                                                      #dictionary of boxes key=coordinates: value=[moves]

    while not frontier.empty():                                     #while the frontier is not empty
        node, path = frontier.get()                                 #pop from frontier
        neighbors, boxes = expand(board, node, boxes, path)         #expand the node, get its neighbor children and boxes
        for neighbor in neighbors:                                  #for each neighbor
            if neighbor[1] not in visited:                             #if neighbor has not been visited
                visited.add(neighbor[1])                               #add neighbor to visited
                frontier.put((neighbor[1], path + [neighbor]))         #put neighbor onto frontier as well as path to neighbor

    return boxes

#
# expand()
# parameters: board, node, boxes, path
# returns: list of neighbors, dictionary of boxes
#
def expand(board, node, boxes, path):
    neighbors = []

    ##UP##
    if board[node[0] - 1][node[1]] != WALL:                         #if UP is not a wall
        if board[node[0] - 1][node[1]] == BOX:                          #if UP is a box
            if board[node[0] - 2][node[1]] != WALL\
                    and board[node[0] - 2][node[1]] != BOX:                         #if you can push the box UP
                if (node[0] - 1, node[1]) in boxes:                             #if box exists in list of boxes
                    boxes[(node[0] - 1, node[1])]\
                        .update({UP: path + [[UP, (node[0]-1, node[1])]]})                #add UP and path to box's moves
                else:
                    boxes[(node[0] - 1, node[1])] \
                        = {UP: path + [[UP, [(node[0]-1, node[1])]]]}                       #else add box to boxes
        else:
            neighbors.append([UP, (node[0] - 1, node[1])])                     #else add UP to neighbors

    ##DOWN##
    if board[node[0] + 1][node[1]] != WALL:                         #if DOWN is not a wall
        if board[node[0] + 1][node[1]] == BOX:                          #if DOWN is a box
            if board[node[0] + 2][node[1]] != WALL\
                    and board[node[0] + 2][node[1]] != BOX:                         #if you can push the box DOWN
                if (node[0] + 1, node[1]) in boxes:                             # if box exists in list of boxes
                    boxes[(node[0] + 1, node[1])]\
                        .update({DOWN: path + [[DOWN, (node[0]+1, node[1])]]})              # add DOWN and path to box's moves
                else:
                    boxes[(node[0] + 1, node[1])] \
                        = {DOWN: path + [[DOWN, (node[0]+1, node[1])]]}                     # else add box to boxes
        else:
            neighbors.append([DOWN, (node[0] + 1, node[1])])                    #else add DOWN to neighbors

    ##LEFT##
    if board[node[0]][node[1] - 1] != WALL:                         #if LEFT is not a wall
        if board[node[0]][node[1] - 1] == BOX:                          #if LEFT is a box
            if board[node[0]][node[1] - 2] != WALL\
                    and board[node[0]][node[1] - 2] != BOX:                         #if you can push the box LEFT
                if (node[0], node[1] - 1) in boxes:                             # if box exists in list of boxes
                    boxes[(node[0], node[1] - 1)]\
                        .update({LEFT: path + [[LEFT, (node[0], node[1]-1)]]})              # add LEFT and path to box's moves
                else:
                    boxes[(node[0], node[1] - 1)] \
                        = {LEFT: path + [[LEFT, (node[0], node[1]-1)]]}                     # else add box to boxes
        else:
            neighbors.append([LEFT, (node[0], node[1] - 1)])                    #else add LEFT to neighbors

    ##RIGHT##
    if board[node[0]][node[1] + 1] != WALL:                         #if RIGHT is not a wall
        if board[node[0]][node[1] + 1] == BOX:                          #if RIGHT is a box
            if board[node[0]][node[1] + 2] != WALL\
                    and board[node[0]][node[1] + 2] != WALL:                         #if you can push the box RIGHT
                if (node[0], node[1] + 1) in boxes:                             # if box exists in list of boxes
                    boxes[(node[0], node[1] + 1)]\
                        .update({RIGHT: path + [[RIGHT, (node[0], node[1]+1)]]})             # add RIGHT and path to box's moves
                else:
                    boxes[(node[0], node[1] + 1)] \
                        = {RIGHT: path + [[RIGHT, (node[0], node[1]+1)]]}                    # else add box to boxes
        else:
            neighbors.append([RIGHT, (node[0], node[1] + 1)])                    #else add RIGHT to neighbors

    return neighbors, boxes
