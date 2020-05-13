# Take input from the user 
fahrenheit = float(input(("Welcome to the Temperature Conversion App\
	\n\nWhat is the given temperature in degrees Fahrenheit: ")))

# Conversion into Degree Celsius
celsius = round(float((fahrenheit - 32) * 5/9), 4) 

# Conversion into Degree Kelvin
kelvin = round(float((fahrenheit - 32) * 5/9 + 273.15), 4)

print("\nDegrees Fahrenheit:\t{}".format(round(fahrenheit, 4)))
print("Degree Celsius:\t\t{}".format(celsius))
print("Degree Kelvin:\t\t{}".format(kelvin))