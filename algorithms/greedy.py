import time
import grid_utils
import colors
import math
from algorithms import algorithm_utils
from operator import attrgetter



def start_search(grid, PATHFINDER_DELAY, SHORTEST_PATH_DELAY):

    for row in grid:
        for square in row:
            if square.state == "start_pos":
                start_pos = square

            elif square.state == "end_pos":
                end_pos = square

    grid_utils.clean_grid(grid)



    start_pos.gScore = algorithm_utils.find_g(start_pos, start_pos)
    start_pos.hScore = algorithm_utils.find_h(start_pos, end_pos)
    start_pos.fScore = algorithm_utils.find_f(start_pos.gScore, start_pos.hScore)


    openList = [start_pos]
    closedList = []



    while len(openList) > 0:


        current_node = algorithm_utils.get_lowest_f_node(openList)



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

            h = algorithm_utils.get_distance(node, end_pos)

            hypo_fscore = current_node.gScore + algorithm_utils.get_distance(node, current_node)
            node_is_better_than_current = False


            if node not in openList:
                node_is_better_than_current = True
                node.hScore = h
                openList.append(node)

            elif hypo_fscore < node.gScore:
                node_is_better_than_current = True

            if node_is_better_than_current:
                node.parent = current_node
                node.gScore = hypo_fscore
                node.fScore = node.gScore + node.hScore

            continue
