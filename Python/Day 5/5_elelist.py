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

for j in l2:
    if j not in l1:
        ul.append(j)


print("List of the elements which are present in list2 but not in list1 is: ", ul)

