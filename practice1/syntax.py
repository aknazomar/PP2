#1 example
a = int(input())
b = int(input())
if a > b:
    print("a is greater than b")
elif a == b:
    print("equal")
else:
    print("a is not greater than b")


#2 example
c = input("c =").split()
d = input("d =").split()
if c > d:
    print("c is longer than d")
elif c == d:
    print("equal")
else:
    print("d is longer than c")


# 3 example
a = "aknaz"
o = "omar"
if a == "aknaz" and o == "omar":
    print("aknaz omar")

#4 example 
f = "faza"
k = "kama"
if f == "faza" or k == "kama":
    print("faza i kama smotryat serial v studii")

#5 example 
arthouse = len("almaloud")
moments = len("helping")
if arthouse == 8:
    print("yayayyayay")
else:
    print("oyoyoyoy")