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
    liste3 = [c.sorted_herbivores_pop[0].phi,c.sorted_herbivores_pop[1].phi,
              c.sorted_herbivores_pop[2].phi]
    assert liste2 == liste3

def test_fodder_eaten():
    c = cell()
    c.herbivores_pop = [herbivore(weight=35, a=3), herbivore(weight=41, a=8),
                       herbivore(weight=20, a=6),herbivore(weight=35, a=3), herbivore(weight=41, a=8),
                       herbivore(weight=20, a=6)]
    c.make_herbivores_eat()
    assert c.available_fodder == 0

def test_newborn_added_to_list():
    c = cell()
    c.herbivores_pop = [herbivore(weight=35, a=3), herbivore(weight=41, a=8),
                        herbivore(weight=20, a=6), herbivore(weight=35, a=3),
                        herbivore(weight=41, a=8),
                        herbivore(weight=20, a=6)]
    c.newborn_animals()
    assert len(c.herbivores_pop) == 7

def test_mother_lost_weight():
    h = herbivore()
    h.birth_probability(N=6)
    c = cell()
    c.herbivores_pop = [herbivore(weight=35, a=3)]
    c.newborn_animals()
    assert h.weight == 35 - h.newborn_birth_weight

def test_count_animals():
    c = cell()
    c.herbivores_pop = [herbivore(weight=35, a=3), herbivore(weight=41, a=8),
                        herbivore(weight=20, a=6), herbivore(weight=35, a=3),
                        herbivore(weight=41, a=8),
                        herbivore(weight=20, a=6)]
    c.counting_animals()
    assert c.N == 6

def test_reset_available_fodder():
    c = cell()
    c.herbivores_pop = [herbivore(weight=35, a=3), herbivore(weight=41, a=8),
                        herbivore(weight=20, a=6), herbivore(weight=35, a=3),
                        herbivore(weight=41, a=8),
                        herbivore(weight=20, a=6)]
    c.make_herbivores_eat()
    c.reset_fodder()
    assert c.available_fodder == c.p['f_max']

def test_reset_appetite():
    c = cell()
    c.herbivores_pop = [herbivore(weight=35, a=3), herbivore(weight=41, a=8),
                        herbivore(weight=20, a=6), herbivore(weight=35, a=3),
                        herbivore(weight=41, a=8),
                        herbivore(weight=20, a=6)]
    c.make_herbivores_eat()
    c.reset_appetite()
    for k in range(len(c.herbivores_pop)):
        assert c.herbivores_pop[k].p['F'] == 10












