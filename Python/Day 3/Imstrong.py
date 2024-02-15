n=input("Enter an integer: ")
l=len(n)
num=int(n)
c=0
for i in range(l):
    c+=(num%10)**l
    num//=10
if c==int(n):
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")
    
