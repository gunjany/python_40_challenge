import random

print("Wwelcome to the coin Toss App.\n\nI will flip \
a coin a set number of times.")

flip_count = int(input("How many times would you like me to \
flip the coin: "))
choice = input("Would you like to see the result of each flip(y/n): ").lower()

print("\nFlipping!!!\n")

head = 0
tail = 0

for flips in range(flip_count):
	coin = random.randint(0, 1)
	if coin == 1:
		head += 1 
		if choice.startswith('y'):
			print("HEAD")

	else:
		tail += 1 
		if choice.startswith('y'):
			print("TAIL")

	if head == tail:
		print("At {} flips, the number of heads and tails were equal at {} each".format(flips+1, head))


print("\nResults of Flipping a coin {} times: \n".format(flip_count))
head_percent = round(head/flip_count * 100, 2)
tail_percent = round(tail/flip_count * 100, 2)
print("Side\t\tCount\t\tPercentage")
print("Heads\t\t{}/{}\t\t{}%".format(head, flip_count, head_percent))
print("Tails\t\t{}/{}\t\t{}%".format(tail, flip_count, tail_percent))