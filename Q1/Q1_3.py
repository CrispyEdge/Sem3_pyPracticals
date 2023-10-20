n = int(input("Enter a number: "))
first  = 0
second = 1
sum = 0
while(sum<=n):
    print(sum)
    first = second
    second = sum
    sum = first + second
