# Mutable vs Immutable in Python

# ---------------- MUTABLE ----------------
# Lists are mutable

a = [1, 2, 3]
b = a

print("Before change:")
print("a =", a)
print("b =", b)

# Changing the existing list object
a[0] = 99

print("\nAfter changing a:")
print("a =", a)
print("b =", b)   # b also changes because both point to the same list

print("\na == b:", a == b)   # True -> same values
print("a is b:", a is b)     # True -> same object


# ---------------- IMMUTABLE ----------------
# Integers are immutable

x = 10
y = x

print("\nBefore change:")
print("x =", x)
print("y =", y)

# Cannot change the integer object 10.
# Instead, x is made to refer to another object (20)
x = 20

print("\nAfter changing x:")
print("x =", x)
print("y =", y)   # y is still 10

print("\nx == y:", x == y)   # False -> different values
print("x is y:", x is y)     # False -> different objects