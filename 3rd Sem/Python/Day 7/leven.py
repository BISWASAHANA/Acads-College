l_ = [35, 12, 69, 55, 75, 14, 73]
iseven_= lambda x:x%2==0      
even_list = [i for i in l_ if iseven_(i)]
print(f"Even numbers in the given list is: {even_list}")
