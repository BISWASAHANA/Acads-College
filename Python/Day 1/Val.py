a=int(input("Enter the number:"))
x=len(str(a))
while x>0:
    print(a%(10**x))
    x=x-1
