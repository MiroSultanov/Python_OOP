class DecorationRepository:

    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type: str):
        for i, decoration in enumerate(self.decorations):
            if decoration.decoration_type == decoration_type:
                return self.decorations.pop(i)
            return 'None'
