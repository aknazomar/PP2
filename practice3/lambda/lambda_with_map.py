# 1 (lambda with map)
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# 2
data = [1.2, 2.5, 8.5, "abc", 67]
dats = list(map(lambda x: x * 2, data))
print(dats)

# 3
alphabet = ["a", "b", "c", "d"]
alpha = list(map(lambda x: x + "a", alphabet))
print(alpha)

# 4
bottle = ["water", "juice", "soda"]
bar = list(map(lambda x: x + " cup", bottle))
print(bar)