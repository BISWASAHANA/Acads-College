l1=[]


n=int(input("How many elements do you want to keep in the list? :"))
print("Enter the elements:")
for i in range(n):
    x=int(input())
    l1.append(x)

mx=0
mn=10000000000000000000

for i in l1:
    if i>mx:
        mx=i

for j in l1:
    if j<mn:
        mn=j


print('Maximum in the given list is:',mx)
print('Minimum in the given list is:',mn)
    


