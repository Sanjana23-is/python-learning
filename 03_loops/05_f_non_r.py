# given a string, find first non repeating character

# sanjanashetty
s = input("enter a sting: ")

for char in s:
    if s.count(char) == 1:
        print (char)
        exit()