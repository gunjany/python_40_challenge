import cmath

print('Welcome to the Quadratic Equation Solver App.')

print('\nA quadratic equation is of the form ax^2 + bx + c = 0\
	\nYour solutions can be real or complex numbers.\
	\nA complex number has two parts: a + bj\
	\nWhere a is the real portion and bj is the imaginary portion')

equation = int(input('\nHow many equations would you like to solve today: '))

for i in range(1, equation + 1):
	print('Solving equation #', i)
	print('---------------------------------------------------\n')
	a = float(input('Please enter your value of a(coefficient of x^2: '))
	b = float(input('Please enter your value of b(coefficient of x: '))
	c = float(input('Please enter your value of c(coefficient: '))

	x1 = (-b + cmath.sqrt(b**2 - 4*a*c))/2*a
	x2 = (-b - cmath.sqrt(b**2 - 4*a*c))/2*a

	print('\nThe solutions to {}x^2 + {}x + {} = 0 are:\n'.format(a, b, c))
	print('\t\tx1 = {}'.format(x1))
	print('\t\tx2 = {}\n'.format(x2))


print('Thank you for using the Quadratic Equation Solver App. Goodbye.')