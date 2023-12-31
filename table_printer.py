from utils import stylize, max_col_length, cell_padding
from arg_parser import IS_BOLD, COLOR
from table_styles import SELECTED_TABLE_STYLE, ANSI_CODES

def table_header(header_row):
	row = header_row['row']
	weights = header_row['weights']
	str = f"{SELECTED_TABLE_STYLE['top_left']}"

	# First line
	for i in range(len(row)):
		str += f"{SELECTED_TABLE_STYLE['horizontal'] * (weights[i] + 2)}"
		if i < len(row) - 1:
			str += f"{SELECTED_TABLE_STYLE['cross_top']}"
		else:
			str += f"{SELECTED_TABLE_STYLE['top_right']}\n"

	# Second line
	str += f"{SELECTED_TABLE_STYLE['vertical']}"
	for i in range(len(row)):
		str += f" {stylize(row[i], ANSI_CODES, 'bold' if IS_BOLD else 'reset')} "
		if i < len(row):
			str += f"{SELECTED_TABLE_STYLE['vertical']}"
	
	# Third line
	str += f"\n{SELECTED_TABLE_STYLE['cross_left']}"
	for i in range(len(row)):
		str += f"{SELECTED_TABLE_STYLE['horizontal'] * (weights[i] + 2)}"
		if i < len(row) - 1:
			str += f"{SELECTED_TABLE_STYLE['cross']}"
		else:
			str += f"{SELECTED_TABLE_STYLE['cross_right']}"

	return str

def table_row(row):
	str = f"{SELECTED_TABLE_STYLE['vertical']}"
	for cell in row:
		str += f" {stylize(cell, ANSI_CODES, COLOR)} {SELECTED_TABLE_STYLE['vertical']}"
	return str

def last_row(header_weights):
	str = f"{SELECTED_TABLE_STYLE['bottom_left']}"
	for i in range(len(header_weights)):
		str += f"{SELECTED_TABLE_STYLE['horizontal'] * (header_weights[i] + 2)}"
		if i < len(header_weights) - 1:
			str += f"{SELECTED_TABLE_STYLE['cross_bottom']}"
		else:
			str += f"{SELECTED_TABLE_STYLE['bottom_right']}"
	return str

def print_table(table):
	# Initialize cells
	cell_padding(table)

	# Print table
	for i in range(len(table)):
		header_row = {
			"row": table[i],
			"weights": [max_col_length(table, j) for j in range(len(table[i]))]
		}
		if i == 0:
			print(table_header(header_row))
		else:
			print(table_row(table[i]))

	print(last_row(header_row['weights']))