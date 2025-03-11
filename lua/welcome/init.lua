local start_buf = vim.api.nvim_get_current_buf()
vim.api.nvim_buf_set_lines(start_buf, 0, 1, true, {
	"   __   ",
	" -/  \\- ",
	"/      \\",
	"|      |",
	"\\      /",
	" -\\   /-",
	"   ---  "
})
