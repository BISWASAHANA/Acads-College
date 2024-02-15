try:
    s=input("Enter the name of the file:")
    f=open(s)
    w=f.readlines()[::-1]
    print("No. of words: ", len(w))
    f.close()
except Exception as e:
    print("Error occured: ", e)