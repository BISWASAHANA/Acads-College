#Write a Python program that creates a menu-driven sorting algorithm application.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)

def print_menu():
    print("Menu:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Quick Sort")
    print("4. Exit")

while True:
    print_menu()
    choice = input("Select a sorting algorithm (1/2/3/4): ")

    if choice == '4':
        break

    try:
        choice = int(choice)
    except ValueError:
        print("Invalid input. Please enter a valid option.")
        continue

    if choice not in [1, 2, 3]:
        print("Invalid choice. Please select a valid option (1/2/3/4).")
        continue

    numbers = input("Enter a list of numbers separated by spaces: ")
    numbers = [int(x) for x in numbers.split()]

    if choice == 1:
        bubble_sort(numbers)
    elif choice == 2:
        selection_sort(numbers)
    elif choice == 3:
        numbers = quick_sort(numbers)

    print("Sorted list: ", numbers)
