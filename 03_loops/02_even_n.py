num = int(input("enter a num: "))
count =0
for n in range(1, num+1):
    if n%2==0:
        count += 1
print(count)