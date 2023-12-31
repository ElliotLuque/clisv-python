import os
from arg_parser import ALIGNMENT

def pad(source_str, dir, char, len):
	str = char * len

	if dir == "right":
		str += source_str
		return str
	else: 
		return source_str + char * len
	
def stylize(str, collection, style):
	if os.isatty(1):
		return collection[style].format(cell=str)
	else:
		return str

def max_col_length(table, col_number):
	max = 0
	for i in range(len(table)):
		if max < len(table[i][col_number]):
			max = len(table[i][col_number]) 
	return max	

def cell_padding(table):
	for i in range(len(table)):
		for j in range(len(table[i])):
			table[i][j] = pad(table[i][j], ALIGNMENT, " ", max_col_length(table, j) - len(table[i][j]))