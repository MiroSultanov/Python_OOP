# Create a class called reverse_iter which should receive an iterable upon initialization. Implement the __iter__ and __next__ methods, so the iterator returns the 
# items of the iterable in reversed order.

class reverse_iter:

    def __init__(self, iterable):
        self.iterable = iterable
        self.start = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > 0:
            self.start -= 1
            return self.iterable[self.start]
        raise StopIteration()


if __name__ == '__main__':
    reversed_list = reverse_iter([1, 2, 3, 4])
    for item in reversed_list:
        print(item)
        
#  Test Code
# reversed_list = reverse_iter([1, 2, 3, 4])
# for item in reversed_list:
#     print(item)
