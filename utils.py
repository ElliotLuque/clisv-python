from arg_parser import ALIGNMENT

def pad(source_string, dir, char, pad):
	if dir == "right":
		str = char * pad
		str += source_string
		return str
	elif dir == "center":
		str = char * pad
		str += source_string
		str += char * pad
		return str
	else: 
		return source_string + char * pad
	
def stylize(str, collection, style):
	return collection[style].format(cell=str)

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