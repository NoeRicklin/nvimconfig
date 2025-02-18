vim.g.mapleader = " "
vim.g.maplocalleader = " "

vim.opt.number = true
vim.opt.relativenumber = false

vim.keymap.set("n", "-", function() vim.cmd("Ex") end, { desc = "Open parent directory of current file" })

vim.api.nvim_create_augroup("shiftwidth", { clear = true })
vim.api.nvim_create_autocmd("BufEnter", {
  pattern = "*.lua",
  group = "shiftwidth",
  callback = function() vim.opt.shiftwidth = 2 end,
  desc = "Set shiftwidth to 2 spaces when opening a *.lua file"
})
