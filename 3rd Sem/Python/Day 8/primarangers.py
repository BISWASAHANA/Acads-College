prime_numbers=[]
primecheck= lambda x: all(x%i!=0 for i in range(2, int(x*0.5)+1))
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
def primes(start,end):
    for i in range(2,end):
        if primecheck(i)==True:
            prime_numbers.append(i)
        else:
            pass
#Taking the range as input

# Print the results
print(f"Prime numbers between {start} and {end} are:")
print(prime_numbers)