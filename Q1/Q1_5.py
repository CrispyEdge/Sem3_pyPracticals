n = int(input("Enter a number: "))
def ArmStrong(n):
    sum = 0
    orignal = n
    while(n>0):
        sum = sum + (n%10)* (n%10)* (n%10)
        n = n // 10
    if(sum==orignal):
        print("The given number is an armstrong number")
    else:
        print("The given number is not an armstrong number")

ArmStrong(n)

n = int(input("Enter a number: "))
def palindrome(n):
    sum = 0
    orignal = n
    while(n>0):
        sum = (sum*10) + (n%10)
        n = n//10
    if(sum==orignal):
        print("The number is a palindrome")
    else:
        print("The number is not a palindrome")

palindrome(n)

