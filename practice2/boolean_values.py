#1 example
print(True)
print(False)

#2 example
x = 5
y = 10

print(x < y)   # True
print(x == y)  # False

#3 example
is_raining = True

if is_raining:
    print("Take an umbrella!")
else:
    print("Enjoy the sunshine!")

#4 example
has_ticket = True
is_student = False

print(has_ticket and is_student)  # False
print(has_ticket or is_student)   # True
print(not has_ticket)             # False

#5 example
def is_even(number):
    return number % 2 == 0

print(is_even(4))  # True
print(is_even(7))  # False