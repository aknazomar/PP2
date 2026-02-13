n = int(input())
pi = list(map(int, input().split()))
max_v = pi[0]
for i in pi:
    if i > max_v:
        max_v = i
print(max_v)