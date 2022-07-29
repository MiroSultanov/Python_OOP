# Create a class WorkerTests
# In judge you need to submit just the WokerTests class, with the unittest module imported.
# Create the following tests:
# •	Test if the worker is initialized with the correct name, salary, and energy
# •	Test if the worker's energy is incremented after the rest method is called
# •	Test if an error is raised if the worker tries to work with negative energy or equal to 0
# •	Test if the worker's money is increased by his salary correctly after the work method is called
# •	Test if the worker's energy is decreased after the work method is called	
# •	Test if the get_info method returns the proper string with correct values


import unittest

class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


class WorkerTests(unittest.TestCase):

    def setUp(self) -> None:
        self.name = 'Me'
        self.salary = 1000
        self.energy = 50

        self.w = Worker(self.name, self.salary, self.energy)

    def test_init(self):
        self.assertEqual(self.w.name, self.name)
        self.assertEqual(self.w.salary, self.salary)
        self.assertEqual(self.w.energy, self.energy)

    def test_energy_incremented_after_rest(self):
        start_energy = self.w.energy
        self.w.rest()
        self.assertGreater(self.w.energy, start_energy)

    def test_error_if_working_with_zero_or_negative_energy(self):
        self.w.energy = 0
        with self.assertRaises(Exception) as contex:
            self.w.work()
        self.assertTrue('Not enough energy' in str(contex.exception))
        self.w.energy = -1
        with self.assertRaises(Exception) as contex:
            self.w.work()
        self.assertTrue('Not enough energy' in str(contex.exception))

    def test_money_increased_with_salary_after_working(self):
        expected = self.w.salary + self.w.money
        self.w.work()
        self.assertEqual(self.w.money, expected)

    def test_worker_energy_decreased_after_work(self):
        starting_energy = self.w.energy
        self.w.work()
        self.assertLess(self.w.energy, starting_energy)

    def test_get_info_method(self):
        expected = f'{self.w.name} has saved {self.w.money} money.'
        self.assertEqual(self.w.get_info(), expected)


if __name__ == '__main__':
    unittest.main()
