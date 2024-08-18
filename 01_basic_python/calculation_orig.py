def add(x, y):
	return x + y

def sub(x, y):
	return x - y

def mul(x, y):
	return x * y

def div(x, y):
	return x / y

def main():
	num1 = float(input('Enter your first number: '))
	num2 = float(input('Enter your second number: '))
	type_ = input('Enter type of operartion (+, -, *, or /): ')

	if type_ == '+':
		print(add(num1, num2))
	elif type_ == '-':
		print(sub(num1, num2))
	elif type_=='*':
		print(mul(num1, num2))
	elif type_=='/':
		print(div(num1, num2))
	else:
		print("Invalid type of operation: '{}'".format(type_))

if __name__ =='__main__':
	main()
