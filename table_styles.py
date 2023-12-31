from arg_parser import TABLE_STYLE

styles = {
	"default": {
		"top_left": "┌",
		"top_right": "┐",
		"bottom_left": "└",
		"bottom_right": "┘",
		"vertical": "│",
		"horizontal": "─",
		"cross": "┼",
		"cross_top": "┬",
		"cross_bottom": "┴",
		"cross_left": "├",
		"cross_right": "┤",
	},
	"double": {
		"top_left": "╔",
		"top_right": "╗",
		"bottom_left": "╚",
		"bottom_right": "╝",
		"vertical": "║",
		"horizontal": "═",
		"cross": "╬",
		"cross_top": "╦",
		"cross_bottom": "╩",
		"cross_left": "╠",
		"cross_right": "╣",
	},
	"ascii": {
		"top_left": "+",
		"top_right": "+",
		"bottom_left": "+",
		"bottom_right": "+",
		"vertical": "|",
		"horizontal": "-",
		"cross": "+",
		"cross_top": "+",
		"cross_bottom": "+",
		"cross_left": "+",
		"cross_right": "+",
	},
	"simple": {
		"top_left": "",
		"top_right": "",
		"bottom_left": "",
		"bottom_right": "",
		"vertical": "",
		"horizontal": "-",
		"cross": "",
		"cross_top": "",
		"cross_bottom": "",
		"cross_left": "",
		"cross_right": "",
	},
	"none": {
		"top_left": "",
		"top_right": "",
		"bottom_left": "",
		"bottom_right": "",
		"vertical": "",
		"horizontal": "",
		"cross": "",
		"cross_top": "",
		"cross_bottom": "",
		"cross_left": "",
		"cross_right": "",
	},

}

ANSI_CODES = {
	"yellow": "\033[1;33m{cell}\033[0m",
	"red": "\033[1;31m{cell}\033[0m",
	"green": "\033[1;32m{cell}\033[0m",
	"blue": "\033[1;34m{cell}\033[0m",
	"magenta": "\033[1;35m{cell}\033[0m",
	"cyan": "\033[1;36m{cell}\033[0m",
	"bold": "\033[1m{cell}\033[0m",
	"reset": "\033[0m{cell}\033[0m"
}


SELECTED_TABLE_STYLE = styles[TABLE_STYLE]