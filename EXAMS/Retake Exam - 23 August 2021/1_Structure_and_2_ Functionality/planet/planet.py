class Planet:

    def __init__(self, name, items):
        self.name = name
        self.items = items

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value.isspace:
            raise ValueError("Planet name cannot be empty string or whitespace!")
        self.__name = value

    @classmethod
    def from_name_items(cls, name, items):
        new_planet = cls(name)
        new_planet.items = [el for el in items.split(', ')]
        return new_planet

    @property
    def info(self):
        items_info = '\n - '.join(self.items)
        result = f'Planet name: {self.name}' \
                 f'\nItems:' \
                 f'\n - {items_info}'
        return result