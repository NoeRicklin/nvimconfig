import pynvim
from time import sleep
from pynvim import Nvim

@pynvim.plugin
class welcome:
    def __init__(self, nvim: Nvim):
        self.nvim = nvim

    @pynvim.command("Welcome")
    def welcome(self):
        for i in range(5):
            self.nvim.command(f"echo '{i}'")
            sleep(1)

