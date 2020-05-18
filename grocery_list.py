import datetime

grocery = ["Meat", "Cheese"]

print("Welcome to the Grocery List App\n")
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

print("Current Date and Time: " + day +"/" + month +" "+ hour + ':' + minute)

print("You currently have {} and {} in your list.\n".format(grocery[0], grocery[1]))

for i in range(3):
	grocery.append(input("Type of food to add to the grocery list: ").capitalize())

print("Here is your grocery list: \n{}". format(grocery))

print("Here is your grocery list sorted: \n{}".format(sorted(grocery)))

print("Simulating grocery shopping...\n")

while len(grocery) != 2:
	print("\nCurrent grocery List: {} items\n{}".format(len(grocery), sorted(grocery)))

	food = (input("What food did you just buy: ")).capitalize()
	print("Removing {} from the lsit...".format(food))
	grocery.remove(food)


if len(grocery) == 2:
	print("\nCurrent grocery List: {} items\n{}".format(len(grocery), sorted(grocery)))
	print("Sorry, the store is out of {}".format(grocery[-1]))
	food = input("What food would you like instead: ").capitalize()
	grocery[-1] = food
	print("\nHere is what remains on your grocery list: \n{}".format(grocery))

