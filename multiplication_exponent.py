# Multiplication table and Exponent table

print("Welcom to the Multiplication/Exponent Table App")

name = input("What is your name: ").capitalize()
number = float(input("What number would you like to work with: "))

print("Multiplication Table for ", number)
for i in range(1, 10):
	print("\t\t{} * {} = {}".format(round(float(i), 1), number, round(i * number, 4)))
print("\nExponent Table for ", number)
for i in range(1, 10):
	print("\t\t{} * {} = {}".format(number, i, round(number**i, 4)))
msg = name.title()+", Math is cool!"

print(msg)
print("\t\t", msg.lower())
print("\t\t\t", msg.title())
print("\t\t\t\t", msg.upper())