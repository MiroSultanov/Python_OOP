import unittest

class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False



class CatTests(unittest.TestCase):

    def test_cat_size_increased_after_eating(self):
        c = Cat("Flerken")
        c.fed = False
        expected = c.size
        c.eat()
        self.assertGreater(c.size, expected)

    def test_cat_is_fed_after_eating(self):
        c = Cat("Flerken")
        c.fed = False
        c.eat()
        self.assertTrue(c.fed)

    def test_raise_error_cat_cannot_eat_if_already_fed(self):
        c = Cat("Flerken")
        c.fed = True
        with self.assertRaises(Exception) as contex:
            c.eat()
        self.assertTrue("Already fed." in str(contex.exception))

    def test_raise_error_cat_cannot_sleep_if_not_fed(self):
        c = Cat("Flerken")
        c.fed = False
        with self.assertRaises(Exception) as contex:
            c.sleep()
        self.assertTrue("Cannot sleep while hungry" in str(contex.exception))

    def test_cat_not_sleepy_after_sleeping(self):
        c = Cat("Flerken")
        c.eat()
        c.sleep()
        self.assertFalse(c.sleepy)


if __name__ == "__main__":
    unittest.main()