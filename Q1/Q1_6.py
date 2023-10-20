# factorial withour recurrsion
n = int(input("Enter a number: "))
def factorialsimple(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

print(factorialsimple(n)) # print is needed if return is used in function instead of print

# factorial with recurrsion
n = int(input("Enter a number: "))
def recurrsionfactorial(n):
    if (n==0):
        return 1
    return n * recurrsionfactorial(n-1)

print(recurrsionfactorial(n))
    
    
