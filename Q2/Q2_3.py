# def histogram(lst):
#     for i in lst:
#         print(i*'*')

# lst = []
# ln = int(int(input("Enter the length of the list: ")))
# print("Enter", ln, "numberes in a column")
# for i in range(ln):
#     result = int(input())
#     lst.append(result)

# histogram(lst)

def histogram(lst):
    for i in lst:
        print(i*'*')
        
lst = []
ls = int(input("enter the length of your number: "))
print("Enter", ls, "numbers: ")
for i in range(ls):
    result = int(input())
    lst.append(result)
    
histogram(lst)