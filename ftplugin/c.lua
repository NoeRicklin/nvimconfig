vim.b.buttonfunc = function() 
	vim.cmd("silent w|silent !gcc % -o %:r.exe")
	vim.api.nvim_input(":!./%:r.exe<cr>")
end
