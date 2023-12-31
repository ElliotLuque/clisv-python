import argparse

parser = argparse.ArgumentParser(prog='clisv',description='Prints the csv file passed by argument in a table format')
parser.add_argument('file', metavar='file', type=str, help='csv file to print')
parser.add_argument('-d','--delimiter', type=str, help='delimiter of csv file. Default: \';\'')
parser.add_argument('-a','--align', metavar='ALIGNMENT', type=str, help='alignment of table elements [left, right]. Default: \'left\'')
parser.add_argument('-l','--max-length', type=int, help='max length of table elements, longer elements will be truncated. Default: \'10\'')
parser.add_argument('-s','--style', type=str, help='border style of table [default, ascii, simple, none]')
parser.add_argument('-c','--color',  type=str, help='color of table elements [red, green, blue, yellow, cyan, magenta]')
parser.add_argument('-b','--bold', action='store_true', help='enables bold headers style')
parser.add_argument('-i','--indexed', action='store_true', help='adds an index column at start of table')
parser.add_argument('-v','--version', action='version', version='%(prog)s 1.0')

args = parser.parse_args()

FILE = args.file
DELIMITER = args.delimiter if args.delimiter else ";"
ALIGNMENT = args.align if args.align else "left"
MAX_ELEMENT_LENGTH = args.max_length if args.max_length else 0
TABLE_STYLE = args.style if args.style else "default"
COLOR = args.color if args.color else "reset"
IS_BOLD = args.bold if args.bold else False
INDEXED = args.indexed if args.indexed else False
