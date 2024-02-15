l=int(input("Enter lower limit: "))
u=int(input("Enter upper limit: "))
s=0

for n in range(l,u+1):
    if n==0 or n==1:
        continue
    else:
        for i in range(2,(n//2)+1):
            if n%i==0:
                break
        else:
            s+=n

print(s)
