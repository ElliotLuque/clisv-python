import sys

input = sys.argv[1]
table_headers = {
	"names": [],
	"lengths": []
}

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

def square_text(text):
	text_length = len(text)
	
	str = f"{t_chars['top_left']}{t_chars['horizontal'] * (text_length + 2)}{t_chars['top_right']}\n"
	str += f"{t_chars['vertical']} {text} {t_chars['vertical']}\n"
	str += f"{t_chars['bottom_left']}{t_chars['horizontal'] * (text_length + 2)}{t_chars['bottom_right']}\n"
	
	return str

def build_table_headers(headers):
	str = f"{t_chars['top_left']}"

	# First line
	for i in range(len(headers["names"])):
		str += f"{t_chars['horizontal'] * (headers['lengths'][i] + 2)}"
		if i < len(headers["names"]) - 1:
			str += f"{t_chars['cross_top']}"
		else:
			str += f"{t_chars['top_right']}\n"
			
	# Second line
	str += f"{t_chars['vertical']}"
	for i in range(len(headers["names"])):
		str += f" {headers['names'][i]} "
		if i < len(headers["names"]):
			str += f"{t_chars['vertical']}"		
	
	# Third line
	str += f"\n{t_chars['cross_left']}"
	for i in range(len(headers["names"])):
		str += f"{t_chars['horizontal'] * (headers['lengths'][i] + 2)}"
		if i < len(headers["names"]) - 1:
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
				table_headers["names"] = line.split(";")
				table_headers["lengths"] = [len(name) for name in table_headers["names"]]
			row_count += 1

	print(build_table_headers(table_headers))

except IOError:
	print(f"File {input} not found")
	sys.exit(1)

