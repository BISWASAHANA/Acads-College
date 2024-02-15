input_numbers = []
odd_pairs = []
n=int(input("How many numbers do you want to input in list?: "))
print("Input the numbers: ")
for i in range(n):
    x=int(input())
    input_numbers.append(x)

for i in range(len(input_numbers)):
    for j in range(i + 1, len(input_numbers)):
        product = input_numbers[i] * input_numbers[j]
        if product % 2 == 1:
            odd_pairs.append((input_numbers[i], input_numbers[j]))
li=[]    
if len(odd_pairs) > 0:
    print("Distinct pairs with odd product:")
    for pair in odd_pairs:
        li.append(pair)
    if len(li)>0:
        for i in li:
            print(i)
    else:
        print("No distinct pairs with odd product found.")