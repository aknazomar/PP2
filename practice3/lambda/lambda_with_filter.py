# 1 (lambda with filter)
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

# 2 (lambda with filter)
names = ["Aknaz", "Adele", "Ulzhan", "Talshyn", "Akniet", "Ayazhan"]
long_names = list(filter(lambda x: len(x) > 4, names))
print(long_names)

# 3
