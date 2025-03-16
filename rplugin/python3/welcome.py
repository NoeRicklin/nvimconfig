import pynvim
from time import sleep
from sys import exit

@pynvim.plugin
class welcome:
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command("Welcome")
    def welcome(self):
        self.nvim.command("e /tmp/welcome")
        self.nvim.command("silent w")
        self.nvim.command("so /home/noeri/.config/nvim/ftplugin/welcome.vim")
        win_height = self.nvim.api.win_get_height(0)

        for i in range(50):
            if str(self.nvim.api.get_current_buf())[15] != "1":
                self.nvim.command("silent bd! 1")
                self.nvim.command("silent !rm /tmp/welcome")
                exit()
            self.nvim.api.buf_set_lines(0, 0, 0, False, [f"{i}"])
            self.nvim.api.buf_set_lines(0, win_height, win_height + 1, False, [])
            self.nvim.command("redraw")

            cursor = self.nvim.api.win_get_cursor(0)
            cursor[0] -= 1
            self.nvim.api.win_set_cursor(0, cursor)

            sleep(0.1)
        self.nvim.command("silent w")

