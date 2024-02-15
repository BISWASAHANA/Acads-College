prin=int(input("Enter the principal amount: "))
roi=0
y=int(input("Enter the no. of years: "))

if prin<200000:
    roi=10
elif prin>=200000 and prin<1000000:
    roi=12
else:
    roi=15

res=((prin*roi/100)*y)
result=prin+((prin*roi/100)*y)
print(f"The Simple Interest of {prin} for {y} years is {res}")
print(f"For an investment of {prin} rupees, after {y} years, the return on investment amount will be {result}")