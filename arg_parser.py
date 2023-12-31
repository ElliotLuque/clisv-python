import argparse

parser = argparse.ArgumentParser(prog='clisv' ,description='Prints csv file as table in console')
parser.add_argument('file', metavar='file', type=str, help='csv file to print')
parser.add_argument('--align', metavar='alignment', type=str, help='alignment of table elements')
parser.add_argument('--color', metavar='color', type=str, help='color of table elements')
parser.add_argument('--delimiter', metavar='delimiter', type=str, help='delimiter of csv file')
parser.add_argument('--bold', action='store_true', help='bold table header')
parser.add_argument('--indexed', action='store_true', help='add index column')
parser.add_argument('--style', metavar='style', type=str, help='style of table')
args = parser.parse_args()

FILE = args.file
ALIGNMENT = args.align if args.align else "left"
COLOR = args.color if args.color else "reset"
DELIMITER = args.delimiter if args.delimiter else ";"
IS_BOLD = args.bold if args.bold else False
INDEXED = args.indexed if args.indexed else False
TABLE_STYLE = args.style if args.style else "default"