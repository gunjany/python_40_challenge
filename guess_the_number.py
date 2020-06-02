print("Welcome to the Guess My Number App.\n")

import random

name = input("Hello! What is your name: ").title()
print('Well {}, I am thinking of a number between 1 and 20.\n'.format(name))

number = random.randint(1, 20)
count  = 0

for guesses in range(5):
	guess = int(input("Take a guess: "))

	if guess == number:
		print("Good job, {}! You guessed my number in {} guesses!".format(name, guesses+1))
		break

	elif guess < number:
		print("Your guess is too low.\n")

	elif guess > number:
		print("Your guess is too high.\n")

	else:
		print("Not an appropriate guess.\n")

	count += 1

if count == 5:
	print("Game Over. The number I was thinking of was {}.".format(number))