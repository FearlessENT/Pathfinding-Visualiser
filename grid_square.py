import pygame
import colors


class Grid_square:



    """base class for a grid square """

    def __init__(self, row, column, WIDTH, PAD, FPS):

        self.x = row
        self.y = column

        self.WIDTH = WIDTH
        self.HEIGHT = WIDTH
        self.PAD = PAD
        self.FPS = FPS



        self.state = "free"
        self.color = colors.WHITE

        self.gScore = None
        self.hScore = None
        self.fScore = None
        self.children = []
        self.found = False
        self.parent = None
        self.border = False

        self.first = False
        self.r_value = 128
        self.g_value = 0
        self.b_value = 128

        self.turn_red = False
        self.backtrack = False
        self.reset = False


        # maze stuff
        self.maze_state = None





    def clicked(self, target_state):

        if target_state == self.state:
            self.turn_to_free()
            return

        elif target_state == "wall":
            self.turn_to_wall()
            return

        elif target_state == "start_pos":
            self.turn_to_start_pos()
            return

        elif target_state == "end_pos":
            self.turn_to_end_pos()
            return



    def turn_to_start_pos(self):
        self.state = "start_pos"
        self.color = colors.GREEN

    def turn_to_end_pos(self):
        self.state = "end_pos"
        self.color = colors.RED

    def turn_to_wall(self):
        self.state = "wall"
        self.color = colors.GREY

    def turn_to_free(self):
        self.state = "free"
        self.color = colors.WHITE


    def animate(self):


        # has node been found yet? dont want unfound nodes changing color
        if self.found == True:

            # is it first time being found? if yes, then change color from constant to convertable color
            if self.first == False:
                self.color = (self.r_value, self.g_value, self.b_value)
                self.first = True
                return



            # if the color is already dynamic, then increase the rgb color


            # if is not being backtracked
            if self.backtrack == False:

                multiplyer = (1 / self.FPS) * 100
                self.r_value = self.r_value + multiplyer
                self.g_value = self.g_value + multiplyer
                self.b_value = self.b_value + multiplyer

                if self.r_value > 255:
                    self.r_value = 255

                elif self.b_value >= 200:
                    self.r_value = self.r_value - (multiplyer * 2)
                    if self.r_value <= 0:
                        self.r_value = 0

                if self.g_value > 180:
                    self.g_value = 180

                if self.b_value > 200:
                    self.b_value = 200





            #IF IS BEing backtracked and needs to turn red
            elif self.backtrack == True and self.turn_red == True:

                multiplyer = (1 / self.FPS) * 100
                self.r_value = self.r_value + multiplyer * 2
                self.g_value = self.g_value - multiplyer
                self.b_value = self.b_value - multiplyer

                if self.r_value > 255:
                    self.r_value = 255

                if self.g_value <= 0:
                    self.g_value = 0

                if self.b_value < 0:
                    self.b_value = 0


            else:
                return

            self.color = (self.r_value, self.g_value, self.b_value)



    def current_state(self):
        return self.state



    def print_values(self):
        print("Node Coords: ", self.x, self.y)
        print("gScore: ", self.gScore)
        print("hScore: ", self.hScore)
        print("fScore: ", self.fScore)



    def draw(self, window):
        pygame.draw.rect(window, self.color, [(self.WIDTH + self.PAD) * self.y + self.PAD, (self.HEIGHT + self.PAD) * self.x + self.PAD, self.WIDTH, self.HEIGHT])
