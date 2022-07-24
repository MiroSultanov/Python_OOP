# Create a class called take_skip. Upon initialization, it should receive a step (int) and a count (int). Implement the __iter__ and __next__ functions. 
# The iterator should return the count numbers (starting from 0) with the given step. For more clarification, see the examples:

class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.__return = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > 0:
            self.count -= 1
            self.__return += self.step
            return self.__return - self.step
        raise StopIteration()


if __name__ == '__main__':
    numbers = take_skip(2, 6)
    for number in numbers:
        print(number)

    numbers = take_skip(10, 5)
    for number in numbers:
        print(number)
        
        
#  Test Code
# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)
    
# numbers = take_skip(10, 5)
# for number in numbers:
#     print(number)
