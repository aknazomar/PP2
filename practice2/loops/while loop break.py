#1
i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1
#1
#2

#2
while True:
    command = input("Enter command (type 'exit' to stop): ")
    if command == "exit":
        break
    print("You typed:", command)

#3
numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(numbers):
    if numbers[i] == 4:
        print("Found 4!")
        break
    i += 1
#Found 4!

#4
while True:
    print("Running once")
    break
#Running once

#5
i = 10
while i > 0:
    print(i)
    if i == 5:
        break
    i -= 1
# 10
# 9
# 8
# 7
# 6
# 5