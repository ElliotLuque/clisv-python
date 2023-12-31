from utils import stylize, max_col_length, cell_padding
from arg_parser import IS_BOLD, COLOR
from table_styles import SELECTED_TABLE_STYLE, ANSI_CODES

def table_header(header_row):
	"""Returns a string containing the header of the table

	Args:
		header_row (dict): dictionary containing header row and weights (cell lengths)
	"""
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
		str += f" {stylize(row[i], 'bold' if IS_BOLD else 'reset')} "
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
	"""Returns a string containing a single row of the table

	Args:
		row (list): row to print
	"""
	str = f"{SELECTED_TABLE_STYLE['vertical']}"
	for cell in row:
		str += f" {stylize(cell, COLOR)} {SELECTED_TABLE_STYLE['vertical']}"
	return str

def last_row(header_weights):
	"""Returns a string containing the last line of the table (bottom border)

	Args:
		header_weights (list): list of header cell lengths
	"""
	str = f"{SELECTED_TABLE_STYLE['bottom_left']}"
	for i in range(len(header_weights)):
		str += f"{SELECTED_TABLE_STYLE['horizontal'] * (header_weights[i] + 2)}"
		if i < len(header_weights) - 1:
			str += f"{SELECTED_TABLE_STYLE['cross_bottom']}"
		else:
			str += f"{SELECTED_TABLE_STYLE['bottom_right']}"
	return str

def print_table(table):
	"""Prints a csv with table format to console

	Args:
		table (list): table containing csv contents to print
	"""
	# Initialize cells
	cell_padding(table)

	# Print table
	for i in range(len(table)):
		if i == 0:
			header_row = {
				"row": table[i],
				"weights": [max_col_length(table, j) for j in range(len(table[i]))]
			}
			print(table_header(header_row))
		else:
			print(table_row(table[i]))

	print(last_row(header_row['weights']))