def histogram(lst):
    for i in lst:
        print(i*'*')

lst = []
ln = int(int(input("Enter the length of the list: ")))
print("Enter", ln, "numberes in a column")
for i in range(ln):
    result = int(input())
    lst.append(result)

histogram(lst)