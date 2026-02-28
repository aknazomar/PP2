# 1 Generator for squares up to N
def generate_squares(N):
    for i in range(1, N+1):
        yield i * i
        
for square in generate_squares(5):
    print(square)


# 2 Generator for even numbers between
#  0 and n (comma-separated)
def even_numbers(n):
    for i in range(0, n+1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number: "))
print(",".join(str(num) for num in even_numbers(n)))


# 3  Generator for numbers 
# divisible by 3 and 4 between 0 and n
def divisible_by_3_and_4(n):
    for i in range(0, n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Example usage
for num in divisible_by_3_and_4(50):
    print(num)


# 4 Generator called squares 
# to yield squares from (a) to (b)
def squares(a, b):
    for i in range(a, b+1):
        yield i * i

for val in squares(3, 7):
    print(val)


# 5 
def squares(a, b):
    for i in range(a, b+1):
        yield i * i

# Test with a for loop
for val in squares(3, 7):
    print(val)