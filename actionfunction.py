from constants import *


def perform_action(action, reachable_boxes, boxes, explored, board, agent, rewards):
    # update previous agent location on board
    if rewards[agent] == GOAL_REWARD:
        board[agent] = GOAL
    else:
        board[agent] = SPACE

    new_box_position = 0
    agent = action[0]  # return
    oldbox_p = action[0]
    move = action[1]

    if move == UP:
        new_box_position = (oldbox_p[0] - 1, oldbox_p[1])
    if move == DOWN:
        new_box_position = (oldbox_p[0] + 1, oldbox_p[1])
    if move == LEFT:
        new_box_position = (oldbox_p[0], oldbox_p[1] - 1)
    if move == RIGHT:
        new_box_position = (oldbox_p[0], oldbox_p[1] + 1)

    boxes = [new_box_position if box == action[0] else box for box in boxes]  # return

    explored += reachable_boxes[agent][move]  # return

    board[agent] = AGENT
    if rewards[new_box_position] == GOAL_REWARD:
        board[new_box_position] = BOX_ON_GOAL
    else:
        board[new_box_position] = BOX

    return agent, boxes, explored, new_box_position, board
