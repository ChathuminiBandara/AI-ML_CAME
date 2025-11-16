x= 10
#print(type(x))
x="CAME"
#print(type(x))
x=22
y="23"
# print(x+y)


class Student:
    def printDetails(self):
        print("This is a student class")

class Customer:
    def printDetails(self):
        print("This is a customer class")

s = Student()
c= Customer()

def printPerson(p):
    p.printDetails()

printPerson(s)
printPerson(c)