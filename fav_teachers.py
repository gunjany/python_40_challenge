print('Welcome to the favorite teachers program.'.title())

fav_teacher = []

for i in range(4):
	fav_teacher.append(input('Who is your {} favorite teacher: '.format(i+1)).title())

print('\nYour favorite teachers ranked are: ', fav_teacher)
sort_fav_teacher = sorted(fav_teacher)
print('Your favorite teachers alphabetically are: ', sort_fav_teacher)
print('Your favorite teachers in reverse alphabetical order are: ', sort_fav_teacher[::-1])

print('\nYour top two teachers are: {} and {}.'.format(fav_teacher[0], fav_teacher[1]))
print('Your next two favorite teachers are: {} and {}'.format(fav_teacher[2], fav_teacher[3]))
print('Your last favorite teacher is: ', fav_teacher[-1])
print('You have a total of {} favorite teachers.\n'.format(len(fav_teacher)))

new_teacher = input('Oops, '+fav_teacher[0] + ' is no longer your first favorite teacher. Who is your new FAVORITE teacher: ').title()
print(new_teacher)

fav_teacher.insert(0, new_teacher)

print('\nYour favorite teachers are ranked as : ', fav_teacher)
sort_fav_teacher = sorted(fav_teacher)
print('Your favorite teachers alphabetically are: ', sort_fav_teacher)
print('Your favorite teachers in reverse alphabetical order are: ', sort_fav_teacher[::-1])

print('\nYour top two teachers are: {} and {}.'.format(fav_teacher[0], fav_teacher[1]))
print('Your next two favorite teachers are: {} and {}'.format(fav_teacher[2], fav_teacher[3]))
print('Your last favorite teacher is: ', fav_teacher[-1])
print('You have a total of {} favorite teachers.\n'.format(len(fav_teacher)))

dislike_teacher = input('You have decided you no longer like a teacher. Which teacher would you like to remove from your list: ').title()

fav_teacher.remove(dislike_teacher)

print('\nYour favorite teachers are ranked as : ', fav_teacher)
sort_fav_teacher = sorted(fav_teacher)
print('Your favorite teachers alphabetically are: ', sort_fav_teacher)
print('Your favorite teachers in reverse alphabetical order are: ', sort_fav_teacher[::-1])

print('\nYour top two teachers are: {} and {}.'.format(fav_teacher[0], fav_teacher[1]))
print('Your next two favorite teachers are: {} and {}'.format(fav_teacher[2], fav_teacher[3]))
print('Your last favorite teacher is: ', fav_teacher[-1])
print('You have a total of {} favorite teachers.\n'.format(len(fav_teacher)))
