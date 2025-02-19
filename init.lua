vim.g.mapleader = " "
vim.g.maplocalleader = " "

vim.opt.number = true
vim.opt.relativenumber = true

vim.opt.ruler = false
vim.opt.showmode = false

vim.keymap.set("n", "-", function() vim.cmd("Ex") end, { desc = "Open parent directory of current file" })

vim.keymap.set("i", "<M-o>", function ()
	cur_line = vim.api.nvim_win_get_cursor(0)[1]
	vim.api.nvim_buf_set_lines(0, cur_line, cur_line, false, { "" })
    end,
    { desc = "Create empty line below current one" }
)

vim.api.nvim_create_augroup("shiftwidth", { clear = true })
vim.api.nvim_create_autocmd("BufEnter", {
    pattern = "*.lua",
    group = "shiftwidth",
    callback = function() vim.opt.shiftwidth = 4 end,
    desc = "Set shiftwidth to 4 spaces when opening a *.lua file"
})

