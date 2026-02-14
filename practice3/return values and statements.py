# Пример 1: возвращаем число
def square(x):
    return x * x

print(square(4))
print()

# Пример 2: возвращаем строку
def welcome(name):
    return "Hello " + name

print(welcome("Aknaz"))
print()

# Пример 3: несколько return
def check_number(n):
    if n > 0:
        return "Positive"
    else:
        return "Non-positive"

print(check_number(-3))
print()

# Пример 4: возвращаем список
def create_list():
    return [1, 2, 3]

print(create_list())
print()

# Пример 5: возвращаем несколько значений
def stats(a, b):
    return a+b, a*b

s, p = stats(3, 4)
print("Sum:", s, "Product:", p)