vow=['a','e','i','o','u','A','E','I','O','U']
sent=input("Enter the sentence")
c=0
for i in sent:
    if i in vow:
        c=c+1
print("No. of vowels in the given sentence is:",c)
