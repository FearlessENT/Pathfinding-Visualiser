import pygame
import random
import threading
import time
import colors
import grid_utils



def color_nodes(nodes):

    for node in nodes:
        node.color = colors.PURPLE



def delete_fronteir_cell(array, target):

    if target in array:
        array.remove(target)
        delete_fronteir_cell(array, target)



def generate_maze(grid):

    grid_utils.clear_grid(grid)
    grid_utils.fill_grid(grid)

    # pick random node
    starting_node = get_random_node(grid)

    starting_node.color = colors.ORANGE
    starting_node.turn_to_free()

    frontier_nodes = get_frontier_nodes(starting_node, grid)

    while len(frontier_nodes) != 0:

        time.sleep(0.001)
        color_nodes(frontier_nodes)

        # pick random cell from frontier cells
        random_frontier_node = random.choice(frontier_nodes)

        neighbors = get_neighbors(random_frontier_node, grid)

        try:
            random_neighbor = random.choice(neighbors)
        except Exception:
            pass


        # get midpoint from random fronteir node and random neighbor
        midpoint_x = int((random_frontier_node.x + random_neighbor.x) / 2)
        midpoint_y = int((random_frontier_node.y + random_neighbor.y) / 2)

        # break down wall and set to passage
        middle_cell = grid[midpoint_x][midpoint_y]
        middle_cell.turn_to_free()
        random_neighbor.turn_to_free()

        new_frontier_nodes = get_frontier_nodes(random_frontier_node, grid)

        for node in new_frontier_nodes:
            frontier_nodes.append(node)

        frontier_nodes.remove(random_frontier_node)
        delete_fronteir_cell(frontier_nodes, random_frontier_node)

        random_frontier_node.turn_to_free()



def get_neighbors(node, grid):

    x = node.x
    y = node.y

    n_1 = grid[x + 2][y]
    n_2 = grid[x - 2][y]
    n_3 = grid[x][y + 2]
    n_4 = grid[x][y - 2]

    neighbor_nodes = [n_1, n_2, n_3, n_4]

    x = 0
    while x < len(neighbor_nodes):
        if (neighbor_nodes[x].border == True) or (neighbor_nodes[x].state == "wall"):
            neighbor_nodes.pop(x)
        else:
            x += 1

    return neighbor_nodes



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
