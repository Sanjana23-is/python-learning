# 🐍 Python Dictionaries


# 1. Creating a dictionary

chai_types = {
    "Masala": "spicy",
    "Ginger": "zesty",
    "Green": "mild"
}

print(chai_types)
# {'Masala': 'spicy', 'Ginger': 'zesty', 'Green': 'mild'}


# 2. Accessing a value using its key

print(chai_types["Masala"])
# spicy


# 3. Changing a value

chai_types["Masala"] = "very spicy"

print(chai_types)
# {'Masala': 'very spicy', 'Ginger': 'zesty', 'Green': 'mild'}


# 4. Adding a new key-value pair

chai_types["Lemon"] = "tangy"

print(chai_types)
# {'Masala': 'very spicy', 'Ginger': 'zesty', 'Green': 'mild', 'Lemon': 'tangy'}


# 5. Looping through dictionary keys

for key in chai_types:
    print(key)

# Masala
# Ginger
# Green
# Lemon


# 6. Looping through keys and values

for key, value in chai_types.items():
    print(key, value)

# Masala very spicy
# Ginger zesty
# Green mild
# Lemon tangy


# 7. Checking if a key exists

if "Masala" in chai_types:
    print("Masala chai is available")

# Masala chai is available


# 8. Length of dictionary

print(len(chai_types))
# 4


# 9. pop() - removes a specific key-value pair

removed = chai_types.pop("Ginger")

print(removed)
# zesty

print(chai_types)
# {'Masala': 'very spicy', 'Green': 'mild', 'Lemon': 'tangy'}


# 10. popitem() - removes the last inserted key-value pair

removed_item = chai_types.popitem()

print(removed_item)
# ('Lemon', 'tangy')

print(chai_types)
# {'Masala': 'very spicy', 'Green': 'mild'}


# 11. del - delete a specific key

del chai_types["Green"]

print(chai_types)
# {'Masala': 'very spicy'}


# 12. Adding another item

chai_types["Ginger"] = "zesty"

print(chai_types)
# {'Masala': 'very spicy', 'Ginger': 'zesty'}


# 13. copy() - creates a separate dictionary

chai_types_copy = chai_types.copy()

chai_types_copy["Lemon"] = "tangy"

print(chai_types)
# {'Masala': 'very spicy', 'Ginger': 'zesty'}

print(chai_types_copy)
# {'Masala': 'very spicy', 'Ginger': 'zesty', 'Lemon': 'tangy'}


# 14. clear() - removes all items

chai_types_copy.clear()

print(chai_types_copy)
# {}


# 15. Nested dictionaries

tea_shop = {
    "chai": {
        "Masala": "spicy",
        "Ginger": "zesty"
    },
    "tea": {
        "Green": "mild",
        "Black": "strong"
    }
}

print(tea_shop)
# {'chai': {'Masala': 'spicy', 'Ginger': 'zesty'},
#  'tea': {'Green': 'mild', 'Black': 'strong'}}


# 16. Accessing a nested dictionary

print(tea_shop["chai"])
# {'Masala': 'spicy', 'Ginger': 'zesty'}

print(tea_shop["chai"]["Ginger"])
# zesty


# 17. Dictionary comprehension

squares = {x: x ** 2 for x in range(6)}

print(squares)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# 18. dict.fromkeys()

keys = ["m", "g", "l"]

new_dict = dict.fromkeys(keys, "delicious")

print(new_dict)
# {'m': 'delicious', 'g': 'delicious', 'l': 'delicious'}


# 19. fromkeys() without a value

new_dict2 = dict.fromkeys(keys)

print(new_dict2)
# {'m': None, 'g': None, 'l': None}


# 20. fromkeys() with a mutable value

new_dict3 = dict.fromkeys(keys, keys)

print(new_dict3)
# {
#     'm': ['m', 'g', 'l'],
#     'g': ['m', 'g', 'l'],
#     'l': ['m', 'g', 'l']
# }

# All three keys refer to the SAME list object.