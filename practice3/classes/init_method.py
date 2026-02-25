# 1 (using __init__ to assign values)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

# The __init__() method is called 
# automatically every time the class 
# is being used to create a new object.

# 2 (testing code without __init__)
class Person:
    pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age)

# 3 (the second example with __init__)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Linus", 28)

print(p1.name)
print(p1.age)

# 4 (setting default values for parametres with __init__)
class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)

#5 (multiple parametres)
class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self. city = city
        self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)