l = tuple(int(x) for x in input("Enter the elements of the tuple separated by spaces: ").split())
result=[]
for i in l:
    for j in l:
        if int(i) * int(j) %2 == 0:
            pair=(int(i),int(j))
            if pair in result:
                continue
            if (int(j),int(i)) not in result:
                result.append(pair)
print(f"Resultant List = {tuple(result)}")
