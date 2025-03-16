import pynvim
from time import sleep
from sys import exit
from random import randint

@pynvim.plugin
class welcome:
    def __init__(self, nvim):
        self.nvim = nvim
        self.active_cols = {}

    @pynvim.command("Welcome")
    def initiate(self):
        self.nvim.command("e /tmp/welcome")
        self.nvim.command("silent w")
        self.nvim.command("so /home/noeri/.config/nvim/ftplugin/welcome.vim")
        self.win_height = self.nvim.api.win_get_height(0)
        self.win_width = self.nvim.api.win_get_width(0)

        self.draw_loop()

        self.nvim.command("silent w")
        self.quit()

    def new_image(self):
        self.active_cols[randint(0, self.win_width)] = randint(5, 35)
        new_line = " " * self.win_width
        for col in sorted(self.active_cols):
            new_line = new_line[:col] + chr(randint(32, 64)) + new_line[col+1:]
            self.active_cols[col] -= 1
            if self.active_cols[col] == 0:
                self.active_cols.pop(col)

        self.nvim.api.buf_set_lines(1, 0, 0, False, [new_line])
        self.nvim.api.buf_set_lines(1, self.win_height, self.win_height + 1, False, [])

    def draw_loop(self):
        while (True):
            if str(self.nvim.api.get_current_buf())[15] != "1":
                self.quit()

            self.new_image()

            self.update_cursor()
            self.nvim.command("redraw")
            sleep(0.06)

    def quit(self):
        self.nvim.command("silent bd! 1")
        self.nvim.command("silent !rm /tmp/welcome")
        exit()

    def update_cursor(self):
        cursor = self.nvim.api.win_get_cursor(0)
        cursor[0] -= 1
        self.nvim.api.win_set_cursor(0, cursor)
    
