n = int(input())
a = list(map(int, input().split()))
sum = 0
for i in a:
    if i > 0:
        sum += 1
print(sum)