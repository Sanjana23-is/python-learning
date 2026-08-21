# Q8. Function with **kwargs
# Write a function that accepts any number of keyword arguments
# and prints them in key: value format.

#keyword arguments - kwargs()
# print(kwargs) - prints the dictionary of key-value pairs

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Superman", power="Flight")
print_kwargs(power="Flight", name="Superman")
print_kwargs(power="Flight")
print_kwargs(name="Superman")
print_kwargs(enemy="Lex Luthor")
