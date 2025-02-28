vim.g.mapleader = " "
vim.g.maplocalleader = " "

vim.opt.number = true
vim.opt.relativenumber = true

vim.opt.ruler = false
vim.opt.showmode = false
vim.opt.wrap = false
vim.opt.splitright = true

vim.opt.tabstop = 4
vim.opt.shiftwidth = 4

vim.keymap.set("n", "<M-h>", "<C-w>h", { desc = "Move to left window" })
vim.keymap.set("n", "<M-j>", "<C-w>j", { desc = "Move to bottom window" })
vim.keymap.set("n", "<M-k>", "<C-w>k", { desc = "Move to top window" })
vim.keymap.set("n", "<M-l>", "<C-w>l", { desc = "Move to right window" })

vim.keymap.set("n", "-", function() vim.cmd("Ex") end, { desc = "Open parent directory of current file" })

vim.keymap.set("i", "<M-o>", function ()
		cur_line = vim.api.nvim_win_get_cursor(0)[1]
		vim.api.nvim_buf_set_lines(0, cur_line, cur_line, false, { "" })
    end,
    { desc = "Create empty line below current one" }
)

vim.api.nvim_create_augroup("yank_hl", { clear = true })
vim.api.nvim_create_autocmd("TextYankPost", {
	group = "yank_hl",
	callback = function()
		vim.highlight.on_yank({ timeout = 150 })
	end,
	desc = "Highlights yanked text"
})
