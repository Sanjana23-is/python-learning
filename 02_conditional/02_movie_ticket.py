## Q2. Movie Ticket Pricing:

# Adults (18+) → $12, Children → $8
# Everyone gets a $2 discount on Wednesday

age = int(input("Enter your age: "))
day = input("Enter the day of the day: ").lower()
# if age > 18:
#     price = 12
# else:
#     price = 8

price = 12 if age >= 18 else 8

if day == "wednesday":
    price = price - 2
print (f"Your ticket price is ${price}")




