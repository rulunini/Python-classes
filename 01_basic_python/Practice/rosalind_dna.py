import argparse

parser = argparse.ArgumentParser(description='test description')

parser.add_argument('input_file', type=str, help='path')
args = parser.parse_args()

with open(args.input_file, 'r') as infile:
	content = infile.read()

print(content)
