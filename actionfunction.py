from constants import *

def perform_action(action, reachable_boxes, boxes, explored, board, agent):
    # update previous agent location on board
    board[agent] = SPACE

    new_box_position=0
    agent=action[0] #return
    oldbox_p=action[0]
    move=action[1]

    if move=='Up':
        new_box_position=(oldbox_p[0]-1, oldbox_p[1])
    if move=='Down':
        new_box_position = (oldbox_p[0]+1, oldbox_p[1])
    if move=='Left':
        new_box_position = (oldbox_p[0], oldbox_p[1]-1)
    if move=="Right":
        new_box_position = (oldbox_p[0], oldbox_p[1]+1)

    boxes=[new_box_position if box == action[0] else box for box in boxes] #return

    explored += reachable_boxes[agent][move] #return

    board[agent] = AGENT
    board[new_box_position] = BOX

    return agent, boxes, explored, new_box_position, board






