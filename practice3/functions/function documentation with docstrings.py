# Пример 1: простая документация
def greet():
    """Prints a greeting message."""
    print("Hello!")

print(greet.__doc__)
print()

# Пример 2: описание аргументов
def add(a, b):
    """Takes two numbers and returns their sum."""
    return a + b

print(add.__doc__)
print()

# Пример 3: многострочный docstring
def multiply(a, b):
    """
    Multiply two numbers.
    Args:
        a: first number
        b: second number
    Returns:
        product of a and b
    """
    return a * b


print(multiply.__doc__)
print()

# Пример 4: docstring для списка
def show_items(items):
    """Prints all items from a list one by one."""
    for i in items:
        print(i)

print(show_items.__doc__)
print()

# Пример 5: docstring для функции без аргументов
def info():
    """Displays basic info message."""
    print("This is a simple function.")

print(info.__doc__)