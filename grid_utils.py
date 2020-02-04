import colors
import grid_square
import time



def load_grid(columns, rows, WIDTH, PAD, FPS):

    # create grid and load into array
    grid = []

    xnum = rows
    ynum = columns


    for row in range(xnum):
        grid.append([])

        for column in range(ynum):
            x = row
            y = column
            square = grid_square.Grid_square(x, y, WIDTH, PAD, FPS)

            if (square.x == 0) or (square.y == 0) or (square.x == xnum - 1) or (square.y == ynum - 1) or (square.x == 1) or (square.y == 1) or (square.x == xnum - 2) or (square.y == ynum - 2):
                square.turn_to_wall()
                square.border = True

            grid[row].append(square)

    return grid






def clean_grid(grid):

    for row in grid:
        for node in row:
            if node.border == True:
                continue
            elif node.state == "wall":
                continue

            elif node.state == "start_pos":
                node.color = colors.GREEN
                continue

            elif node.state == "end_pos":
                node.color = colors.RED
                continue

            node.backtrack = False
            node.turn_red = False
            node.found = False
            node.first = True
            node.r_value = 0
            node.g_value = 0
            node.b_value = 0

            node.color = colors.WHITE
            node.children = []
            node.found = False
            node.parent = None
            node.border = False

            node.first = False
            node.r_value = 128
            node.g_value = 0
            node.b_value = 128

            node.turn_red = False
            node.backtrack = False
            node.reset = False

            node.turn_to_free()




def clear_grid(grid):

    stop = True

    for row in grid:
        for node in row:
            if node.border == True:
                continue

            node.backtrack = False
            node.turn_red = False
            node.found = False
            node.first = True
            node.r_value = 0
            node.g_value = 0
            node.b_value = 0

            node.turn_to_free()
            node.children = []
            node.found = False
            node.parent = None
            node.border = False

            node.first = False
            node.r_value = 128
            node.g_value = 0
            node.b_value = 128

            node.turn_red = False
            node.backtrack = False
            node.reset = False

            node.turn_to_free()

    stop = False





def fill_grid(grid):

    for row in grid:
        for node in row:
            if node.border == True:
                pass
            else:
                node.turn_to_wall()
