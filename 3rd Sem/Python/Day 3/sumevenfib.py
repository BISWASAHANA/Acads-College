num1=0
num2=1
next_num=num2
s=0
ul=int(input("Enter the upperlimit: "))
while next_num<=ul+1:
    num1,num2=num2,next_num
    next_num=num1+num2
    if next_num%2==0:
        print(next_num)
        s+=next_num
        
print("Sum of even valued terms of fibonacci series: ",s)
    
