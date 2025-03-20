-- [digit].[digit] sets the minimal width and maximal width of the tag. Here the minimal width
-- is set to one larger than the actual width of the tag that only display sometimes, to space
-- them apart from other tags, but not having to add a literal <space>, which would lead to
-- undesirable spacing
local mode = "%{toupper(mode())}"
local filename = "%f"
local help_file = "%7.h"
local read_only = "%5.r"
local unsaved_changes = "%4.m"
local buttonfunction = " %@v:lua.buttoncaller@"
local buttonclose = "%T"
local split = "%="
local file_lines = "Lines: %L"
local cur_line = "%l"
local cur_column = "%v"
local percentage = "%P"

user1_hl = {}
user1_hl["ctermfg"] = "white"
user1_hl["ctermbg"] = "white"
vim.api.nvim_set_hl(0, "User1", user1_hl)
vim.cmd("hi StatusLine ctermfg=White")

local hi_norm = "%#StatusLine#"
local hi_hide = "%#User1#"

local left_side = mode .. help_file..read_only..unsaved_changes
local center = buttonfunction..filename..buttonclose
local right_side = "%<" .. cur_line..":"..cur_column.." ("..percentage..")".." - "..file_lines

vim.opt.statusline=hi_norm..left_side..hi_hide..right_side..hi_norm..split..center..split..hi_hide..left_side..hi_norm..right_side

buttoncaller = function() vim.b.buttonfunc() end

vim.api.nvim_create_augroup("buttonfunc group", { clear = true })
vim.api.nvim_create_autocmd("BufEnter", {
	group = "buttonfunc group",
	callback = function()
		if vim.b.buttonfunc == nil then
			vim.b.buttonfunc = function() vim.cmd("w") end
		end
	end,
	desc = "Default behaviour of statusline button"
})

