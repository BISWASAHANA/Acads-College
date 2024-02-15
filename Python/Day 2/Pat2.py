rows = int(input("Enter the no. of rows: "))

for i in range(1, rows + 1):
    print(" " * (i - 1), "* " * (rows - i + 1))