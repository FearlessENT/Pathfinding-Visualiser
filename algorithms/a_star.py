import grid_utils
import colors
import math
from operator import attrgetter
import time





def start_search(grid, PATHFINDER_DELAY, SHORTEST_PATH_DELAY):

    # get the start position and end position
    for row in grid:
        for square in row:
            if square.state == "start_pos":
                start_pos = square

            elif square.state == "end_pos":
                end_pos = square

    grid_utils.clean_grid(grid)

    start_pos.gScore = find_g(start_pos, start_pos)
    start_pos.hScore = find_h(start_pos, end_pos)
    start_pos.fScore = find_f(start_pos.gScore, start_pos.hScore)


    openList = [start_pos]
    closedList = []

    while len(openList) > 0:

        current_node = get_lowest_f_node(openList)

        openList.remove(current_node)
        closedList.append(current_node)

        if current_node.state == "end_pos":

            time.sleep(0.02)

            path = [end_pos]
            node = current_node
            while node.parent != None:
                time.sleep(SHORTEST_PATH_DELAY)
                node = node.parent
                path.append(node)
                if node != end_pos:
                    node.color = colors.GREEN

                node.backtrack = True


            start_pos.color = colors.RED
            end_pos.color = colors.RED
            return

        if current_node == start_pos:
            current_node.color = colors.RED
        else:
            current_node.color = colors.ORANGE
            current_node.found = True

        time.sleep(PATHFINDER_DELAY)

        x = current_node.x
        y = current_node.y

        # get nodes around current node
        node1 = grid[x][y - 1]
        node2 = grid[x][y + 1]
        node3 = grid[x - 1][y]
        node4 = grid[x + 1][y]

        successor_nodes = [node1, node2, node3, node4]

        for node in successor_nodes:

            # check if walkable
            if (node.state == "wall") or (node in closedList):
                continue

            hypo_fscore = current_node.gScore + find_h(node, current_node)
            node_is_better_than_current = False

            if node not in openList:
                node_is_better_than_current = True
                node.hScore = find_h(node, end_pos)
                openList.append(node)

            elif hypo_fscore < node.gScore:
                node_is_better_than_current = True

            if node_is_better_than_current == True:
                node.parent = current_node
                node.gScore = hypo_fscore
                node.fScore = node.gScore + node.hScore

    print("Path Not Found")

    for node in closedList:
        if node.state == "wall":
            continue
        elif node == start_pos:
            node.color = colors.GREEN
        else:
            node.backtrack = True
            node.turn_red = True






def get_lowest_f_node(array):

    min_f = min(array, key = attrgetter("fScore"))
    return min_f


# distance from current node and start node
def find_g(current, start_pos):
    g = get_distance(current, start_pos)
    return g


# distance from current node and target / destination / finish node
def find_h(current, end_pos):

    dx = abs(current.x - end_pos.x)
    dy = abs(current.y - end_pos.y)

    D = 1
    D2 = 1
    h = D * ((dx + dy) + (D2 - 2 * D) * min(dx, dy))

    return h


# hscore and gscore added together
def find_f(score1, score2):
    return score1 + score2


# distance from 2 points. also the hueristics, which is causing issues
def get_distance(start, end):
    x1 = start.x
    y1 = start.y
    x2 = end.x
    y2 = end.y
    distancex = sqr(x2 - x1)
    distancey = sqr(y2 - y1)
    distance = sqrt(distancex + distancey)
    distance = distancex + distancey
    return distance


def sqr(number):
    return number * number


def sqrt(number):
    return math.sqrt(number)
