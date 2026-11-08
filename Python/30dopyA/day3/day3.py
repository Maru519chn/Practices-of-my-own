#Boolean, operator, assignment operators, arithmetic operators, comparison operators, logical operators and exercises.

# Boolean
# True or false

# Assignment operators
# Assignment operators are used to assign values to variables.
# = → x = 5 same as x = 5
# += → x += 5 same as x = x + 5
# -= → x -= 5 same as x = x - 5
# *= → x *= 5 same as x = x * 5
# /= → x /= 5 same as x = x / 5
# %= → x %= 5 same as x = x % 5
# //= → x //= 5 same as x = x // 5
# **= → x **= 5 same as x = x ** 5
# &= → x &= 5 same as x = x & 5
# |= → x |= 5 same as x = x | 5
# ^= → x ^= 5 same as x = x ^ 5
# >>= → x >>= 5 same as x = x >> 5
# <<= → x <<= 5 same as x = x << 5

#Arithmetic operators
# Addition(+): a + b
# Subtraction(-): a - b
# Multiplication(*): a * b
# Division(/): a / b
# Modulus(%): a % b
# Floor division(//): a // b
# Exponentiation(**): a ** b

print('Addition: ', 5 + 3)
print('Subtraction: ', 5 - 3)
print('Multiplication: ', 5 * 3)
print('Division: ', 5 / 3)
print('Modulus: ', 5 % 3)
print('Floor division: ', 5 // 3)
print('Exponentiation: ', 5 ** 3)
print('Division without the remainder: ', 5 // 3)

print('Floating Point Number, PI: ', 3.14)
print('Floating Point Number, e: ', 2.71)
print('Floating Point Number, Golden Ratio: ', 1.618)
print('Floating Point Number, Square Root of 2: ', 1.414)

print('Complex Number: ', 1 + 2j)
print('Multiplication of Complex Number: ', (1 + 2j) * (3 + 4j))

a = 3
b = 2

Total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# Should have used sum instead of total but sum is a built-in function in Python.
# Try to avoid overriding built-in functions in Python.

print('a + b =', Total)
print('a - b =', diff)
print('a * b =', product)
print('a / b =', division)
print('a % b =', remainder)
print('a // b =', floor_division)
print('a ** b =', exponential)

print('== Addition, Substraction, Multiplication, Modulus ==')

num_one = 3
num_two = 4

#Arithmetic Operations
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
div = num_one / num_two
remainder = num_one % num_two

print('Total: ', total)
print('Difference: ', diff)
print('Product: ', product)
print('Division: ', div)
print('Remainder: ', remainder)

pi = 3.14
e = 2.71
g = 9.81

#Calculating the area of a circle
radius = 10
area_of_circle = pi * radius ** 2
print('Area of Circle: ', area_of_circle)

#Calculating the area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of Rectangle: ', area_of_rectangle)

#Weight of an object
mass = 75
weight = mass * g
print('Weight of an object: ', weight, 'N')

#Density of an liquid
mass = 75 #in kg
volume = 0.075 #in m^3
density = mass / volume
print('Density of an liquid: ', density, 'kg/m^3')
