def strc(s):
    u=0
    l=0
    for i in s:
        if i.isupper():
            u+=1
        elif i.islower():
            l+=1
    return(f"The number of uppercase letters is: {u} and the number of lowercase letters is {l}")

x=input("Enter the string: ")
print(strc(x))
