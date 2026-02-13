n = int(input())
episodes = {}

for _ in range(n):
    s, k = input().split()
    k = int(k)
    if s in episodes:
        episodes[s] += k
    else:
        episodes[s] = k

for name in sorted(episodes.keys()):
    print(name, episodes[name])