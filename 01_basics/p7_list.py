# Lists in Python

# 1. Creating a list

tea_varieties = ["Black", "Green", "Oolong", "White"]

print(tea_varieties)


# 2. Accessing elements

print(tea_varieties[0])
print(tea_varieties[1])
print(tea_varieties[-1])


# 3. Slicing

print(tea_varieties[1:2])
print(tea_varieties[1:3])
print(tea_varieties[1:1])


# 4. Changing elements

tea_varieties[3] = "Herbal"
print(tea_varieties)

tea_varieties[1:2] = ["Lemon"]
print(tea_varieties)

tea_varieties[1:3] = ["Green", "Masala"]
print(tea_varieties)


# 5. Looping through a list

for tea in tea_varieties:
    print(tea)


# Printing with a custom separator

for tea in tea_varieties:
    print(tea, end="-")


# 6. Checking if an item exists

if "Oolong" in tea_varieties:
    print("I have Oolong Tea")


# 7. Adding elements - append()

tea_varieties.append("Oolong")
print(tea_varieties)


# 8. Removing elements - pop()

tea_varieties.pop()
print(tea_varieties)


# 9. Removing elements - remove()

tea_varieties.remove("Green")
print(tea_varieties)


# 10. Adding elements at a specific position - insert()

tea_varieties.insert(1, "Green")
print(tea_varieties)


# 11. Copying a list

tea_varieties_copy = tea_varieties.copy()

tea_varieties_copy.append("Lemon")

print(tea_varieties)
print(tea_varieties_copy)


# 12. List Comprehension

squared_num = [x ** 2 for x in range(10)]

print(squared_num)