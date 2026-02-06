#they are not required, but I didn't know
#1 example
a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

#2 example
c = int(input())
d = int(input())
c += 3
d += 5
print(c)
print(d)

#3 example
x = 3
print(x := 3)

#4 example 
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

#5 example
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#6 example
x = 5
print(x > 0 and x < 10)

x = 5
print(x < 5 or x > 10)

x = 5
print(not(x > 3 and x < 10))

#7 example
#is - Checks if both variables point to the same object in memory
#== - Checks if the values of both variables are equal
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

#8 example
x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

#9 example 
#Check if "banana" is present in a list:

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

#Check if "pineapple" is NOT present in a list:

fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)

text = "Hello World"
print("H" in text)
print("hello" in text)
print("z" not in text)

#10 example
print(6 & 3) #Sets each bit to 1 if both bits are 1
print(6 | 3) #Sets each bit to 1 if one of two bits is 1
print(6 ^ 3)  #Sets each bit to 1 if only one of two bits is 1
print(6 << 3) #Shift left by pushing zeros in from the right and let the leftmost bits fall off
print(6 >> 3) #Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

#