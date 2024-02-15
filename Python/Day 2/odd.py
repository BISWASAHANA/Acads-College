n = int(input("Enter the range: "))

if n%2==1:
    n=n+1

for i in range(1,n):
    if i%2==1:
        print(i)
