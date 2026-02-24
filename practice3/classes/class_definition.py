# creating class
class MyClass:
    x = 5

# creating object
p1 = MyClass()
print(p1.x)

# deleting objects
del p1

# create three objects from the MyClass class
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)
# note: each object is independent and has its own copy of the class properties

# the pass statement
class Person:
    pass
# class definitions cannot be empty, 
# but if you for some reason have a 
# class definition with no content, 
# put in the pass statement to avoid 
# getting an error.