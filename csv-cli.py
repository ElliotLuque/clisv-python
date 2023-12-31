import sys
import csv

input = sys.argv[1]
t_chars = {
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
}

table = []

def table_header(header_row):
	row = header_row['row']
	weights = header_row['weights']
	str = f"{t_chars['top_left']}"

	# First line
	for i in range(len(row)):
		str += f"{t_chars['horizontal'] * (weights[i] + 2)}"
		if i < len(row) - 1:
			str += f"{t_chars['cross_top']}"
		else:
			str += f"{t_chars['top_right']}\n"

	# Second line
	str += f"{t_chars['vertical']}"
	for i in range(len(row)):
		str += f" {row[i]} "
		if i < len(row):
			str += f"{t_chars['vertical']}"
	
	# Third line
	str += f"\n{t_chars['cross_left']}"
	for i in range(len(row)):
		str += f"{t_chars['horizontal'] * (weights[i] + 2)}"
		if i < len(row) - 1:
			str += f"{t_chars['cross']}"
		else:
			str += f"{t_chars['cross_right']}"

	return str

def table_row(row):
	str = f"{t_chars['vertical']}"
	for cell in row:
		str += f" {cell} {t_chars['vertical']}"
	return str

def last_row(header_weights):
	str = f"{t_chars['bottom_left']}"
	for i in range(len(header_weights)):
		str += f"{t_chars['horizontal'] * (header_weights[i] + 2)}"
		if i < len(header_weights) - 1:
			str += f"{t_chars['cross_bottom']}"
		else:
			str += f"{t_chars['bottom_right']}"
	return str

def cell_padding(table):
	for i in range(len(table)):
		for j in range(len(table[i])):
			table[i][j] = pad(table[i][j], "right", " ", max_col_length(table, j) - len(table[i][j]))

def print_table(table):
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
		
def max_col_length(table, col_number):
	max = 0
	for i in range(len(table)):
		if max < len(table[i][col_number]):
			max = len(table[i][col_number]) 
	return max			

def pad(source_string, dir, char, pad):
	if dir == "left":
		str = char * pad
		str += source_string
		return str
	elif dir == "both":
		str = char * pad
		str += source_string
		str += char * pad
		return str
	else: 
		return source_string + char * pad

try:
	row_count = 0

	with open(input, 'r') as file:
		reader = csv.reader(file, delimiter=';')
		for row in reader:
			if not row:
				continue
			table.append(row)
	
	cell_padding(table)
	print_table(table)


except IOError:
	print(f"File {input} not found")
	sys.exit(1)

