#1
numbers = [2, 4, 6, 8, 10, 12]
for n in numbers:
    if n == 8:
        print("Found 8, stopping loop")
        break
    print("Checked:", n)
#Checked: 2
#Checked: 4
#Checked: 6
#Found 8, stopping loop

#2
values = [5, 3, 7, -2, 9]
for v in values:
    if v < 0:
        print("Negative number found:", v)
        break
    print("Positive:", v)
#Positive: 5
# Positive: 3
# Positive: 7
# Negative number found: -2

#3
text = "hello world"
for ch in text:
    if ch == " ":
        print("Space found, stopping")
        break
    print("Letter:", ch)
#Letter: h
# Letter: e
# Letter: l
# Letter: l
# Letter: o
# Space found, stopping

#4
for i in range(1, 11):
    if i**2 > 30:
        print("Square too big:", i**2)
        break
    print("Square:", i**2)
# Square: 1
# Square: 4
# Square: 9
# Square: 16
# Square: 25
# Square too big: 36

#5
attempts = ["123", "hello", "python", "admin"]
for attempt in attempts:
    if attempt == "python":
        print("Correct password found:", attempt)
        break
    print("Wrong attempt:", attempt)
# Wrong attempt: 123
# Wrong attempt: hello
# Correct password found: python
