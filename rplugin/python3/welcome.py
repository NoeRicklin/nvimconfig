# Don't show cursor / remove flickering
# More control for settings like color and speed

# Check out: scratch-buffer, noswapfile, bufhidden=delete

import pynvim
from time import sleep
from random import randint

@pynvim.plugin
class welcome:
    def __init__(self, nvim):
        self.nvim = nvim
        self.active_cols = {}
        self.running = False

    @pynvim.command("Welcome")
    def initiate(self):
        if self.running:
            return

        self.welc_buf = self.nvim.api.create_buf(False, False)
        self.welc_buf.options["filetype"] = "welcome"
        self.welc_buf.options["buftype"] = "nowrite"

        self.win_ops = {"relative": "editor",
                        "row": 0,
                        "col": 0,
                        "width": 1,
                        "height": 1,
                        "focusable": False,
                        "style": "minimal"}

        self.running = True
        self.welc_win = self.nvim.api.open_win(self.welc_buf, False, self.win_ops)
        self.reset_win_size()

        self.welc_ns = self.nvim.api.create_namespace("WelcomeFloat")
        self.nvim.api.set_hl(self.welc_ns, "Pmenu", {"ctermbg": ""})
        self.nvim.api.win_set_hl_ns(self.welc_win, self.welc_ns)

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

        self.nvim.api.buf_set_lines(self.welc_buf, 0, 0, False, [new_line])
        self.nvim.api.buf_set_lines(self.welc_buf, self.win_height, len(self.welc_buf) + 1, False, [])

    def draw_loop(self):
        while (self.running):
            self.new_image()

            self.nvim.command("redraw")
            sleep(0.06)
        self.nvim.api.buf_delete(self.welc_buf, {})

    @pynvim.command("QuitWelcome")
    def quit(self):
        self.running = False

    @pynvim.autocmd("VimResized")
    def reset_win_size(self):
        if not self.running:
            return
        self.win_width = self.nvim.api.win_get_width(0)
        self.win_height = self.nvim.api.win_get_height(0) + 1

        self.nvim.api.win_set_width(self.welc_win, self.win_width)
        self.nvim.api.win_set_height(self.welc_win, self.win_height)

        self.nvim.api.win_set_cursor(self.welc_win, [1, 0])

    @pynvim.autocmd("BufNew,InsertEnter")
    def quit_out(self):
        if self.running:
            self.quit()

