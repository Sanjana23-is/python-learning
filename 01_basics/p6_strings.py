# Strings in Python

# 1. Creating strings
single_quote = 'Masala Chai'
double_quote = "Masala Chai"
triple_quote = """This is a
multi-line string"""

print(single_quote)
print(double_quote)
print(triple_quote)


# 2. Indexing
chai = "masala chai"

first_char = chai[0]
last_char = chai[-1]

print(first_char)       # m
print(last_char)        # i


# 3. Slicing
slice_c = chai[0:6]
print(slice_c)          # masala

print(chai[:6])         # masala
print(chai[7:])         # chai
print(chai[:])          # masala chai

# Negative indexing
print(chai[-1])         # i
print(chai[-4:])        # chai


# 4. String length
print(len(chai))


# 5. Strings are immutable
# chai[0] = "M"   # TypeError

# Instead, create a new string
chai = "Masala Chai"
print(chai)


# 6. Changing case
print(chai.upper())
print(chai.lower())


# 7. Removing whitespace
chai = "   masala chai   "

print(chai.strip())
print(chai.lstrip())
print(chai.rstrip())


# 8. Replacing text
chai = "Lemon Chai"

new_chai = chai.replace("Lemon", "Ginger")

print(new_chai)     # Ginger Chai
print(chai)         # Lemon Chai


# 9. Splitting a string
chai = "Lemon, Ginger, Masala, Mint"

print(chai.split(","))
print(chai.split(", "))


# 10. Finding text
chai = "Masala Chai"

print(chai.find("Chai"))    # 7
print(chai.find("chai"))    # -1


# 11. Counting occurrences
chai = "masala chai chai"

print(chai.count("chai"))   # 2


# 12. Joining strings
chai_variety = ["Lemon", "Masala", "Ginger"]

print("".join(chai_variety))
print(" ".join(chai_variety))
print("-".join(chai_variety))
print(", ".join(chai_variety))


# 13. Looping through a string
chai = "Masala Chai"

for letter in chai:
    print(letter)


# 14. String formatting
chai_type = "Masala"
quantity = 2

print("{} ordered {} cups of {}".format(quantity, chai_type, chai_type))

# f-string
print(f"{quantity} cups of {chai_type} chai")

# 1. Escape Characters

print("Hello\nWorld")       # \n -> new line
print("Hello\tWorld")       # \t -> tab
print("Hello\\World")       # \\ -> backslash
print("He said \"Hello\"")  # \" -> double quote
print('It\'s Python')       # \' -> single quote


# 2. Quotes Inside Strings

chai = "He said 'Masala Chai'"
print(chai)

chai = 'He said "Masala Chai"'
print(chai)

chai = "He said \"Masala Chai is awesome\""
print(chai)


# 3. Raw Strings

path = r"C:\user\pwd"
print(path)

# Alternative way using \\

path = "C:\\user\\pwd"
print(path)


# 4. String Membership - in

chai = "masala chai"

print("masala" in chai)
print("chai" in chai)
print("coffee" in chai)


# 5. String Membership - not in

print("coffee" not in chai)
print("masala" not in chai)


# 6. Case-sensitive Membership

print("Masala" in chai)   # False
print("masala" in chai)   # True


# 7. Strings are Sequences

chai = "masala"

# Indexing
print(chai[0])       # m
print(chai[1])       # a
print(chai[-1])      # a

# Slicing
print(chai[0:3])     # mas
print(chai[1:4])     # asa

# Iterating through a string
for letter in chai:
    print(letter)