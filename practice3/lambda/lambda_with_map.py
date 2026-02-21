# 1 (lambda with map)
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# 2 (lambda with filter)
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

# 3 (lambda with filter)
names = ["Aknaz", "Adele", "Ulzhan", "Talshyn", "Akniet", "Ayazhan"]
long_names = list(filter(lambda x: len(x) > 4, names))
print(long_names)

# 4 (lambda with sorted) sorting a list with tuples by the second element
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

# 5 (lambda with sorted) sorting strings by length
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)