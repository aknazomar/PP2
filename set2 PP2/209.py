a = int(input())
listik = list(map(int, input().split()))

maxik = max(listik)
minik = min(listik)
for i in range(len(listik)):
    if listik[i] == maxik:
        listik[i] = minik
print(*listik)