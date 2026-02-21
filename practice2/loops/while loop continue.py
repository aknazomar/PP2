#1
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
print()
# 1
# 2
# 4
# 5

#2
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
print()
# 1
# 3
# 5
# 7
# 9

#3
words = ["hi", "hello", "a", "world"]
i = 0
while i < len(words):
    if len(words[i]) < 3:
        i += 1
        continue
    print(words[i])
    i += 1
print()
# hello
# world

#4
i = 0
while i <= 20:
    i += 1
    if i % 5 == 0:
        continue
    print(i)
print()
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 11
# 12
# 13
# 14
# 16
# 17
# 18
# 19
# 21

#5
attempts = ["123", "pass", "python", "hello"]
i = 0
while i < len(attempts):
    if attempts[i] != "python":
        i += 1
        continue
    print("Correct password found:", attempts[i])
    break
print()

#Correct password found: python