print("Weelcome to the Basketball Roster Program\n")

player_list = []

player_list.append(input("Who is your Point Guard Player: ").title())
player_list.append(input("Who is your Shooting Guard Player: ").title())
player_list.append(input("Who is your Small Forward Player: ").title())
player_list.append(input("Who is your Power Forward Player: ").title())
player_list.append(input("Who is your Center Player: ").title())

print("\tYour starting 5 for the upcoming basketball season are:")

print("\t\t"+"Point Guard".ljust(16, ' ') + ': '.ljust(14, ' ')+ player_list[0])
print("\t\t"+"Shooting Guard".ljust(16, ' ') + ': '.ljust(14, ' ')+ player_list[1])
print("\t\t"+"Small Forward".ljust(16, ' ') + ': '.ljust(14, ' ')+ player_list[2])
print("\t\t"+"Power Forward".ljust(16, ' ') + ': '.ljust(14, ' ')+ player_list[3])
print("\t\t"+"Center".ljust(16, ' ') + ': '.ljust(14, ' ')+ player_list[4])
   
injured_Player = player_list[2]
player_list.remove(injured_Player)
print(player_list)

print("\nOh no {} is injured.".format(injured_Player))  
print("Your roster only has {} players.".format(len(player_list)))
added_player = input("Who will take {}'s spot: ".format(injured_Player)).title()
player_list.insert(2, added_player)

print("\tYour starting 5 for the upcoming basketball season are:")

print("\t\t"+"Point Guard".ljust(16, ' ') + ': '.ljust(14, ' ')+ player_list[0])
print("\t\t"+"Shooting Guard".ljust(16, ' ') + ': '.ljust(14, ' ')+ player_list[1])
print("\t\t"+"Small Forward".ljust(16, ' ') + ': '.ljust(14, ' ')+ player_list[2])
print("\t\t"+"Power Forward".ljust(16, ' ') + ': '.ljust(14, ' ')+ player_list[3])
print("\t\t"+"Center".ljust(16, ' ') + ': '.ljust(14, ' ')+ player_list[4])
    
print("Good luck {} you will do great.".format(added_player))
print("Your roster now has " + str(len(player_list)) + " players.")