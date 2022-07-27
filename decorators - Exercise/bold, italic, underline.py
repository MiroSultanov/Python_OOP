# Create three decorators: make_bold, make_italic, make_underline, which will have to wrap a text returned from a function in <b></b>, <i></i> and <u></u> respectively.

def make_bold(func_ref):
    def wrapper(*args):
        result = func_ref(*args)
        return f"<b>{result}</b>"

    return wrapper


def make_italic(func_ref):
    def wrapper(*args):
        result = func_ref(*args)
        return f"<i>{result}</i>"

    return wrapper


def make_underline(func_ref):
    def wrapper(*args):
        result = func_ref(*args)
        return f"<u>{result}</u>"

    return wrapper


# Test Code

@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))
@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))
