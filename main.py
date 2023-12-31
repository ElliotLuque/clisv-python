import sys
import csv
from table_printer import print_table
from arg_parser import FILE as input, DELIMITER, INDEXED

def main():
	try:
		table = []
		with open(input, 'r', encoding='utf-8') as file:
			reader = csv.reader(file, delimiter=DELIMITER)
			for row in reader:
				if not row:
					continue
				table.append(row)
		
		# Add a column with indexes at start
		if INDEXED:
			for i in range(len(table)):
				if i == 0:
					table[i].insert(0, "(index)")
				else:
					table[i].insert(0, str(i))

		print_table(table)
	except IOError:
		print(f"File {input} not found")
		sys.exit(1)

if __name__ == '__main__':
	main()
