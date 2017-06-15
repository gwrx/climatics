import unittest
from climatics import temperature
from coins import acceptor

class TestTemperature(unittest.TestCase):

    temp = None

    def setUp(self):
        tempObj = temperature.outside()
        tempObj.updateWeaterData()
        self.temp = tempObj.toCelsius()
        
    def test_external_temperature(self):
        self.assertIsNotNone(self.temp)
        self.assertGreater(self.temp, 0)


if __name__ == '__main__':
    unittest.main()
