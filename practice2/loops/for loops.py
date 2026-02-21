#1
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
print(" ")
# apple
# banana
# cherry

#2
total = 0
for i in range(1, 6):
    total += i**2
print("Sum of squares:", total)  # 55
print(" ")
# Sum of squares: 55

#3
for i in range(1, 4):
    for j in range(1, 4):
        print(i, "x", j, "=", i*j)
print(" ")
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9


#4
numbers = [1, 2, 3, 4, 5, 6]
odds = [n for n in numbers if n % 2 != 0]
print(odds)
print(" ")
# [1, 3, 5]

#5
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
print(" ")
# 0 apple
# 1 banana
# 2 cherry