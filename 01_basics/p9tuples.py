# Tuples in Python


# 1. Creating a tuple

t_types = ("b", "g", "o")

print(t_types)
# ('b', 'g', 'o')


# 2. Accessing elements using indexing

print(t_types[0])
# b

print(t_types[-1])
# o


# 3. Tuples are immutable

# t_types[0] = "l"
# TypeError: 'tuple' object does not support item assignment


# 4. Finding the length

print(len(t_types))
# 3


# 5. Concatenating tuples

more_t = ("h", "e")

all_t = t_types + more_t

print(all_t)
# ('b', 'g', 'o', 'h', 'e')


# 6. Checking if an item exists

if "g" in all_t:
    print("yes")
# yes


# 7. count() - counts occurrences of an item

more_t = ("h", "e", "h")

print(more_t.count("h"))
# 2

print(more_t.count("s"))
# 0


# 8. Tuple unpacking

t_types = ("b", "g", "o")

b, g, o = t_types

print(b)
# b

print(g)
# g

print(o)
# o


# 9. Another example of tuple unpacking

name, age, branch = ("Sanjana", 21, "ISE")

print(name)
# Sanjana

print(age)
# 21

print(branch)
# ISE


# 10. Number of variables should match the number of values

# a, b = (1, 2, 3)
# ValueError: too many values to unpack


# 11. Tuple can contain different types

student = ("Sanjana", 21, "ISE", True)

print(student)
# ('Sanjana', 21, 'ISE', True)


# 12. Tuples can be nested

nested_tuple = (("Masala", "Ginger"), ("Green", "Black"))

print(nested_tuple)
# (('Masala', 'Ginger'), ('Green', 'Black'))

print(nested_tuple[0])
# ('Masala', 'Ginger')

print(nested_tuple[0][1])
# Ginger