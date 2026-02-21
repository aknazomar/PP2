#1
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# 1
# 2
# 4
# 5

#2
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
# 1
# 3
# 5
# 7
# 9

#3
words = ["hi", "hello", "a", "world"]
for word in words:
    if len(word) < 3:
        continue
    print(word)
# hello
# world

#4
scores = [95, 40, 67, 88, 30]
for score in scores:
    if score < 50:
        continue
    print("Passed:", score)
# Passed: 95
# Passed: 67
# Passed: 88

#5
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            continue
        print(f"i={i}, j={j}")
# i=1, j=1
# i=1, j=3
# i=2, j=1
# i=2, j=3
# i=3, j=1
# i=3, j=3