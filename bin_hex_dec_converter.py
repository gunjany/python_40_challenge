print("Welcome to the Binary/Hexadecomal Converter App.\n")

number = int(input('Compute binary and hexadecimal values up to the following number: '))

bin_num = []
hex_num = []

print("Generating lists.....complete!\n")

for i in range(1 , number+1):
	bin_num.append(bin(i))
	hex_num.append(hex(i))

print('Using slices, we will now show a portion of each list.\n')
first_num = int(input('What decimal number would you like to start at: '))
second_num = int(input('What decimal number would you like to stop at: '))

print('Decimal values from {} to {}:'.format(first_num, second_num))
for i in range(first_num, second_num+1):
	print(i)

print('\nBinary values from {} to {}:'.format(first_num, second_num))
for x in range(first_num-1, second_num ):
	print(bin_num[x])

print('\nHexadecimal values from {} to {}:'.format(first_num, second_num))
for x in range(first_num-1, second_num ):
	print(hex_num[x])	

input('Press enter to see all the values from {} to {}.'.format(1, number))
print('Decimal-------Binary-------Hexadecimal\n------------------------------')
for i in range(0, number):
	print('{}-----{}-----{}'.format(i+1, bin_num[i], hex_num[i])) 