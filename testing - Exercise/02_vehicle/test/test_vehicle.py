from unittest import TestCase

from project.vehicle import Vehicle


class TestVehicle(TestCase):

    FUEL = 100
    HORSE_POWER = 120
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.FUEL, self.HORSE_POWER)

    def test_vehicle_init(self):
        self.assertEqual(self.vehicle.fuel, self.FUEL)
        self.assertEqual(self.vehicle.horse_power, self.HORSE_POWER)
        self.assertEqual(self.vehicle.capacity, self.FUEL)
        self.assertEqual(self.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_raises_error_when_fuel_not_enough(self):
        with self.assertRaises(Exception) as error:
            self.vehicle.drive(100)
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual("Not enough fuel", str(error.exception))

    def test_drive_when_distance_is_reachable(self):
        distance = 50
        fuel_needed = self.DEFAULT_FUEL_CONSUMPTION * distance

        self.vehicle.drive(distance)

        expected_result = self.FUEL - fuel_needed
        self.assertEqual(expected_result, self.vehicle.fuel)

    def test_drive_with_max_possible_distance(self):
        distance = self.FUEL / self.DEFAULT_FUEL_CONSUMPTION

        self.vehicle.drive(distance)

        self.assertEqual(0, self.vehicle.fuel)

    def test_refuel_raises_error_when_capacity_overflow(self):
        with self.assertRaises(Exception) as error:
            self.vehicle.refuel(self.vehicle.capacity + 1)
        self.assertEqual("Too much fuel", str(error.exception))

    def test_refuel_increases_fuel_in_the_car(self):
        fuel_amount = 20
        self.vehicle.fuel -= fuel_amount

        self.vehicle.refuel(fuel_amount)

        self.assertEqual(self.FUEL, self.vehicle.fuel)

    def test_vehicle_str_returns_proper_string_message(self):
        actual_result = str(self.vehicle)
        expected_result = f"The vehicle has {self.HORSE_POWER} " \
               f"horse power with {self.FUEL} fuel left and {self.DEFAULT_FUEL_CONSUMPTION} fuel consumption"

        self.assertEqual(actual_result, expected_result)


