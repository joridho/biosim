import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

from biosim.animals import herbivore
from biosim.Cell import cell

def test_simple_sorting():
    c = cell()
    c.herbivores_pop = [herbivore(weight=35,a=3), herbivore(weight=41,a=8),herbivore(weight=20,a=6)]
    liste1 = c.herbivores_pop
    liste2 = [liste1[0].phi, liste1[1].phi, liste1[2].phi]
    liste2.sort()
    c.sorting_animals()
    assert liste2 == c.sorted_herbivores_pop

def test_fodder_eaten():
    c = cell()
    c.herbivores_pop = [herbivore(weight=35, a=3), herbivore(weight=41, a=8),
                       herbivore(weight=20, a=6)]
    c.make_herbivores_eat()
    assert c.available_fodder == 0






