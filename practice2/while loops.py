#1
i = 1
while i <= 5:
    print(i)
    i += 1
print()
# 1
# 2
# 3
# 4
# 5

#2
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blast off!")
print()
# 5
# 4
# 3
# 2
# 1
# Blast off!

#3
password = ""
while password != "python":
    password = input("Enter password: ")
print("Access granted")
print()
# Enter password: python
# Access granted

#4
total = 0
num = 1
while num <= 5:
    total += num
    num += 1
print("Sum is:", total)
print()
#Sum is: 15

#5
keep_running = True
i = 0
while keep_running:
    print("Loop iteration:", i)
    i += 1
    if i == 3:
        keep_running = False
print()
# Loop iteration: 0
# Loop iteration: 1
# Loop iteration: 2