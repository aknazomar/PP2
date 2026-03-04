class Person:
    def printname(self):
        print("Person: generic name")

class Student(Person):
    def printname(self):  # overriding the parent method
        print("Student: specific name")

p = Person()
s = Student()

p.printname()  # Person: generic name
s.printname()  # Student: specific name

# Here, Student overrides 
# printname. Even though Student 
# inherits from Person, its own 
# version of printname is used.