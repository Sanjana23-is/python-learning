# Numbers in Python

# 1. Integer (int)
x = 10
y = -5

print(x)
print(type(x))


# 2. Floating-point number (float)
a = 3.14
b = 0.1 + 0.1

print(a)
print(type(a))
print(b)  # floating-point precision issue


# 3. Complex number
z = 2 + 3j

print(z)
print(z.real)   # real part
print(z.imag)   # imaginary part


# 4. Basic arithmetic
x = 10
y = 3

print(x + y)    # addition
print(x - y)    # subtraction
print(x * y)    # multiplication
print(x / y)    # division
print(x // y)   # floor division
print(x % y)    # remainder
print(x ** y)   # power


# 5. Type conversion
print(int(3.14))       # 3
print(float(10))       # 10.0
print(int("64"))       # 64


# 6. Different number bases
print(0b1000)          # binary → 8
print(0o20)            # octal → 16
print(0xFF)            # hexadecimal → 255

print(bin(64))         # binary representation
print(oct(64))         # octal representation
print(hex(64))         # hexadecimal representation


# 7. Decimal - exact decimal calculations
from decimal import Decimal

print(Decimal("0.1") + Decimal("0.1") + Decimal("0.1"))


# 8. Fraction
from fractions import Fraction

f = Fraction(2, 7)
print(f)


# 9. Useful math functions
import math

print(math.floor(3.5))     # 3
print(math.floor(-3.5))    # -4
print(math.trunc(3.8))     # 3
print(math.trunc(-3.8))    # -3


# 10. Random numbers
import random

print(random.random())          # random float: 0 to 1
print(random.randint(1, 10))    # random integer: 1 to 10
print(random.choice([1, 2, 3])) # random item