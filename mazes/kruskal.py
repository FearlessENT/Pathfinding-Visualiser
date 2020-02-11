import pygame
import random
import threading
import time
import colors
import grid_utils






def generate_maze(grid):
    print("")

    grid_utils.clear_grid(grid)

    # get all nodes


    starting_node = get_random_node(grid)

    starting_node_neighbors = get_neighbors(starting_node, grid)

    neighbor_nodes = []

    for node in starting_node_neighbors:
        neighbor_nodes.append(node)
        node.color = colors.ORANGE


    while len(neighbor_nodes) > 0:

        random_node = random.choice(neighbor_nodes)
















def get_frontier_nodes(node, grid):

    x = node.x
    y = node.y

    n_1 = grid[x + 2][y]
    n_2 = grid[x - 2][y]
    n_3 = grid[x][y + 2]
    n_4 = grid[x][y - 2]

    frontier_nodes = [n_1, n_2, n_3, n_4]

    x = 0
    while x < len(frontier_nodes):
        if (frontier_nodes[x].border == True) or (frontier_nodes[x].state == "free"):
            frontier_nodes.pop(x)
        else:
            x += 1

    return frontier_nodes








def get_random_node(grid):

    width = len(grid[1])
    height = len(grid)

    randomx = random.randint(2, int(width / 2))
    randomy = random.randint(2, int(height / 2))

    chosen_cell = grid[randomx][randomy]

    return chosen_cell
