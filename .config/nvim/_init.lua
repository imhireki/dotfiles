
vim.o.termguicolors = true
vim.opt.syntax = "ON"

vim.o.timeoutlen = 500
vim.o.updatetime = 200

vim.o.number = true
vim.o.numberwidth = 2
vim.o.signcolumn = 'yes'
vim.o.cursorline = true

vim.o.expandtab = true
vim.o.smarttab = true
vim.o.cindent = true
vim.o.autoindent = true
vim.o.wrap = true
vim.o.textwidth = 300
vim.o.tabstop = 4
vim.o.shiftwidth = 4
vim.o.softtabstop = -1 -- If negative, shiftwidth value is used
vim.o.list = true
vim.o.listchars = 'trail:·,nbsp:◇,tab:→ ,extends:▸,precedes:◂'

vim.o.clipboard = 'unnamedplus'

vim.o.backup = false
vim.o.writebackup = false
vim.o.undofile = true
vim.o.swapfile = false


vim.o.splitright = true
vim.o.splitbelow = true

vim.opt.mouse = "a"

vim.g.mapleader = ' '
vim.g.maplocalleader = ' '

local ok, _ = pcall(vim.cmd, 'colorscheme dracula')

--BOOTSTRAPPING
local fn = vim.fn
local install_path = fn.stdpath('data')..'/site/pack/packer/start/packer.nvim'
if fn.empty(fn.glob(install_path)) > 0 then
  packer_bootstrap = fn.system({'git', 'clone', '--depth', '1', 'https://github.com/wbthomason/packer.nvim', install_path})
  vim.cmd [[packadd packer.nvim]]
end

-- Plugins
return require('packer').startup(function(use)
use 'wbthomason/packer.nvim'
use 'https://github.com/vim-airline/vim-airline' --Satus bar
use 'https://github.com/vifm/vifm.vim.git' --Vifm file manager
use 'https://github.com/preservim/nerdtree' --File manager
use 'https://github.com/vim-python/python-syntax' --Python syntax
use 'https://github.com/tpope/vim-commentary' --For commentg code (gcc & gc)
use 'https://github.com/preservim/tagbar' --Tagbar for code navigation
use 'https://github.com/tc50cal/vim-terminal' --Terminal
use 'akinsho/toggleterm.nvim' --Open multiple terminals
use 'https://github.com/Yggdroot/indentLine' --Indent line indication
use 'https://github.com/terryma/vim-multiple-cursors' --CTRL + N for multiple cursors
use 'https://github.com/ryanoasis/vim-devicons' --Developer icons
use 'jiangmiao/auto-pairs' --Automatic bracket pairs
--use 'https://github.com/neoclide/coc.nvim' --Autocomplition
use 'https://github.com/ap/vim-css-color.git' 
use 'dracula/vim' --dracula colorscheme
use { 
    'dracula/vim',
  config = function()
    vim.cmd([[colorscheme dracula]])
  end
} -- Dracula colorscheme
use 'https://github.com/rafi/awesome-vim-colorschemes' --More colorschemes
  if packer_bootstrap then
    require('packer').sync()
  end
end)





