n = int(input())
freq = {}
for _ in range(n):
    num = input().strip()
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

count = 0
for v in freq.values():
    if v == 3:
        count += 1

print(count)