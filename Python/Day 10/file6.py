try:
    f1=input("Enter the name of the first file:")
    f2=input("Enter the name of the second file:")
    f1o=open(f1)
    f2o=open(f2, "w")
    w=f1o.read()[::-1]
    f2o.write(w)
    print
    f1o.close()
    f2o.close()
except Exception as e:
    print("Error occured: ", e)