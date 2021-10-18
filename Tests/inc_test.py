import unittest

from main.inc import inc

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.inc = inc()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.inc, inc)

if __name__ == '__main__':
    unittest.main()