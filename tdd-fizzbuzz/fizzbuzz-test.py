import unittest
from fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def test_first_element(self):
        result = fizzbuzz(1)
        self.assertEqual(result, 1)

    def test_second_element(self):
        result = fizzbuzz(2)
        self.assertEqual(result, 2)

    def test_for_three_return_fizz(self):
        result = fizzbuzz(3)
        self.assertEqual(result, "Fizz")

    def test_multiple_three_return_fizz(self):
        result = fizzbuzz(6)
        self.assertEqual(result, "Fizz")

    def test_five_return_buzz(self):
        result = fizzbuzz(5)
        self.assertEqual(result, "Buzz")

    def test_multiple_five_return_buzz(self):
        result = fizzbuzz(10)
        self.assertEqual(result, "Buzz")

    def test_multiple_three_and_five_return_fizzbuzz(self):
        result = fizzbuzz(15)
        self.assertEqual(result, "FizzBuzz")


if __name__ == "__main__":
    unittest.main()
