# Пример 1: позиционные аргументы
def add(a, b):
    print(a + b)

add(2, 3)
print()

# Пример 2: аргументы по умолчанию
def greet(name="Guest"):
    print("Hello,", name)

greet()
greet("Aknaz")
print()

# Пример 3: *args (произвольное количество)
def show_numbers(*args):
    for num in args:
        print(num)

show_numbers(1, 2, 3, 4)
print()

# Пример 4: **kwargs (ключевые аргументы)
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

show_info(name="Aknaz", age=20)
print()

# Пример 5: смешанные аргументы
def profile(name, age=18, *skills, **details):
    print("Name:", name)
    print("Age:", age)
    print("Skills:", skills)
    print("Details:", details)

profile("Aknaz", 21, "Python", "Git", country="Kazakhstan")