import unittest
import fizz_buzz


class FizzBuzzTests(unittest.TestCase):

    def test_fizz(self):
        number = 6

        result = fizz_buzz.get_replay(number)
