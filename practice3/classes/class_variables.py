# 1
class Dog:
    species = "Canis familiaris"  # переменная класса

    def __init__(self, name):
        self.name = name  # переменная экземпляра

dog1 = Dog("Buddy")
dog2 = Dog("Charlie")

print(dog1.name, dog1.species)  # Buddy Canis familiaris
print(dog2.name, dog2.species)  # Charlie Canis familiaris


# 2
class Car:
    count = 0  # переменная класса

    def __init__(self, model):
        self.model = model
        Car.count += 1  # увеличиваем общий счётчик

car1 = Car("Toyota")
car2 = Car("BMW")

print("Всего машин создано:", Car.count)  # 2

# 3
class Student:
    school_name = "№1 School"  # переменная класса

    def __init__(self, name):
        self.name = name

student1 = Student("Aknaz")
student2 = Student("Dana")

print(student1.name, student1.school_name)  # Aknaz №1 School
print(student2.name, student2.school_name)  # Dana №1 School

# 4
class Circle:
    pi = 3.14  # переменная класса

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * (self.radius ** 2)

c1 = Circle(5)
print("Площадь:", c1.area())  # 78.5

# меняем значение переменной класса
Circle.pi = 3.14159
c2 = Circle(5)
print("Площадь с новым pi:", c2.area())  # 78.53975
