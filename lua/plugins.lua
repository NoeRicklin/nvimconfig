--TODO: Automatically pull updates

local plugins = {
	"https://github.com/NoeRicklin/nvimStatusline",
	"https://github.com/NoeRicklin/nvimColorscheme",
}

local pluginsPath = vim.fn.stdpath("config") .. "/lua/plugins/"
vim.fn.mkdir(pluginsPath, "p")	-- p flag avoids error when dir exists

for _, url in ipairs(plugins) do
	local pluginName = string.match(url, "[^/]+$")

	pluginExists = #vim.fs.find(pluginName, {
		path = pluginsPath
	}) ~= 0

	if not pluginExists then
		vim.print("Cloning " .. pluginName .. " Plugin")
		vim.fn.system({ "git", "clone", url, pluginsPath .. pluginName })
		vim.print("Done")
	end

	require("plugins/" .. pluginName)
end

