import random

print("Welcome to the Rock Pa[er Scissor Game.\n")

rounds = int(input("How many rounds would you like to play: "))

rps = ['Rock', 'Paper', 'Scissor']

comp_sc = 0
player_sc = 0

for choice in range(rounds):
	print("\nRound ", str(choice+1))
	print("Player: {}\t Computer: {}\n". format(player_sc, comp_sc))

	comp_choice = random.choice(rps)

	player_choice = input("Time to pick...rock, paper, scissor: ").title()

	print("\tComputer: {}\n\tPlayer: {}".format(comp_choice, player_choice))

	if player_choice == comp_choice:
		print("\n\tIt's a tie.")

	elif player_choice == 'Scissor' and comp_choice =='Paper':
		print("\tScissors cut Paper!\n\tYou win round {}".format(choice+1))
		player_sc += 1

	elif player_choice == 'Paper' and comp_choice =='Rock':
		print("\tPaper covers Rock!\n\tYou win round {}".format(choice+1))
		player_sc += 1

	elif player_choice == 'Rock' and comp_choice =='Scissor':
		print("\tRock breaks Scissors!\n\tYou win round {}".format(choice+1))
		player_sc += 1

	elif comp_choice == 'Scissor' and player_choice =='Paper':
		print("\tScissors cut Paper!\n\tComputer win round {}".format(choice+1))
		comp_sc += 1

	elif comp_choice == 'Paper' and player_choice =='Rock':
		print("\tPaper covers Rock!\n\tComputer win round {}".format(choice+1))
		comp_sc += 1

	elif comp_choice == 'Rock' and player_choice =='Scissor':
		print("\tRock breaks Scissors!\n\tComputer win round {}".format(choice+1))
		comp_sc += 1	

	else:
		print("\tThat's not a valid option!\n\tComputer gets the point.")
		comp_sc += 1

print("\nFinal Game Results:")
print("\t\tRounds Played: ", str(rounds))
print("\t\tPlayer Score: ", str(player_sc))
print("\t\tComputer Score: ", str(comp_sc))

if comp_sc>player_sc:
	print("\t\tWinner: Computer :-(")

else:
	print("\t\tWinner: PLAYER!")
