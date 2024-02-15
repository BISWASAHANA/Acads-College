try:
    f1=input("Enter the name of the first file:")
    f2=input("Enter the name of the second file:")
    f1o=open(f1,'rb')
    f2o=open(f2,'wb')
    f2o.write(f1o.read(100))
    f1o.close()
    f2o.close()
except Exception as e:
    print("Error occured: ", e)