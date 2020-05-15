num_ints = [15, 100, 55, 42]
num_strings = ["15", "100", "55", "42"]
num_floats = [45.2, 48.52, 75.369, 32.15]
num_lists = [[1, 2, 3], ['1', '2', '3'], [45.2, 56.2, 85.96]]

# Summary of each data type

print("\t\t\tSummary Table\n")

print("the variable num_strings is a ", type(num_strings))
print("It contains the elements: ", num_strings)
print("The element {} is a {}.\n".format(num_strings[0], type(num_strings[0])))

print("the variable num_ints is a ", type(num_ints))
print("It contains the elements: ", num_ints)
print("The element {} is a {}.\n".format(num_ints[0], type(num_ints[0])))

print("the variable num_floats is a ", type(num_floats))
print("It contains the elements: ", num_floats)
print("The element {} is a {}.\n".format(num_floats[0], type(num_floats[0])))

print("the variable num_lists is a ", type(num_lists))
print("It contains the elements: ", num_lists)
print("The element {} is a {}.\n".format(num_lists[0], type(num_lists[0])))

print("Now sorting num_strings and num_ints...")
print("Sorted num_strings: ", sorted(num_strings))
print("Sorted num_ints: ", sorted(num_ints))

print("\nStrings are sorted alphabetically while integers are sorted numerically!")