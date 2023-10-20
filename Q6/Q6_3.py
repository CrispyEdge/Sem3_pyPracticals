n = int(input("Enter the num: "))
f = open("file.txt", "r")

for lines in (f.readlines() [-n:]):
    print(lines, end ="")
f.close()