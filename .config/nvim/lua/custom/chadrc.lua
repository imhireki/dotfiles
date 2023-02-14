-- First read our docs (completely) then check the example_config repo

local M = {}

M.ui = {
  changed_themes = {
    catppuccin = {
      base_30 = {
        grey_fg = "#FAE3B0",
      }
    },
  },
  theme = "catppuccin",
  transparency = true,
}

return M
