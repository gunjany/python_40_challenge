class UserItems:
	def __init__(self, n):
		self.name = n	
		self.price_0_100 = 5.10
		self.price_100_500 = 5.00
		self.price_500_1000 = 4.95
		self.price_1000 = 4.85
		print('Hello {}. Welcome to you account.'.format(self.name))
		print('Current shipping prices are as follows:\n\
			\nShipping orders 1 to 100:\t\t$5.10 each\
			\nShipping orders 100 to 500:\t\t$5.00 each\
			\nShipping orders 500 to 1000:\t\t$4.95 each\
			\nShipping orders over 1000:\t\t$4.80 each')

	def takeInput(self, items):
		bill_payment = items
		price_each = 0
		if items > 0 and items < 100:
			bill_payment *= 5.10
			bill_payment = round(bill_payment, 2)
			price_each = self.price_0_100
		elif items >= 100 and items < 500:
			bill_payment *= 5.00
			bill_payment = round(bill_payment, 2)
			price_each = self.price_100_500
		elif items >= 500 and items < 1000:
			bill_payment *= 4.95
			bill_payment = round(bill_payment, 2)
			price_each = self.price_500_1000
		else:
			bill_payment *= 4.85
			bill_payment = round(bill_payment, 2)
			price_each = self.price_1000

		return bill_payment, price_each
		

print("Welcome to the Shipping Accounts Program.\n")

users = ['Bob', 'Marley', 'Teena', "Aron", 'Ryan']

name = input("What is your user name? ").title()

if name in users:
	obj = UserItems(name)
	quantity = int(input("\nHow many items would you like to ship: "))
	price, price_each = obj.takeInput(quantity)
	print('\nTo ship {} items it will cost you ${} at ${} per item.'.format(quantity, price, price_each)) 

	place_order = input('Would you like to place the order(y/n): ').lower()

	if place_order == 'y':
		print('\nOkay. Shipping your {} items.'.format(quantity))
	elif place_order == 'n':
		print('\nOkay, no order is being placed at this time.')
	else:
		print('\nSorry Not a correct option. We are not shipping the orders.')
else:
	print('\nSorry, you don\'t have an account with us. GoodBye.')






