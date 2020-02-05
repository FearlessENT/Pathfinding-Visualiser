import pygame
import math
import time
import threading
import tkinter
import os
from grid_square import Grid_square
from window_settings import Change_window_settings_interface
from operator import attrgetter
import maze_prim
import grid_utils
import colors
from algorithms import *
from mazes import *



# get settings
f = open("settings.txt", "r")

content = f.readlines()

x = 0
while x < len(content):

    new_value = str(content[x]).rstrip("\n")
    content[x] = new_value

    x += 1

f.close()



WIN_WIDTH = int(content[0])
WIN_HEIGHT = int(content[1])

WIDTH = int(content[2])
HEIGHT = WIDTH
PAD = int(content[3])
PATHFINDER_DELAY = float(content[4])
SHORTEST_PATH_DELAY = float(content[5])
FPS = int(content[6])





red = False


global current_mode
current_mode = "wall"







def settings_control():

    thread1 = threading.Thread(target = open_settings_window)
    thread1.start()


def open_settings_window():
    window1 = Change_window_settings_interface()





class Interface:

    """base class for the user interface"""

    def __init__(self):

        self.current_algorithm = "diekstra"
        self.current_maze = "prims"

        self.tkinter_window = tkinter.Tk()
        self.tkinter_window.geometry("{}x{}".format(WIN_WIDTH, WIN_HEIGHT))
        self.tkinter_window.title("Pathfinding Visualiser")
        direc = os.getcwd()
        direc = str(direc) + "\\logo.ico"
        self.tkinter_window.iconbitmap(direc)

        framex = int(WIN_WIDTH * 0.7)
        framey = int(WIN_HEIGHT * 0.9)

        self.embed = tkinter.Frame(self.tkinter_window, width = framex, height = framey)
        self.embed.grid(row = 1, column = 1, columnspan = 10, rowspan = 10)

        os.environ["SDL_WINDOWID"] = str(self.embed.winfo_id())
        os.environ["SDL_VIDEODRIVER"] = "windib"
        pygame.init()


        rows = int(framey / (WIDTH + PAD))
        columns = int(framex / (HEIGHT + PAD))
        global grid
        grid = grid_utils.load_grid(columns, rows, WIDTH, PAD, FPS)



        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()



        # the buttons to control pathfinding
        # below controls the width of the buttons to make fit in the window no matter what size window is
        but_width = int(WIN_WIDTH / 100)* 2
        but_width = int(framex / 45)
        but_height = int(WIN_HEIGHT / 100)
        but_height = int(framey / 200)

        self.wall_button = tkinter.Button(text = "Walls", width = but_width, height = but_height, command = current_walls, bg = "grey")
        self.start_pos_button = tkinter.Button(text = "Start Position", width = but_width, height = but_height, command = current_start_pos, bg = "green")
        self.end_pos_button = tkinter.Button(text = "End Position", width = but_width, height = but_height, command = current_end_pos, bg = "red")
        self.go_button = tkinter.Button(text = "Begin Pathfinding", width = but_width, height = but_height, command = lambda: current_go(self.current_algorithm), bg = "blue")
        self.clear_grid_button = tkinter.Button(text = "Clear Grid", width = but_width, height = but_height, command = current_clear_grid, bg = "orange")

        padxv = int(WIN_WIDTH / 1000)
        self.wall_button.grid(row = 11, column = 1, padx = padxv, pady = padxv)
        self.start_pos_button.grid(row = 11, column = 2, padx = padxv, pady = padxv)
        self.end_pos_button.grid(row = 11, column = 3, padx = padxv, pady = padxv)
        self.go_button.grid(row = 11, column = 4, padx = padxv, pady = padxv)
        self.clear_grid_button.grid(row = 11, column = 5, padx = padxv, pady = padxv)

        self.create_maze_button = tkinter.Button(text = "Generate Maze", width = but_width, height = but_height, command = lambda: create_maze_control(self.current_maze))
        self.create_maze_button.grid(row = 11, column = 6, padx = padxv, pady = padxv)



        # select which pathfinding algorithm to use

        width = int((WIN_WIDTH / 100) * 2)
        height = int(width / 5)




        font_size = int(width / 2)
        font = ("SimSun", font_size)

        self.algorithm_frame = tkinter.Frame(background = "gainsboro")
        self.algorithm_frame.grid(row = 1, column = 12, sticky = "n", padx = 4)

        self.pathfinding_algorithms_label = tkinter.Label(self.algorithm_frame, text = "Algorithms", bg = "cyan", width = width, height = height, font = font)
        self.pathfinding_algorithms_label.pack(pady = 7)


        self.diekstra_button = tkinter.Button(self.algorithm_frame, text = "Dijkstra's", bg = "green2", width = width, height = height, font = font, command = lambda: self.algorithm_select("diekstra"))
        self.diekstra_button.pack(fill = "both", pady = 2)

        self.a_star_button = tkinter.Button(self.algorithm_frame, text = "A*", width = width, height = height, font = font, command = lambda: self.algorithm_select("a_star"))
        self.a_star_button.pack(fill = "both", pady = 2)

        self.greedy_button = tkinter.Button(self.algorithm_frame, text = "Greedy First", width = width, height = height, font = font, command = lambda: self.algorithm_select("greedy"))
        self.greedy_button.pack(fill = "both", pady = 2)

        self.algorithms = [self.greedy_button, self.diekstra_button, self.a_star_button]



        self.information_frame = tkinter.Frame(background = "gainsboro")
        self.information_frame.grid(row = 2, column = 12)



        # maze selection
        self.maze_frame = tkinter.Frame(background = "gainsboro")
        self.maze_frame.grid(row = 1, column = 13, sticky = "n", padx = 4)

        self.maze_label = tkinter.Label(self.maze_frame, text = "Mazes", bg = "cyan", width = width, height = height, font = font)
        self.maze_label.pack(fill = "both", pady = 7)

        self.prim_button = tkinter.Button(self.maze_frame, text = "Prims Algorithm", bg = "green2", width = width, height = height, font = font, command = lambda: self.maze_select("prims"))
        self.prim_button.pack(fill = "both", pady = 2)

        self.depth_button = tkinter.Button(self.maze_frame, text = "Depth-First", width = width, height = height, font = font, command = lambda: self.maze_select("depth"))
        self.depth_button.pack(fill = "both", pady = 2)


        self.mazes = [self.prim_button, self.depth_button]




        # settigs button
        self.settings_button = tkinter.Button(text = "Settings", command = settings_control)
        self.settings_button.grid(row = 11, column = 12)






    def algorithm_select(self, selected_algorithm):

        self.current_algorithm = selected_algorithm

        for algorithm in self.algorithms:
            algorithm.configure(bg = "white")

        if selected_algorithm == "a_star":
            self.a_star_button.configure(bg = "green2")

        elif selected_algorithm == "diekstra":
            self.diekstra_button.configure(bg = "green2")

        elif selected_algorithm == "greedy":
            self.greedy_button.configure(bg = "green2")



    def maze_select(self, selected_maze):

        self.current_maze = selected_maze

        for maze in self.mazes:
            maze.configure(bg = "white")

        if selected_maze == "prims":
            self.prim_button.configure(bg = "green2")

        elif selected_maze == "depth":
            self.depth_button.configure(bg = "green2")






