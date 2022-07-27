# Create a decorator called logged. It should return the name of the function that is being called and its parameters. It should also return the result of the execution of 
# the function being called

def logged(func_ref):
    def wrapper(*args):
        result = func_ref(*args)
        return f"you called {func_ref.__name__}{args}\nit returned {result}"

    return wrapper

# Test Code

@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))
