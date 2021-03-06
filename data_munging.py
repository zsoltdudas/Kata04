import unittest
from utils import file_handling


class data_munging(unittest.TestCase, file_handling):
    def setUp(self):
        self.spread = []

    def test_weather(self):
        weather_data = self.read_file("weather.dat")
        smallest = self.smallest_difference(weather_data, 1, 2)

        print "Day with smallest spread: ", smallest + 1

    def test_football(self):
        league = self.read_file("football.dat")
        smallest = self.smallest_difference(league, 6, 8)

        print "Smallest goal difference: ", league[smallest][1]

if __name__ == '__main__':
    unittest.main()
