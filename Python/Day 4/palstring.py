s=input("Enter a string: ")
if s.lower()==s[::-1].lower():
    print(f"The given sting {s} is a palindrome")
else:
    print(f"The given sting {s} is not a palindrome")
