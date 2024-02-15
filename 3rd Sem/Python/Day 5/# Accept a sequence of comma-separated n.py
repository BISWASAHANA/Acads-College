# Accept a sequence of comma-separated numbers from the user
input_str = input("Enter a sequence of comma-separated numbers: ")

# Split the input string into a list of strings using a comma as the delimiter
numbers_str = input_str.split(',')

# Convert the list of strings to a tuple of integers
numbers_tuple = tuple(int(num) for num in numbers_str)

# Display the generated tuple
print("Generated tuple:", numbers_tuple)