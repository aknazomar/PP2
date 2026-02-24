# 1 (lambda with sorted) sorting a list with tuples by the second element
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

# 2 (lambda with sorted) sorting strings by length
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

# 3 (lambda with sorted) sorting numbers
random_nums = [1, 2, 5, 7, 4, 3, 7, 9]
sorted_nums = sorted(random_nums, key=lambda x: x)
print(sorted_nums)

# 4 (lambda with sorted) sorting algebraic operations 
algebra = [1+2, 4*2, 1-1, 5+2, 9/1, 8-7]
sorting = sorted(algebra, key=lambda x: x)
print(sorting)