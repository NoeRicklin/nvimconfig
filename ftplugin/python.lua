cur_file_path = vim.api.nvim_buf_get_name(0)
test_file_pattern = "test_.*%.py"

if string.match(cur_file_path, test_file_pattern) then
    test_file_path = vim.fn.findfile("test.sh", cur_file_path .. ";")
    current_directory = vim.fn.getcwd()
    vim.b.buttonfunc = function() vim.cmd("w|!" .. current_directory .. "/" .. test_file_path) end
else
	vim.b.buttonfunc = function() vim.cmd("silent w|!python3 %") end
end
