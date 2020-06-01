print("Welcome to voter Registration App.\n")
name = input("What is your name? ").title()
age = int(input("What is your age: "))

parties = ['Republican', 'Democratic', 'Independent', 'Libertarian', 'Green']

if age > 18:
	print("Congratulations, {}, you are old enough to vote.".format(name))
	print("Parties are as follows:")
	for party in parties:
		print("\t\t"+party)

	choice = input("Whichbparty do you wish to join: ").title()

	if choice in parties:
		print("Congratulations, you have joined {}.".format(choice))
		if choice == 'Republican' or choice == 'Democratic':
			print("Your chosen party, {}, is a major party.".format(choice))
		elif choice == 'Independent':
			print("Your chosen party, {}, is an independent party.".format(choice))
		else:
			print("Your chosen party, {}, is not a major party.".format(choice))
	else:
		print("That's not a party in the list.")
else:
	print("You are not old enough to vote yet.")