l1=[]
l2=[]
ul=[]
n1=int(input("Enter the no. of elements you want to insert in l1: "))
print("Enter the elements: ")
for i in range(n1):
    x=int(input())
    l1.append(x)

n2=int(input("Enter the no. of elements you want to insert in l2: "))
print("Enter the elements: ")
for i in range(n2):
    x=int(input())
    l2.append(x)

for i in l1:
    if i not in ul:
        ul.append(i)
for j in l2:
    if j not in ul:
        ul.append(j)


print("Union of the given list is: ", ul)

