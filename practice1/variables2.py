# Variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# typing many variables in the same line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


# giving same value for many varibles
x = y = z = "Orange"
print(x)
print(y)
print(z)


# joining many varibles
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


# Multiple variables in one line
x = 5
y = "John"
print(x, y)

# Global variable
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()