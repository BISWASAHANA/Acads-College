n=int(input("Enter an integer: "))
if n==1:
    print(f"{n} is not a prime number")
flag=True
for i in range(2,(n//2)+1):
    if n%i==0:
        flag=False
        break
if flag==False:
    print(f"{n} is not a prime number")
else:
    print(f"{n} is a prime number")

