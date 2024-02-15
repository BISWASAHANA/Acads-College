def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = gcd(max(num1, num2),min(num1, num2))
res=((num1*num2)//(result))
print(f"The LCM of {num1} and {num2} is {res}")
