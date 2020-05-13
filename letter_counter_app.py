name = input(("Welcome to the Letter COunter App\nWhat is your name: "))

print("Hello {}".format(name.capitalize()))
msg = input("\nI will count the number of times that a specific letter occurs in a message.\nPlease enter a message:")

letter = input("\nWhich letter would you like to count the occurences of: ")
letter = letter.lower()

msg = msg.lower()
count = 0
for char in msg:
	if char == letter:
		count += 1

print("\n{}, your message has {} {}'s in it.".format(name.capitalize(), count, letter))