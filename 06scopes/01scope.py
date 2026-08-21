username = "luna"
def fun():
    username = "sanjana"
    print("username is", username) 

print("username is", username)
fun()

# ex 1
x=99
def fun2(y):
    z=x+y
    return z
print(fun2(1))

# ex 3
def fun3():
    x=88
    return x

print(fun3())


# ex 4
# def fun4():
#     global x
#     x=88
#     return x

# fun4()
# print(x)

def fun5():
    x = 22
    def inner():
        print(x)
    # inner()
    return inner()

fun5()

