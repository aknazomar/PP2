n = int(input())
if n < 10:
    if n % 2 == 0 and n % 3 == 0:
        print("Yes")
    else:
        print("No")
elif n % 2 == 0 and n % 3 == 0 and n % 5 == 0:
    print("Yes")
else:
    print("No")