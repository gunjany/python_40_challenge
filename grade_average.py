print('Welcome to the Average Calculator App\n')

def grade_summary(grades):
	print('\tTotal Number of Grades: {}'.format(len(grades)))
	print('\tHighest Grade: ', max(grades))
	print('\tLowest Grade: ', min(grades))
	average= 0
	for num in grades:
		average += num

	average /= len(grades) 
	print('\tAverage: ', average)
	return average


name = input('What is your name: ').title()
num_of_grades = int(input('How many grades would you like to enter: '))

grades = []

for i in range(num_of_grades):
	grades.append(float(input('Enter grade {}: '.format(i+1))))

grades_sorted = grades
grades_sorted.sort()
grades_sorted = grades_sorted[::-1]

print('Grades Highest to lowest:')
for grade in grades_sorted:
	print('\t', grade)

print("{}'s Grade Summary:".format(name))

avg1 = grade_summary(grades)

desired = float(input('What is your desired average: '))
grade_req = round(float(desired * (len(grades)+1) - sum(grades)), 2)
print('Good Luck {}!\nYou will need to get a {} on your next assignment to earn a {} average.'.format(name, grade_req, desired))

print('Lets see what your average could have been if you did better/worse on an assignment.')
change_grade = float(input('What grade would you like to change: '))
changed_grade = float(input('What grade would you like to change {} with: '.format(change_grade)))
grades_sorted = [changed_grade if x==change_grade else x for x in grades_sorted]

grades_sorted.sort()
grades_sorted = grades_sorted[::-1]

print('New Grades Highest to lowest:')
for grade in grades_sorted:
	print('\t', grade)

print("{}'s New Grade Summary:".format(name))

avg2 = grade_summary(grades_sorted)

print('\nYour new average would be a {} compared to your real average of {}!'.format(avg2, avg1))
print('That is a change of {} points!'.format(avg2-avg1))

print('\nToo Bad your original grades are still the same!')
print(grades)
print('You should go ask for extra credit!')