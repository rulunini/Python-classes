filename = 'new_file.txt'

f = open(filename, 'w')
for i in range(1, 11):
	data = f'{i} lines'
	f.write(data + '\n')

f.close()
