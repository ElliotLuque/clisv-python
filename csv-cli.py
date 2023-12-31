import sys

input = sys.argv[1]
table_headers = []

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

def build_table_headers(headers):
	str = f"{t_chars['top_left']}"

	# First line
	for i in range(len(headers)):
		str += f"{t_chars['horizontal'] * (len(headers[i]) + 2)}"
		if i < len(headers) - 1:
			str += f"{t_chars['cross_top']}"
		else:
			str += f"{t_chars['top_right']}\n"
			
	# Second line
	str += f"{t_chars['vertical']}"
	for i in range(len(headers)):
		str += f" {headers[i]} "
		if i < len(headers):
			str += f"{t_chars['vertical']}"		
	
	# Third line
	str += f"\n{t_chars['cross_left']}"
	for i in range(len(headers)):
		str += f"{t_chars['horizontal'] * (len(headers[i]) + 2)}"
		if i < len(headers) - 1:
			str += f"{t_chars['cross']}"
		else:
			str += f"{t_chars['cross_right']}\n"

	return str
	
def build_table_rows(rows):
	pass

try:
	row_count = 0

	with open(input, "r") as file:
		for line in file:
			if row_count == 0:
				line = line.strip()
				table_headers = line.split(";")
			row_count += 1

	print(build_table_headers(table_headers))

except IOError:
	print(f"File {input} not found")
	sys.exit(1)

