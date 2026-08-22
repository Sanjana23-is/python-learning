# Q2. Create a decorator that prints the function name and the values of its arguments every time the function is called.

def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(args) for arg in args)
        kwargs_value= ', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"Function '{func.__name__}' called with arguments: {args_value} and keyword arguments: {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

@debug
def greet(name, greet = "Hello"):
    print(f"{greet}, {name}!")

greet("chai", greet = "Hi")