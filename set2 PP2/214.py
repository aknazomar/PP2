n = int(input())
nums = list(map(int, input().split()))

freq = {}
for x in nums:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

max_count = 0
answer = None
for x in freq:
    if freq[x] > max_count or (freq[x] == max_count and (answer is None or x < answer)):
        max_count = freq[x]
        answer = x

print(answer)
