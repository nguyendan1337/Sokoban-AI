import sokoban as sb
import queue as q

# String constants for each component of the Sokoban puzzle
WALL = "#"
AGENT = "@"
GOAL = "."
BOX = "$"

# Moves
UP = "Up"
DOWN = "Down"
LEFT = "Left"
RIGHT = "Right"

#
# getReachableBoxes
# parameters: board, agent
# returns: list of boxes
#
def getReachableBoxes(board, agent):

    frontier = q.Queue()                                        #create frontier
    frontier.put(agent.coordinates)                             #push agent's current location onto frontier
    reached = [agent.coordinates]                               #create list of reached spaces, add agent's current location
    boxes = {}                                                  #dictionary of boxes key=coordinates: value=[moves]

    while not frontier.empty():                                 #while the frontier is not empty
        node = frontier.get()                                   #pop from frontier
        children, boxes = expand(board, node, boxes)            #expand the node, get its neighbor children and boxes
        for child in children:
            if child not in reached:
                reached.append(child)
                frontier.put(child)

    return boxes

def expand(board, node, boxes):
    children = []

    if board[node[0] - 1][node[1]] != WALL:                     #if UP is not a wall
        if board[node[0] - 1][node[1]] == BOX:                      #if UP is a box
            if board[node[0] - 2][node[1]] != WALL:                     #if you can push the box UP
                if (node[0] - 1, node[1]) in boxes:                         #if box exists in list of boxes
                    boxes[(node[0] - 1, node[1])].append(UP)                    #add UP to box's moves
                else:
                    boxes[(node[0] - 1, node[1])] = [UP]                    #else add box to boxes
        else:
            children.append((node[0] - 1, node[1]))                 #else add UP to children

    if board[node[0] + 1][node[1]] != WALL:                     #if DOWN is not a wall
        if board[node[0] + 1][node[1]] == BOX:                      #if DOWN is a box
            if board[node[0] + 2][node[1]] != WALL:                     #if you can push the box DOWN
                if (node[0] + 1, node[1]) in boxes:                         # if box exists in list of boxes
                    boxes[(node[0] + 1, node[1])].append(DOWN)                    # add DOWN to box's moves
                else:
                    boxes[(node[0] + 1, node[1])] = [DOWN]                  # else add box to boxes
        else:
            children.append((node[0] + 1, node[1]))                 #else add DOWN to children

    if board[node[0]][node[1] - 1] != WALL:                     #if LEFT is not a wall
        if board[node[0]][node[1] - 1] == BOX:                      #if LEFT is a box
            if board[node[0]][node[1] - 2] != WALL:                     #if you can push the box LEFT
                if (node[0], node[1] - 1) in boxes:                         # if box exists in list of boxes
                    boxes[(node[0], node[1] - 1)].append(LEFT)                  # add UP to box's moves
                else:
                    boxes[(node[0], node[1] - 1)] = [LEFT]                  # else add box to boxes
        else:
            children.append((node[0], node[1] - 1))                 #else add LEFT to children

    if board[node[0]][node[1] + 1] != WALL:                     #if RIGHT is not a wall
        if board[node[0]][node[1] + 1] == BOX:                      #if RIGHT is a box
            if board[node[0]][node[1] + 2] != WALL:                     #if you can push the box RIGHT
                if (node[0], node[1] + 1) in boxes:                         # if box exists in list of boxes
                    boxes[(node[0], node[1] + 1)].append(RIGHT)                  # add UP to box's moves
                else:
                    boxes[(node[0], node[1] + 1)] = [RIGHT]                  # else add box to boxes
        else:
            children.append((node[0], node[1] + 1))                 #else add RIGHT to children

    return children, boxes

sokoban = sb.Sokoban("test/sokoban01.txt")
agent = sb.Agent(sokoban.agentX, sokoban.agentY)
boxes = getReachableBoxes(sokoban.board, agent)
print(boxes)
