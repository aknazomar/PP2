# Пример 1: список как аргумент
def print_list(lst):
    for item in lst:
        print(item)

print_list([1, 2, 3])
print()

# Пример 2: строка как аргумент
def shout(text):
    print(text.upper())

shout("hello")
print()

# Пример 3: словарь как аргумент
def print_dict(d):
    for k, v in d.items():
        print(k, "=", v)

print_dict({"name": "Aknaz", "age": 20})
print()

# Пример 4: кортеж как аргумент
def sum_tuple(t):
    print(sum(t))

sum_tuple((1, 2, 3))
print()

# Пример 5: комбинированные типы
def show_data(data):
    print("Type:", type(data))
    print("Value:", data)

show_data([1, 2, 3])
show_data("Hello")
show_data(42)
print()