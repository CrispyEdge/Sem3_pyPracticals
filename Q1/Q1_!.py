import datetime
name = input("Enter your name: ")
age = int(input("Enter your age: "))
CurrentYear = datetime.datetime.now().year
print("You will turn 100 years old in", + (CurrentYear+(100-age)))
