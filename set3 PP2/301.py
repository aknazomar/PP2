n = int(input())
while n > 0:
    if n % 2 != 0:
        print("Not valid")
        break
    n //= 10
else:
    print("Valid")