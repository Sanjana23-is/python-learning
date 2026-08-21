### Q7. Coffee Customization ☕️
# Customize a coffee order: **"Small"**, **"Medium"**, or **"Large"**, with an option for **"Extra shot"** of espresso.

order_size = input("Enter coffee size (Small, Medium, Large): ").lower()
extra_shot = input("Do you want an extra shot of espresso? (yes/no): ").lower()

if extra_shot:
    coffee = order_size + " coffee with extra shot"

else:
    coffee = order_size + "coffee"

print("order: ", coffee)