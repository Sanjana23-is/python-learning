# Q9. Generator Function with yield
# Write a generator function that yields even numbers up to a specified limit.

def even_numbers(limit):
    for i in range(2, limit+1, 2):
        yield i 
        # about yield - it is used to return a value from a generator function. It allows the function to produce a series of values over time, instead of computing them all at once and sending them back. When the generator function is called, it returns an iterator object but does not start execution immediately. Each time the next() method is called on the iterator, the function executes until it reaches a yield statement, which returns the yielded value and pauses the function's state. The next time next() is called, the function resumes execution right after the yield statement, continuing until it either reaches another yield or completes execution.

for num in even_numbers(10):
    print(num)