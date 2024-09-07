import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    
    def setUp(self):
        print(f"Setting up for {self._testMethodName}...")

    def tearDown(self):
        print(f"Tearing down after {self._testMethodName}...")

    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(1, -2), -1)
        self.assertEqual(add(-1, 2), 1)

if __name__ == '__main__':
    unittest.main()
    
