from unittest import TestCase

from project.train.train import Train


class TestTrain(TestCase):

    def setUp(self) -> None:
        self._TRAIN_FULL = "Train is full"
        self._PASSENGER_EXISTS = "Passenger {} Exists"
        self._PASSENGER_NOT_FOUND = "Passenger Not Found"
        self._PASSENGER_ADD = "Added passenger {}"
        self._PASSENGER_REMOVED = "Removed {}"
        self.train = Train('Fast', 10)

    def test_init(self):
        self.assertEqual(self.train.name, 'Fast')
        self.assertEqual(self.train.capacity, 10)
        self.assertListEqual(self.train.passengers, [])
        self.assertTrue(hasattr(self.train, 'add'))
        self.assertTrue(hasattr(self.train, 'remove'))

    def test_add_to_success(self):
        result = self.train.add('Miro')
        self.assertEqual(self._PASSENGER_ADD.format("Miro"), result)
        self.assertTrue("Miro" in self.train.passengers)
        self.assertEqual(len(self.train.passengers), 1)

    def test_add_capacity(self):
        self.train.capacity = 1
        self.train.add("Petya")
        with self.assertRaises(ValueError) as error:
            self.train.add("Miro")
        self.assertEqual(self._TRAIN_FULL, str(error.exception))
        self.assertListEqual(self.train.passengers, ["Petya"])

    def test_add_existing_passenger(self):
        self.train.add("Petya")
        with self.assertRaises(ValueError) as error:
            self.train.add("Petya")
        self.assertEqual(self._PASSENGER_EXISTS.format("Petya"), str(error.exception))

    def test_remove_success(self):
        self.train.add("Petya")
        self.train.add("Miro")
        result = self.train.remove("Petya")
        self.assertEqual(self._PASSENGER_REMOVED.format("Petya"), result)
        self.assertListEqual(self.train.passengers, ["Miro"])

    def test_non_existing_passenger(self):
        with self.assertRaises(ValueError) as error:
            self.train.remove("Miro")
        self.assertEqual(self._PASSENGER_NOT_FOUND.format("Miro"), str(error.exception))

    if __name__ == '__main__':
        unittest.main()



