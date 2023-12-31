import os
from arg_parser import ALIGNMENT, MAX_ELEMENT_LENGTH
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

def format_cells(table):
	"""Format all cells in (table) depending on ALIGNMENT and MAX_LENGTH
	
	Args:
		table (list): table to format
	"""
	for i in range(len(table)):
		for j in range(len(table[i])):
			# Truncate cell if its too long
			if len(table[i][j]) > MAX_ELEMENT_LENGTH and MAX_ELEMENT_LENGTH > 0:
				table[i][j] = table[i][j][:MAX_ELEMENT_LENGTH] + "…"

			# Pad cell if its too short
			if MAX_ELEMENT_LENGTH <= 0:
				table[i][j] = pad(table[i][j], ALIGNMENT, " ", max_col_length(table, j) - len(table[i][j]))
			else:
				table[i][j] = pad(table[i][j], ALIGNMENT, " ", MAX_ELEMENT_LENGTH + 1 - len(table[i][j]))
