# Take input from the user 
miles_per_hour = float(input(("Welcome to the Miles Per Hour Conversion App\
	\n\nWhat is your speed in mules per hour: ")))

# 1 mph = 0.4474 mps
meters_per_second = float(miles_per_hour * 0.4474)

print("Your speed in meters per second is : {}".format(round(meters_per_second, 2)))
