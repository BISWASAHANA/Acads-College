start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Use a lambda function to check if a number is divisible by both 5 and 7
is_divisible = lambda x: x % 5 == 0 and x % 7 == 0

# Use list comprehension to find the numbers within the range that satisfy the condition
divisible_numbers = [x for x in range(start, end + 1) if is_divisible(x)]

# Print the results
print(f"Numbers divisible by 5 and 7 between {start} and {end}:")
for i in divisible_numbers:
    print(i)

