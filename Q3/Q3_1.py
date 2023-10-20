str = 'the quick brown fox jumps over the lazy dog'
alphabet = 'abcdefghijklmnoqrstuvwxyz'
result = True
for i in alphabet:
    if i not in str.lower():
        result = False

if result == True:
    print("pangram")
else:
    print("False")
