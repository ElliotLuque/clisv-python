import os
from arg_parser import ALIGNMENT
from table_styles import ANSI_CODES

def pad(source_str, dir, char, len):
	"""Pads (source_str) with (char) to (len) length in (dir) direction
	
	Args:
		source_str (str): string to pad
		dir (str): direction of padding [left, right]
		char (str): character to pad with
		len (int): length of padding
	
	Returns:
		str: padded string
	"""
	str = char * len

	if dir == "right":
		str += source_str
		return str
	else: 
		return source_str + char * len
	
def stylize(str, style):
	"""Stylizes (str) with (style)
	
	Args:
		str (str): string to stylize
		style (str): style to apply [color, bold, reset]

	Returns:
		str: stylized string
	"""
	if os.isatty(1):
		return ANSI_CODES[style].format(cell=str)
	else:
		return str

def max_col_length(table, col_number):
	"""Returns length of longest string in column (col_number) of (table)

	Args:
		table (list): table to search
		col_number (int): number of column to search

	Returns:
		int: length of longest string in column
	"""
	max = 0
	for i in range(len(table)):
		if max < len(table[i][col_number]):
			max = len(table[i][col_number]) 
	return max	

def cell_padding(table):
	"""Pads all cells in (table) to equal length
	
	Args:
		table (list): table to pad
	"""
	for i in range(len(table)):
		for j in range(len(table[i])):
			table[i][j] = pad(table[i][j], ALIGNMENT, " ", max_col_length(table, j) - len(table[i][j]))