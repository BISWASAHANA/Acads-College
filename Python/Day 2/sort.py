# Input three numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Using if-elif-else to sort the numbers
if num1 <= num2 and num1 <= num3:
    smallest = num1
    if num2 <= num3:
        middle = num2
        largest = num3
    else:
        middle = num3
        largest = num2
elif num2 <= num1 and num2 <= num3:
    smallest = num2
    if num1 <= num3:
        middle = num1
        largest = num3
    else:
        middle = num3
        largest = num1
else:
    smallest = num3
    if num1 <= num2:
        middle = num1
        largest = num2
    else:
        middle = num2
        largest = num1

# Print the sorted numbers
print("Sorted numbers:", smallest, middle, largest)
