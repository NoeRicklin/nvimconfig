file_path = vim.api.nvim_buf_get_name(0)
config_path = vim.fn.stdpath("config")

-- Checks if lua script is a config file
if string.match(file_path, config_path) then
    vim.b.buttonfunc = function() vim.cmd("w|so") end
end
