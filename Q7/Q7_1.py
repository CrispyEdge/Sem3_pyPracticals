# class Student:
#     def __init__(self, name, rollno, phoneno):
#         self.name = name
#         self.rollno = rollno
#         self.phoneno = phoneno

#     def display(self):
#         print("The name of the student is: ", self.name)
#         print("The rollno of the student is: ", self.rollno)
#         print("The phoneno of the student is: ", self.phoneno)

# name = input("Enter the name of the student: ")
# rollno = int(input("Enter the rollno of the student: "))
# phoneno = int(input("Enter the phoneno of the student: "))

# obj = Student(name, rollno, phoneno)
# obj.display()

class Student:
    def __init__(self, name, rollno, phoneno):
        self.name = name
        self.rollno = rollno
        self.phoneno = phoneno

    def display(self):
        print("The name of the student is: ", self.name)
        print("The rollno of the student is: ", self.rollno)
        print("The phoneno of the student is: ", self.phoneno)
        
    def fun1(self, num1):
        self.num1 = num1
        print(num1)
        
        
class Employee:
    
    def __init__(self, name, rollno, phoneno):
        self.name = name
        self.rollno = rollno
        self.phoneno = phoneno

    def display(self):
        print("The name of the e is: ", self.name)    
        print("The rollno of the e is: ", self.rollno)
        print("The phoneno of the e is: ", self.phoneno)
        
    def fun1(self, num1):
        self.num1 = num1
        print(num1)
        

name = input("Enter the name of the student: ")
rollno = int(input("Enter the rollno of the student: "))
phoneno = int(input("Enter the phoneno of the student: "))

obj = Student(name, rollno, phoneno)
obj.display()



obj2 = Employee(name, rollno, phoneno)
obj2.display()


