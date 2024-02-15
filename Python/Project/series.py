#Consider the following series:
#1,1,2,3,4,9,8,27,16,81,32,243,64,729,128,2187…This series is a mixture of 2 series.
#Write a program to find the nth term in the series. The nth term calculated by the program should be printed on the screen. No other character/string or message should be printed besides the value of the nth term.

def find_nth_term(n):
    if n % 2 == 0:
        # Even-indexed terms (powers of 2)
        return 2 ** (n // 2)
    else:
        # Odd-indexed terms (powers of 3)
        return 3 ** (n // 2)

n = int(input())
result = find_nth_term(n)
print(result)
