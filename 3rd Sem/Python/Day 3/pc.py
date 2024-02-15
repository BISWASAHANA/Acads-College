flag=True
c=0
p=0
x=0
while flag:
    f=True
    n=int(input("Enter an integer: "))
    if n==-1:
        break
    else:
        x+=1
        if n==0 or n==1:
            c+=1
        else:
            for i in range(2,(n//2)+1):
                if n%i==0:
                    f=False
            if f==False:
                c+=1
        

print("The no. of composite numbers =",c)
print("The no. of prime numbers =",x-c)

                
