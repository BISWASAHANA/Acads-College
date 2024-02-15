def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a,b):
    result = gcd(a,b)
    res=((a*b)//(result))
    print(f"The LCM of {a} and {b} is {res}")

n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
if n1<n2:
    n1,n2=n2,n1

x=int(input("What do you want to find? \n1. GCD \n2. LCM \n: "))
if x==1:
    print(gcd(n1,n2))
elif x==2:
    print(lcm(n1,n2))
else:
    print("Invalid choice entered")