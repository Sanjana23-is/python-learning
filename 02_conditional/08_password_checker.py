# Q8. Password Strength Checker:
# Check if a password is Weak (<6), Medium (6-10), or Strong (>10) based on its length.

password = input("enter password: ")

if len(password)<6:
    print("weak")
elif len(password) <= 10:
    print("medium")
else: 
    print("strong")