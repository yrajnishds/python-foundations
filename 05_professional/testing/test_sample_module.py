import unittest
from sample_module import add, is_even


class TestSampleModule(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(5))


if __name__ == "__main__":
    unittest.main()