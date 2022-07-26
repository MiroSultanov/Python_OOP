# Having the following code:
#     def even_numbers(function):

#     def wrapper(numbers):

#         # TODO: Implement

#     return wrapper

# Complete the code, so it works as expected.

def even_numbers(function):
    def wrapper(numbers):
        result = function(numbers)
        return [x for x in result if x % 2 == 0]

    return wrapper

@even_numbers
def get_numbers(numbers):
    return numbers
print(get_numbers([1, 2, 3, 4, 5]))
