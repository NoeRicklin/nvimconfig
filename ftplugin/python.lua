cur_file_path = vim.api.nvim_buf_get_name(0)
python_file = "test_.*%.py"

if string.match(cur_file_path, python_file) then
    test_file_path = vim.fn.findfile("test.sh", cur_file_path .. ";")
    current_directory = vim.fn.getcwd()
    vim.b.buttonfunc = function() vim.cmd("w|!" .. current_directory .. "/" .. test_file_path) end
end
