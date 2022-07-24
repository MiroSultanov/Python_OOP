# Create a class called dictionary_iter. Upon initialization, it should receive a dictionary object. Implement the iterator to return each key-value pair of
# the dictionary as a tuple of two elements (the key and the value).

class dictionary_iter:

    def __init__(self, dict_obj: dict):
        self.dict_obj = dict_obj

    def __iter__(self) -> iter:
        return self

    def __next__(self) -> tuple:
        if self.dict_obj.keys():
            key = list(self.dict_obj.keys())[0]
            value = self.dict_obj.pop(key)
            return key, value
        raise StopIteration()


if __name__ == '__main__':
    result = dictionary_iter({1: "1", 2: "2"})
    for x in result:
        print(x)
        
        
# Test Code
# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)
    
    
# result = dictionary_iter({"name": "Peter", "age": 24})
# for x in result:
#     print(x)
