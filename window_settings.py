import tkinter


class Change_window_settings_interface:

    """class for changing the settings of the window"""

    def __init__(self):

        self.window = tkinter.Tk()
        self.window.geometry("400x400")
        self.window.configure(background = "grey")



        self.settings_label = tkinter.Label(self.window, text = "Settings", font = ("SimSun", 20))
        self.settings_label.grid(row = 1, column = 1, columnspan = 3)

        font = ("SimSun", 10)
        width = 30
        self.window_width_label = tkinter.Label(self.window, text = "Window Width:", font = font, width = width)
        self.window_width_label.grid(row = 2, column = 1)
        self.window_width_entry = tkinter.Entry(self.window)
        self.window_width_entry.grid(row = 2, column = 2)


        self.window_height_label = tkinter.Label(self.window, text = "Window Height:", font = font, width = width)
        self.window_height_label.grid(row = 3, column = 1)
        self.window_height_entry = tkinter.Entry(self.window)
        self.window_height_entry.grid(row = 3, column = 2)


        self.grid_width_label = tkinter.Label(self.window, text = "Grid Square Size:", font = font, width = width)
        self.grid_width_label.grid(row = 4, column = 1)
        self.grid_width_entry = tkinter.Entry(self.window)
        self.grid_width_entry.grid(row = 4, column = 2)


        self.grid_pad_label = tkinter.Label(self.window, text = "Grid Square Pad:", font = font, width = width)
        self.grid_pad_label.grid(row = 5, column = 1)
        self.grid_pad_entry = tkinter.Entry(self.window)
        self.grid_pad_entry.grid(row = 5, column = 2)

        self.algorithm_search_delay_label = tkinter.Label(self.window, text = "Algorithm Search Delay:", font = font, width = width)
        self.algorithm_search_delay_label.grid(row = 6, column = 1)
        self.algorithm_search_delay_entry = tkinter.Entry(self.window)
        self.algorithm_search_delay_entry.grid(row = 6, column = 2)

        self.algorithm_backtrack_delay_label = tkinter.Label(self.window, text = "Algorithm Backtrack Delay:", font = font, width = width)
        self.algorithm_backtrack_delay_label.grid(row = 7, column = 1)
        self.algorithm_backtrack_delay_entry = tkinter.Entry(self.window)
        self.algorithm_backtrack_delay_entry.grid(row = 7, column = 2)


        self.fps_label = tkinter.Label(self.window, text = "FPS:", font = font, width = width)
        self.fps_label.grid(row = 8, column = 1)
        self.fps_entry = tkinter.Entry(self.window)
        self.fps_entry.grid(row = 8, column = 2)




        self.save_button = tkinter.Button(self.window, text = "Save", width = width, command = self.update_settings)
        self.save_button.grid(row = 9, column = 1, columnspan = 2)




        self.entrys = [self.window_width_entry, self.window_height_entry, self.grid_width_entry, self.grid_pad_entry, self.algorithm_search_delay_entry, self.algorithm_backtrack_delay_entry, self.fps_entry]

        settings = self.read_settings()


        x = 0
        while x < len(self.entrys):

            self.entrys[x].insert(0, settings[x])
            x += 1








        self.window.bind("<Return>", self.update_settings)

        self.window.mainloop()







    def update_settings(self, e = 0):

        f = open("settings.txt", "w")


        values = [self.window_width_entry.get(), self.window_height_entry.get(), self.grid_width_entry.get(), self.grid_pad_entry.get(), self.algorithm_search_delay_entry.get(), self.algorithm_backtrack_delay_entry.get(), self.fps_entry.get()]

        for value in values:
            print(value)

            f.write(str(value) + "\n")



        f.close()




    def read_settings(self):

        f = open("settings.txt", "r")

        content = f.readlines()

        x = 0
        while x < len(content):

            new_value = str(content[x]).rstrip("\n")
            content[x] = new_value

            x += 1

        print(content)
        f.close()

        return content








#
