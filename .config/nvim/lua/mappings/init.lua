local map = vim.api.nvim_set_keymap
local opts = { noremap = true, silent = true }

vim.g.mapleader = ' '

map('n', '<leader>t', ':NvimTreeToggle<CR>', opts)

map('n', '<leader>bp', ':BufferPrevious<CR>', opts)
map('n', '<leader>bn', ':BufferNext<CR>', opts)
map('n', '<leader>bk', ':BufferClose<CR>', opts)

map('n', '<leader>b1', ':BufferGoto 1<CR>', opts)
map('n', '<leader>b2', ':BufferGoto 2<CR>', opts)
map('n', '<leader>b3', ':BufferGoto 3<CR>', opts)
map('n', '<leader>b4', ':BufferGoto 4<CR>', opts)
map('n', '<leader>b5', ':BufferGoto 5<CR>', opts)
map('n', '<leader>b6', ':BufferGoto 6<CR>', opts)
map('n', '<leader>b7', ':BufferGoto 7<CR>', opts)
map('n', '<leader>b8', ':BufferGoto 8<CR>', opts)
map('n', '<leader>b9', ':BufferGoto 9<CR>', opts)

map('n', '<leader>ff', ':Telescope find_files<CR>', opts)
map('n', '<leader>fg', ':Telescope live_grep<CR>', opts)


