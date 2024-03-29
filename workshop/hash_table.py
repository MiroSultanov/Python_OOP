from copy import copy

class HashTable:
    DEFAULT_CAPACITY = 4

    def __init__(self):
        self.data = [None] * self.DEFAULT_CAPACITY
        self.free_slots = self.DEFAULT_CAPACITY
        self.count = 0

    def add(self, key, value):
        if self.free_slots == 0:
            self.grow_data()

        idx = self.calc_idx(key)
        if self.data[idx] is None:
            self.data[idx] = [(key, value)]
            self.free_slots -= 1
            self.count += 1
            return

        for k, v in self.data[idx]:
            if key == k:
                raise KeyError(f"{key} already exists")
        self.data[idx].append((key, value))
        self.count +=1

    def get(self, key):
        idx = self.calc_idx(key)
        idx_elements = self.data[idx]
        if idx_elements is None:
            raise KeyError(f"{key} not found")

        for k, v in idx_elements:
            if k == key:
                return v
            raise KeyError(f"{key} not found")

    def remove(self, key):
        idx = self.calc_idx(key)
        idx_elements = self.data[idx]
        if idx_elements is None:
            raise KeyError(f"{key} does not found")

        for k, v in idx_elements:
            if k == key:
                self.data[idx].remove((k, v))
                self.count =- 1
                return

        raise KeyError(f"{key} does not exists")

    def items(self):
        result =[]
        for slot in self.data:
            if slot is None:
                continue
            result.extend(slot)
        return result

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        try:
            old_value = self.get(key)
            idx = self.calc_idx(key)
            self.data[idx].remove((key, old_value))
            self.data[idx].append((key, value))
        except KeyError:
            self.add(key, value)

    def len(self):
        return self.count

    def calc_idx(self, key):
        return hash(key) % len(self.data)

    def grow_data(self):
        new_capacity = len(self.data) * 2

        existing_data = copy(self.data)

        self.free_slots = new_capacity
        self.data = [None] * new_capacity
        self.count = 0

        for slot in existing_data:
            for key, value in slot:
                self.add(key, value)

    def get_max_len(self):
        result = float('-inf')
        for slot in self.data:
            if slot in None:
                continue
            if len(slot) > result:
                result = len(slot)
        return result


# hash_table = Hashtable()
#
# for idx in range(1000000):
#     hash_table.add(f"name_{idx}", {idx})
#
# print(hash_table.get_max_len())

table = HashTable()

table["name"] = "Peter"
table["age"] = 25

print(table)
print(table.get("name"))
print(table["age"])
print(len(table))
