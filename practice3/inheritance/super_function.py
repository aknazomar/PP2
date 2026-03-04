class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname= lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()

# By using the super() function, 
# you do not have to use the name 
# of the parent element, it will 
# automatically inherit the methods 
# and properties from its parent.