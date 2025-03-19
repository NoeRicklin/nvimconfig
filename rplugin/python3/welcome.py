# Shouldn't be able to edit file
# Should be able to restart welcome screen on command
# Error on opening 2nd nvim instance with welcome active on 1st
# Weird behaviour when opening nvim with a file
# Don't show cursor / remove flickering
# Error when cursor moves out of range
# More control for settings like color and speed

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
        self.nvim.command("e welcome")
        # self.nvim.command("so /home/noeri/.config/nvim/ftplugin/welcome.vim")
        self.nvim.command("setlocal buftype=nowrite")
        self.welcome_buf = self.nvim.current.buffer
        self.set_win_size()
        
        self.draw_loop()

        self.quit()

    def new_image(self):
        self.active_cols[randint(0, self.win_width)] = randint(5, 35)
        new_line = " " * self.win_width
        for col in sorted(self.active_cols):
            new_line = new_line[:col] + chr(randint(32, 64)) + new_line[col+1:]
            self.active_cols[col] -= 1
            if self.active_cols[col] == 0:
                self.active_cols.pop(col)

        self.welcome_buf[0:0] = [new_line]
        # self.nvim.api.buf_set_lines(self.welcome_buf.number, 0, 0, False, [new_line])
        if len(self.welcome_buf) > self.win_height:
            del(self.welcome_buf[self.win_height])

    def draw_loop(self):
        while (True):
            if self.nvim.current.buffer != self.welcome_buf:
                self.quit()

            self.new_image()

            self.update_cursor()
            self.nvim.command("redraw")
            sleep(0.06)

    def quit(self):
        self.nvim.command(f"silent bd! {self.welcome_buf.number}")
        exit()

    def update_cursor(self):
        cur_cursor = self.nvim.current.window.cursor
        new_cursor = (cur_cursor[0] - 1, cur_cursor[1])
        self.nvim.current.window.cursor = new_cursor
    
    @pynvim.autocmd("VimResized", pattern="welcome")
    def set_win_size(self):
        self.win_height = self.nvim.api.win_get_height(0)
        self.win_width = self.nvim.api.win_get_width(0)


