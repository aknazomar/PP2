# Пример 1: простая функция
def greet():
    print("Hello!")

greet()  # вызов функции
print()

# Пример 2: функция без аргументов
def say_hi():
    print("Hi there!")

say_hi()
print()

# Пример 3: функция вызывается несколько раз
def repeat():
    print("This is repeated")

repeat()
repeat()
print()


# Пример 4: функция внутри цикла
def loop_message():
    print("Looping...")

for i in range(3):
    loop_message()
print()


# Пример 5: функция в другой функции
def outer():
    print("Outer function")
    def inner():
        print("Inner function")
    inner()
outer()
print()