def max_val(list_val):
     max_val = max(list_val, key = lambda i: (isinstance(i, int), i))  
     return(max_val)
l=[35,67,89,31,29,47,97,53,41,61]
print("Original list:")
print(l)
print("\nMaximum values in the said list using lambda:")
print(max_val(l))