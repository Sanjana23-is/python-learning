# Q3. Grade Calculator:
# A (90-100), B (80-89), C (70-79), D (60-69), F (<60)

score = int(input("enter ur score: "))

if score > 100 or score < 0:
    print("Invalid score")
    exit()

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")