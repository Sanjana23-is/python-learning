# Q1. Age Group Categorization:
# Child (<13), Teenager (13-19), Adult (20-59), Senior (60+)

age = input("Enter your age: ")
age_int = int(age)

# if(age_int < 13):
#     print("Child")
# elif(age_int >= 13 and age_int < 20):
#     print("Teenager")
# elif(age_int >= 20 and age_int < 60):
#     print("Adult")
# else:
#     print("Senior Citizen")

if age_int < 13:
    print("Child")
elif age_int < 20:
    print("Teenager")
elif age_int < 60:
    print("Adult")
else:
    print("Senior Citizen")

