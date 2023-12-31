import sys

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

table_header = []
table_rows = []

def build_table_header(header):
	str = f"{t_chars['top_left']}"

	# First line
	for i in range(len(header)):
		str += f"{t_chars['horizontal'] * (len(header[i]) + 2)}"
		if i < len(header) - 1:
			str += f"{t_chars['cross_top']}"
		else:
			str += f"{t_chars['top_right']}\n"
			
	# Second line
	str += f"{t_chars['vertical']}"
	for i in range(len(header)):
		str += f" {header[i]} "
		if i < len(header):
			str += f"{t_chars['vertical']}"		
	
	# Third line
	str += f"\n{t_chars['cross_left']}"
	for i in range(len(header)):
		str += f"{t_chars['horizontal'] * (len(header[i]) + 2)}"
		if i < len(header) - 1:
			str += f"{t_chars['cross']}"
		else:
			str += f"{t_chars['cross_right']}"

	return str
	
def build_table_row(row):
	str = f"{t_chars['vertical']}"
	for cell in row:
		str += f"\033[1;33m {cell} \033[0m{t_chars['vertical']}"
	return str

def build_table_row_last(header):
	str = f"{t_chars['bottom_left']}"
	for i in range(len(header)):
		str += f"{t_chars['horizontal'] * (len(header[i]) + 2)}"
		if i < len(header) - 1:
			str += f"{t_chars['cross_bottom']}"
		else:
			str += f"{t_chars['bottom_right']}"
	return str

def build_table(header, rows):
	print(build_table_header(header))
	
	for row in rows:
		print(build_table_row(row))
	print(build_table_row_last(header))

def pad(source_string, dir, char, pad):
	if dir == "left":
		str = char * pad
		str += source_string
		return str
	else: 
		return source_string + char * pad

try:
	row_count = 0

	with open(input, "r") as file:
		for line in file:
			line = line.strip()

			if not line:
				continue

			if row_count == 0:
				table_header = line.split(";")
			else:
				table_rows.append(line.split(";"))
			row_count += 1

	build_table(table_header, table_rows)

except IOError:
	print(f"File {input} not found")
	sys.exit(1)

