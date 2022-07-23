# Create a generator function called reverse_text that receives a string and yields all string characters on one line in reversed order.

def reverse_text(input_text: str) -> iter:
    i = len(input_text)
    while i > 0:
        i -= 1
        yield input_text[i]


for char in reverse_text("step"):
    print(char, end='')
    
# Test Code
# for char in reverse_text("step"):
#     print(char, end='')
