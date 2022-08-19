import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import main_gui as main_gui


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(main_gui._title, "Hello World")  # add assertion here


if __name__ == '__main__':
    unittest.main()
