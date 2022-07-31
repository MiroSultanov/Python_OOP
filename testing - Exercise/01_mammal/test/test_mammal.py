import unittest
from project.mammal import Mammal

class TestMammals(unittest.TestCase):
    NAME = 'Pesho'
    MAMMAL_TYPE = 'TYPE'
    SOUND = "SOUND"
    KINGDOM = "animals"

    def setUp(self) -> None:
        self.m = Mammal(self.NAME, self.MAMMAL_TYPE, self.SOUND)

    def test_init(self):
        self.assertEqual(self.m.name, self.NAME)
        self.assertEqual(self.m.type, self.MAMMAL_TYPE)
        self.assertEqual(self.m.sound, self.SOUND)
        self.assertEqual(self.KINGDOM, self.m._Mammal__kingdom)

    def test_make_sound_animals(self):
        actual_result = self.m.make_sound()
        expected_result = f"{self.NAME} makes {self.SOUND}"

        self.assertEqual(actual_result, expected_result)

    def test_get_kingdom_returns_animals(self):
        actual_result = self.m.get_kingdom()

        self.assertEqual(self.KINGDOM, actual_result)

    def test_info_returns_proper(self):
        actual_result = self.m.info()
        expected_result = f"{self.NAME} is of type {self.MAMMAL_TYPE}"

        self.assertEqual(actual_result, expected_result)

if __name__ == "__main__":
    main()