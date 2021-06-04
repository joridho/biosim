import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

from biosim.Cell import cell
from Herbivore import herbivore

def test_simple_sorting():
    c = cell()
    c.herbivore_pop = [herbivore(weight=35,a=3), herbivore(weight=41,a=8),herbivore(weight=20,a=6)]



