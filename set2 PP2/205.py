n = int(input())
if n > 0:
    a = n & (n - 1)
    if a == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")