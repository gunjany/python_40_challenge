import math

def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n-1)


print('Welcome to the Factorial Calculator App\n')

number = int(input('What number would you like to compute the factorial of? '))

print('{}! = 1'.format(number), end = '')

for i in range(2, number + 1):
	print('*{}'.format(i), end = '')

print('\nHere is the result from the math library:')
fact_math = math.factorial(number)
print('The factorial of {} is {}!'.format(number, fact_math))

fact_fun = factorial(number)
print('\nHere is the result from my own algorithm:\nThe factorial of {} is {}!'.format(number, fact_fun))

if fact_fun == fact_math:
	print('\nIt is shown twice that {}! = {}(with excitement)'.format(number, fact_fun))