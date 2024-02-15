#Write a Python program that creates a menu-driven number base converter.

def decimal_to_binary(decimal):
    return bin(decimal).replace("0b", "")

def decimal_to_octal(decimal):
    return oct(decimal).replace("0o", "")

def decimal_to_hexadecimal(decimal):
    return hex(decimal).replace("0x", "")

def binary_to_decimal(binary):
    return int(binary, 2)

def octal_to_decimal(octal):
    return int(octal, 8)

def hexadecimal_to_decimal(hexadecimal):
    return int(hexadecimal, 16)

def print_menu():
    print("Menu:")
    print("1. Decimal to Binary")
    print("2. Decimal to Octal")
    print("3. Decimal to Hexadecimal")
    print("4. Binary to Decimal")
    print("5. Octal to Decimal")
    print("6. Hexadecimal to Decimal")
    print("7. Exit")

while True:
    print_menu()
    choice = input("Select a conversion (1/2/3/4/5/6/7): ")

    if choice == '7':
        break

    try:
        choice = int(choice)
    except ValueError:
        print("Invalid input. Please enter a valid option.")
        continue

    if choice not in [1, 2, 3, 4, 5, 6]:
        print("Invalid choice. Please select a valid option (1/2/3/4/5/6/7).")
        continue

    if choice in [1, 2, 3]:
        decimal_input = int(input("Enter a decimal number: "))
    else:
        if choice == 4:
            binary_input = input("Enter a binary number: ")
        elif choice == 5:
            octal_input = input("Enter an octal number: ")
        elif choice == 6:
            hexadecimal_input = input("Enter a hexadecimal number: ")

    if choice == 1:
        result = decimal_to_binary(decimal_input)
        print("Binary: ", result)
    elif choice == 2:
        result = decimal_to_octal(decimal_input)
        print("Octal: ", result)
    elif choice == 3:
        result = decimal_to_hexadecimal(decimal_input)
        print("Hexadecimal: ", result)
    elif choice == 4:
        result = binary_to_decimal(binary_input)
        print("Decimal: ", result)
    elif choice == 5:
        result = octal_to_decimal(octal_input)
        print("Decimal: ", result)
    elif choice == 6:
        result = hexadecimal_to_decimal(hexadecimal_input)
        print("Decimal: ", result)
