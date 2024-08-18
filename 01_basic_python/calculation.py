def add(x, y):
	return x + y

def sub(x, y):
	return x - y

# 아래에 곱하기 함수(mul)를 추가해보세요.
# def mul( , ):
#	return  

# 아래에 나누기 함수(div)를 추가해보세요.



def main():
	num1 = float(input('Enter your first number: '))
	num2 = float(input('Enter your second number: '))
	type_ = input('Enter type of operartion (+, -, *, or /): ')

	if type_ == '+':
		print(add(num1, num2))
	elif type_ == '-':
		print(sub(num1, num2))
	
	# 아래에 type_가 '*'라면, mul 함수의 결과를 출력하는 코드를 작성해주세요.
	# elif type_== :
	# 		print()
	
	# 아래에 type_가 '/'라면, div 함수의 결과를 출력하는 코드를 작성해주세요.
	

	else:
		print("Invalid type of operation: '{}'".format(type_))

if __name__ =='__main__':
	main()
