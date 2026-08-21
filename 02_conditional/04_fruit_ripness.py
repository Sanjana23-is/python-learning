# Q4. Fruit Ripeness Checker:
# Green → Unripe, Yellow → Ripe, Brown → Overripe


fruit_c = input("Enter the color of the fruit: ").lower()

if fruit_c == "green":
    print("The fruit is unripe.")
elif fruit_c == "yellow":
    print("The fruit is ripe.")
elif fruit_c == "brown":
    print("The fruit is overripe.")
else:
    print("Unknown fruit color.")