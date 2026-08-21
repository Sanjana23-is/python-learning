# reverse a string in a loop

s = input("enter a sting: ")
# rev = s[::-1]

rev = ""
for i in s:
    rev = i + rev
    
print(rev)