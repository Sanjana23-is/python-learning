# Q10. Pet Food Recommendation:
# Recommend pet food based on species and age.
# Dog < 2 years → Puppy food
# Cat > 5 years → Senior cat food
# Otherwise → Regular pet food

species = input("Enter pet species: ").lower()
age = int(input("Enter pet age: "))

if species == "dog" and age < 2:
    print("Puppy food")
elif species == "cat" and age > 5:
    print("Senior cat food")
else:
    print("Regular pet food")