print("Welcome to the Thesaurus App!\n")

import random

words = {"hot":['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
		 "cold":['chilly', 'cool', 'freezing', 'frigid', 'polar'],
		 "happy":['content', 'cheery', 'merry', 'jovial', 'jocular'],
	 	 "sad":['unhappy', 'downcast', 'miserable', 'glum', 'melancholy'],}

print("Choose a word from the thesaurus and I will give you a synonym. \nHere are the words in the thesaurus:")

for word in words:
	print('\t\t', word)

user_word = input('What word would you like a synonym for: ').lower()

if user_word in words:
	syn = random.choice(words[user_word])
	print('A synonym for {} is {}\n'.format(user_word, syn))
else:
	print("This word is not in the Thesaurus.\n")

whole_th = input("Would you like to see the whole thesaurus (yes/no): ").lower()

if whole_th.startswith('y'):
	for word in words:
		print("\n{} synonyms are: ".format(word))
		for syn in words[word]:
			print('\t\t-', syn)

else:
	print("\nI hope you enjoyed the program. Thank you!")
