print('Welcome to the Fibonacci Calculator App\n')
num = int(input('How many digits of the Fibonnacci Sequence would you like to compute: '))
num = num +1

def fibonacci(n):
	fibo = [0, 1]
	for i in range(n-2):
		fibo.append(fibo[i] + fibo[i+1])

	return fibo

fibonacci_ = fibonacci(num)

print('The first {} numbers of the fibonacci Sequence are: \n'.format(num-1))
for i in (fibonacci_):
	print(i)

print('\nThe corresponding Golden Ratio values are:')
golden = []
for i in range(1, len(fibonacci_)-1):
	golden.append(fibonacci_[i+1]/fibonacci_[i])

for ratio in golden:
	print(ratio)

print("\nThe ratio of consecutive Fibonacci terms approaches Phi: 1.618...")