def create_maze_control(maze):


    if maze == "prims":

        thread1 = threading.Thread(target = create_maze_prim)
        thread1.start()

    elif maze == "depth":

        thread1 = threading.Thread(target = create_maze_depth)
        thread1.start()




def create_maze_prim():

    prim.generate_maze(grid)


def create_maze_depth():

    depth_first.generate_maze(grid)










def current_walls():
    global current_mode
    current_mode = "wall"

def current_start_pos():
    global current_mode
    current_mode = "start_pos"

def current_end_pos():
    global current_mode
    current_mode = "end_pos"

def current_clear_grid():
    thread2 = threading.Thread(target = grid_utils.clear_grid, args = (grid,))
    thread2.start()


def current_go(algorithm):
    print("Running...")

    if algorithm == "a_star":
        thread1 = threading.Thread(target = a_star.start_search, args = (grid, PATHFINDER_DELAY, SHORTEST_PATH_DELAY,))
        thread1.start()

    elif algorithm == "diekstra":
        thread1 = threading.Thread(target = diekstra.start_search, args = (grid, PATHFINDER_DELAY, SHORTEST_PATH_DELAY,))
        thread1.start()

    elif algorithm == "greedy":
        thread1 = threading.Thread(target = greedy.start_search, args = (grid, PATHFINDER_DELAY, SHORTEST_PATH_DELAY,))
        thread1.start()

    else:
        print("not programmed yet")










def main():


    main_window = Interface()
    clock = pygame.time.Clock()


    running = True
    while running:
        clock.tick(FPS)

        main_window.window.fill(colors.BLACK)

        clicking = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



            elif event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()





                # check if grid is clicked
                column = position[0] // (WIDTH + PAD)
                row = position[1] // (HEIGHT + PAD)
                try:
                    grid[row][column].clicked(current_mode)
                except:
                    pass


            elif pygame.mouse.get_pressed()[0]:


                #print("user dragged")

                position = event.pos
                column = position[0] // (WIDTH + PAD)
                row = position[1] // (HEIGHT + PAD)

                if current_mode == "end_pos":
                    pass
                elif current_mode == "start_pos":
                    pass


                else:
                    try:
                        if grid[row][column].state == current_mode:
                            pass
                        else:
                            grid[row][column].clicked(current_mode)

                    except:
                        pass





        # update all the squares
        for row in grid:
            for square in row:
                square.animate()
                square.draw(main_window.window)




        pygame.display.update()
        try:
            main_window.tkinter_window.update()
        except:
            pygame.quit()
            quit()
    pygame.quit()
    quit()


















main()
