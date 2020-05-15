print("Welcome to the Grade Sorter App\n")

grade =[]
for i in range(4):
	grade.append(int(input("What is your "+ str(i+1) +" grade(0-100): ")))

print("Your grades are: ", grade)
grade = sorted(grade)
grade = grade[::-1]
print("\nYour grades from highest to lowest are: ", grade)

print("The lowest two grades will now be dropped.\n")
print("Reversed grade: {}".format(grade.pop()))
print("Reversed grade: {}".format(grade.pop()))

print("\nYour remaining grades are: ", grade)
print("Nice work! Your highest grade is a ", grade[0])