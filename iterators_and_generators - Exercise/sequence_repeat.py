# Create a class called sequence_repeat which should receive a sequence and a number upon initialization. Implement an iterator to return the given elements, 
# so they form a string with a length - the given number. If the number is greater than the number of elements, then the sequence repeats as necessary. 
# For more clarification, see the examples:

class sequence_repeat:

    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.__i = -1

    def __iter__(self) -> iter:
        return self

    def __next__(self) -> str:
        if self.number > 0:
            self.number -= 1
            if self.__i == len(self.sequence) - 1:
                self.__i = -1
            self.__i += 1
            return self.sequence[self.__i]
        raise StopIteration()


if __name__ == '__main__':
    result = sequence_repeat('abc', 5)
    for item in result:
        print(item, end='')
        
#  Test Code
# result = sequence_repeat('abc', 5)
# for item in result:
#     print(item, end ='')
    
# result = sequence_repeat('I Love Python', 3)
# for item in result:
#     print(item, end ='')
