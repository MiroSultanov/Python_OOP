# Refactor the provided code, so you do not need to make any changes in it when you want to add new species to the animals' list

def add_other_animal_sounds(func):
    new_sounds = {
        'chicken': 'cluck'
    }

    def wrapper(animals: list):
        for animal in animals:
            if animal.species in ['cat', 'dog']:
                func([animal])
            else:
                print(new_sounds.get(animal.species, 'no sound'))
    return wrapper


class Animal:
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species


@add_other_animal_sounds
def animal_sound(animals: list):
    for animal in animals:
        if animal.species == 'cat':
            print('meow')
        elif animal.species == 'dog':
            print('woof-woof')


animals = [Animal('cat'), Animal('dog')]
animal_sound(animals)

## add a new animal and refactor the code to work without having to make changes to it
## when adding new animals
animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
animal_sound(animals)
