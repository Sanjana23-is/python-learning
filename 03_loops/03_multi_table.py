num = int(input("enter a number: "))

for n in range(1, 11):
    if(n == 5):
        continue
    print(f"{n} * {n} = {num*n} ")

