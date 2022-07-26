# Having the following code:
    
#     def vowel_filter(function):

#     def wrapper():

#         # TODO: Implement

#     return wrapper

# Complete the code, so it works as expected:

def vowel_filter(function):
    vowels = set('aeiou' + 'aeiou'.upper())

    def wrapper():
        result = function()
        return [c for c in result if c in vowels]
    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())

