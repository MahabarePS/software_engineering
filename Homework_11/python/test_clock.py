import unittest
from Clock import Clock

class TestClock(unittest.TestCase):

    def test_add_hour(self):
        clock = Clock(10, 30, 45)
        clock.add_hour()
        self.assertEqual(clock.hours, 11)

    def test_add_minute(self):
        clock = Clock(10, 30, 45)
        clock.add_minute()
        self.assertEqual(clock.minutes, 31)

    def test_add_second(self):
        clock = Clock(10, 30, 45)
        clock.add_second()
        self.assertEqual(clock.seconds, 46)

    def test_get_24_hour_format(self):
        clock = Clock(10, 30, 45)
        self.assertEqual(clock.get_24_hour_format(), "10:30:45")

    def test_get_12_hour_format(self):
        clock = Clock(10, 30, 45)
        self.assertEqual(clock.get_12_hour_format(), "10:30:45 AM")

if __name__ == '__main__':
    unittest.main()
