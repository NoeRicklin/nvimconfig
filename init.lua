vim.g.mapleader = " "
vim.g.maplocalleader = " "

vim.opt.number = true
vim.opt.relativenumber = false

vim.keymap.set("n", "-", function() vim.cmd("Ex") end, { desc = "Open parent directory of current file" })
