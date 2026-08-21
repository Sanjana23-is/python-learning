# factorial of a number using while loop
num = int(input("enter a num: "))
# 4
ans = 1

# def fact(n):
#     if n==1:
#         return 1
#     return n* fact(n-1)
# print (fact(3))

while(num>1):
    ans = ans * num
    num-=1
print(ans)
