# Q4. Create a function that returns both the area and
# circumference of a circle given its radius.

import math
r = 5

def total(r):
    area = round(math.pi * r ** 2, )
    circum = round(2*math.pi*r, 2)
    return area, circum

a, c = total(r)
print("area: ", a, "\ncircumference: ", c)
def area(r):
    return round(math.pi * r ** 2, )

def circum(r):
    return round(2*math.pi*r, 2)

print(area(r))
print(circum(r))