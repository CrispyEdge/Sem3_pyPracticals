def NumRev(n):
    rev = 0
    while(n>0):
        rev = (rev * 10) + (n % 10)
        n = n // 10
    print("The reverse of this number is", rev)

n = int(input("Enter the number: "))
NumRev(n)
