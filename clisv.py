import sys
import csv
import argparse

parser = argparse.ArgumentParser(description='Prints csv file as table in console')
parser.add_argument('file', metavar='file', type=str, help='csv file to print')
parser.add_argument('--align', metavar='alignment', type=str, help='alignment of table elements')
parser.add_argument('--color', metavar='color', type=str, help='color of table elements')
parser.add_argument('--delimiter', metavar='delimiter', type=str, help='delimiter of csv file')
parser.add_argument('--bold', metavar='bold', type=bool, help='bold table header')
parser.add_argument('--indexed', action='store_true', help='add index column')
args = parser.parse_args()

ALIGNMENT = args.align if args.align else "left"
COLOR = args.color if args.color else "reset"
DELIMITER = args.delimiter if args.delimiter else ";"
BOLD = args.bold if args.bold else False
INDEXED = args.indexed if args.indexed else False

input = args.file
table_chars = {
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
table_styles = {
	"yellow": "\033[1;33m{cell}\033[0m",
	"red": "\033[1;31m{cell}\033[0m",
	"green": "\033[1;32m{cell}\033[0m",
	"blue": "\033[1;34m{cell}\033[0m",
	"bold": "\033[1m{cell}\033[0m",
	"reset": "\033[0m{cell}\033[0m"
}

table = []

def table_header(header_row):
	row = header_row['row']
	weights = header_row['weights']
	str = f"{table_chars['top_left']}"

	# First line
	for i in range(len(row)):
		str += f"{table_chars['horizontal'] * (weights[i] + 2)}"
		if i < len(row) - 1:
			str += f"{table_chars['cross_top']}"
		else:
			str += f"{table_chars['top_right']}\n"

	# Second line
	str += f"{table_chars['vertical']}"
	for i in range(len(row)):
		str += f" {stylize(row[i], table_styles, 'bold' if BOLD else 'reset')} "
		if i < len(row):
			str += f"{table_chars['vertical']}"
	
	# Third line
	str += f"\n{table_chars['cross_left']}"
	for i in range(len(row)):
		str += f"{table_chars['horizontal'] * (weights[i] + 2)}"
		if i < len(row) - 1:
			str += f"{table_chars['cross']}"
		else:
			str += f"{table_chars['cross_right']}"

	return str

def table_row(row):
	str = f"{table_chars['vertical']}"
	for cell in row:
		str += f" {stylize(cell, table_styles, COLOR)} {table_chars['vertical']}"
	return str

def last_row(header_weights):
	str = f"{table_chars['bottom_left']}"
	for i in range(len(header_weights)):
		str += f"{table_chars['horizontal'] * (header_weights[i] + 2)}"
		if i < len(header_weights) - 1:
			str += f"{table_chars['cross_bottom']}"
		else:
			str += f"{table_chars['bottom_right']}"
	return str

def cell_padding(table):
	for i in range(len(table)):
		for j in range(len(table[i])):
			table[i][j] = pad(table[i][j], ALIGNMENT, " ", max_col_length(table, j) - len(table[i][j]))

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

def stylize(str, collection,style):
	return collection[style].format(cell=str)

def pad(source_string, dir, char, pad):
	if dir == "right":
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

	with open(input, 'r', encoding='utf-8') as file:
		reader = csv.reader(file, delimiter=DELIMITER)
		for row in reader:
			if not row:
				continue
			table.append(row)
	
	if INDEXED:
		for i in range(len(table)):
			if i == 0:
				table[i].insert(0, "(index)")
			else:
				table[i].insert(0, str(i))

	cell_padding(table)
	print_table(table)


except IOError:
	print(f"File {input} not found")
	sys.exit(1)

