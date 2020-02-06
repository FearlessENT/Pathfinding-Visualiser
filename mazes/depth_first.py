import pygame
import random
import threading
import time
import colors
import grid_utils



def generate_maze(grid):
    print("ss")

    grid_utils.clear_grid(grid)
    grid_utils.fill_grid(grid)


    starting_node = get_random_node(grid)



    starting_node.turn_to_free()








def get_random_node(grid):

    width = len(grid[1])
    height = len(grid)

    randomx = random.randint(2, int(width / 2))
    randomy = random.randint(2, int(height / 2))

    chosen_cell = grid[randomx][randomy]

    return chosen_cell
