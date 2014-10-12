import unittest

from model import BikePart, Wheel, RoadWheel, MountainWheel, CarbonFrame, \
    BicycleModel, Customer, BicycleManufacturer, BicycleShop


class BikePartTest(unittest.TestCase):

    def setUp(self):
        self._bikePart = BikePart(10, 100)

    def get_cost(self):
        self.assertEqual(self._bikePart.get_cost(), 10)

    def get_weight(self):
        self.assertEqual(self._bikePart.get_weight(), 100)


class WheelTest(unittest.TestCase):

    def setUp(self):
        self._wheel = Wheel('myWheel', 10, 100)

    def get_name(self):
        self.assertEqual(self._wheel.get_name(), 'myWheel')


class BicyleModelTest(unittest.TestCase):

    def setUp(self):
        self._frame = CarbonFrame(10, 100)
        self._frontWheel = RoadWheel("Front RoadWheel", 10, 100)
        self._backWheel1 = MountainWheel("Back MountainWheel", 10, 100)
        self._backWheel2 = RoadWheel("Back RoadWheel", 10, 100)
        self._bike = BicycleModel(
            "Good Build", self._frontWheel, self._backWheel2, self._frame
        )

    def test_different_heel_type_init(self):
        self.assertRaises(
            AssertionError,
            BicycleModel,
            "Error Build",
            self._frontWheel,
            self._backWheel1,
            self._frame
        )

    def test_get_cost(self):
        self.assertEqual(30, self._bike.get_cost())

    def test_get_weight(self):
        self.assertEqual(300, self._bike.get_weight())

    def test_change_cost(self):
        self._bike.change_cost_by_percentage(0.1)
        self.assertEqual(33, self._bike.get_cost())


class CustomerTest(unittest.TestCase):

    def setUp(self):
        self._frame = CarbonFrame(10, 100)
        self._frontWheel = RoadWheel("Front RoadWheel", 10, 100)
        self._backWheel1 = MountainWheel("Back MountainWheel", 10, 100)
        self._backWheel2 = RoadWheel("Back RoadWheel", 10, 100)
        self._bike = BicycleModel(
            "Good Build", self._frontWheel, self._backWheel2, self._frame
        )
        self._customer = Customer('Customer', 10000)

    def test_buy_bike(self):
        self._customer.buy_bike(self._bike)
        self.assertNotEqual(None, self._customer.get_bike())
        self.assertEqual(self._customer.get_funds(), 9970)


class BicycleManufacturerTest(unittest.TestCase):

    def setUp(self):
        self._manufacturer = BicycleManufacturer("Manufacturer", 0.2)

    def test_generate_bikes(self):
        bikes = self._manufacturer.generate_bikes()
        self.assertEqual(len(bikes), 3)


class generate_bikes(unittest.TestCase):

    def setUp(self):
        self._manufacturer1 = BicycleManufacturer("Manufacturer1", 0.2)
        self._manufacturer2 = BicycleManufacturer("Manufacturer2", 0.3)
        self._shop = BicycleShop(
            "Shop", 0.2, [self._manufacturer1, self._manufacturer2]
        )
        self._customer = Customer('Customer', 10000)

    def get_bikes_from_manufacturer(self):
        self.assertEqual(6, len(self._shop.get_inventory()))

    def test_sell_bike(self):
        for i in range(6):
            self._shop.sell_bike(self._customer, self._shop.get_inventory()[0])
            self.assertEqual(6-(i+1), len(self._shop.get_inventory()))

if __name__ == "__main__":
    unittest.main()
