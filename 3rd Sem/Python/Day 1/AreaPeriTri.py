import math
def AreaTri(s1,s2,s3):
    s=(s1+s2+s3)/2
    area=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
    return area

def PeriTri(s1,s2,s3):
    return s1+s2+s3
s1,s2,s3=map(int,input("Enter the length of the 3 sides: ").split())
print("What do you want to calculate?\n1. Area \n2. Perimeter")
ans=int(input("Enter 1 or 2:"))
if ans==1:
    print("Area =",AreaTri(s1,s2,s3))
else:
    print("Perimeter =",PeriTri(s1,s2,s3))


    
    
