# Create a generator function called fibonacci() that generates the Fibonacci numbers infinitely. The first two numbers in the sequence are always 0 and 1. 
# Each following Fibonacci number is created by the sum of the current number with the previous one.

def fibonacci():
    prior = 0
    current = 1
    yield 0
    yield 1
    while True:
        retval = prior + current
        prior, current = current, retval
        yield retval


generator = fibonacci()
for i in range(10):
    print(next(generator))
    
    
#  Test Code
# generator = fibonacci()
# for i in range(5):
#     print(next(generator))
    
    
# generator = fibonacci()
# for i in range(1):
#     print(next(generator))
