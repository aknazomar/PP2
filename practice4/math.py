# 1 (Convert degree to radian)
import math

degree = 15
radian = math.radians(degree)
print("Input degree:", degree)
print("Output radian:", radian)


# 2 (Calculate the area of a trapezoid)
height = 5
base1 = 5
base2 = 6

area = ((base1 + base2) / 2) * height
print("Height:", height)
print("Base 1:", base1)
print("Base 2:", base2)
print("Expected Output:", area)


# 3 (Calculate the area of a regular polygon)
import math

n = 4   # number of sides
s = 25  # length of a side

area = (n * s**2) / (4 * math.tan(math.pi / n))
print("Input number of sides:", n)
print("Input the length of a side:", s)
print("The area of the polygon is:", area)

# 4 (Calculate the area of a parallelogram)
base = 5
height = 6

area = base * height
print("Length of base:", base)
print("Height of parallelogram:", height)
print("Expected Output:", area)
