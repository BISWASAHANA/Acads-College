lst=[87,"rust",108,"golang","python","ruby","java","solana","rust","solana","ruby","java"]
def ul(l):
    unil=[]
    for i in l:
        if l.count(i)==1:
            unil.append(i)
    return(f"The unique elements in the given list {lst} are {unil}")

print(ul(lst))
