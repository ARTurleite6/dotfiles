local wezterm = require("wezterm")
local action = wezterm.action

local config = {
	default_domain = "WSL:Ubuntu",
	inactive_pane_hsb = {
		saturation = 0.8,
		brightness = 0.7,
	},
	default_cursor_style = "BlinkingBar",
	font = wezterm.font("JetBrains Mono"),
	color_scheme = "Gruvbox dark, hard (base16)",
	use_dead_keys = false,
	scrollback_lines = 5000,
	adjust_window_size_when_changing_font_size = false,
	hide_tab_bar_if_only_one_tab = true,
	disable_default_key_bindings = true,
	leader = { key = "b", mods = "CTRL", timeout_milliseconds = 2000 },
	keys = {
		{ key = "p", mods = "CTRL|SHIFT", action = action.ActivateCommandPalette },
		{ key = "c", mods = "LEADER", action = action.SpawnTab("CurrentPaneDomain") },
		{ key = "q", mods = "LEADER", action = action.CloseCurrentPane({ confirm = false }) },
		{ key = "c", mods = "CTRL|SHIFT", action = action.CopyTo("Clipboard") },
		{ key = "v", mods = "CTRL|SHIFT", action = action.PasteFrom("Clipboard") },
		{ key = "|", mods = "LEADER", action = action.SplitHorizontal({ domain = "CurrentPaneDomain" }) },
		{ key = "_", mods = "LEADER", action = action.SplitVertical({ domain = "CurrentPaneDomain" }) },
		{ key = "k", mods = "LEADER", action = action.ActivatePaneDirection("Up") },
		{ key = "j", mods = "LEADER", action = action.ActivatePaneDirection("Down") },
		{ key = "h", mods = "LEADER", action = action.ActivatePaneDirection("Left") },
		{ key = "l", mods = "LEADER", action = action.ActivatePaneDirection("Right") },
		{ key = "n", mods = "LEADER", action = action.ActivateTabRelative(1) },
		{ key = "p", mods = "LEADER", action = action.ActivateTabRelative(-1) },
		{ key = "Enter", mods = "LEADER", action = action.ActivateCopyMode },
		{ key = "+", mods = "CTRL|SHIFT", action = action.IncreaseFontSize },
		{ key = "-", mods = "CTRL|SHIFT", action = action.DecreaseFontSize },
		{ key = "0", mods = "CTRL|SHIFT", action = action.ResetFontSize },
	},
}

return config
