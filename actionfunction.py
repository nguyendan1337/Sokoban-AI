def actionf(action, reachbox, board_boxes, explored):
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

    board_boxes=[new_box_position if box==action[0] else box for box in board_boxes] #return

    explored += reachbox[agent][move] #return

    return agent, board_boxes, explored,new_box_position






