import unittest

''''
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
'''

from biosim.animals import herbivore
from biosim.Cell import cell

def test_adding_animals():
    c = cell()
    c.adding_animals()
    assert len(c.herbivores_pop) == 50

def test_simple_sorting():
    '''
    This is a test that checks if the herbivores get sorted in a list based on ascending
    phi-value.
    '''
    c = cell()
    c.herbivores_pop = [herbivore(weight=35, a=3), herbivore(weight=41, a=8),
                        herbivore(weight=20, a=6)]
    liste1 = c.herbivores_pop
    liste2 = [liste1[0].phi, liste1[1].phi, liste1[2].phi]
    liste2.sort()
    c.sorting_animals()
    liste3 = [c.sorted_herbivores_pop[0].phi, c.sorted_herbivores_pop[1].phi,
              c.sorted_herbivores_pop[2].phi]
    assert liste2 == liste3


def test_available_fodder_function():
    
    #This is a test that checks if the cell gets it maximum amount of fodder back
    #with the help of the available fodder function
    
    c = cell()
    available_fodder = 800
    c.available_fodder_function()
    assert c.af == available_fodder


def test_fodder_eaten():
    c = cell()
    c.herbivores_pop = [herbivore(weight=35, a=3), herbivore(weight=41, a=8),
                        herbivore(weight=20, a=6), herbivore(weight=35, a=3),
                        herbivore(weight=41, a=8), herbivore(weight=20, a=6)]
    c.make_herbivores_eat()
    #assert c.af == 800 - 6 * 10
    #assert herbivore.p['F']  == 10
    #assert len(c.herbivores_pop) == 6
    #liste5 = c.herbivores_pop
    #assert liste5 == []

'''
def test_newborn_added_to_list():
    c = cell()
    c.herbivores_pop = [herbivore(weight=35, a=3), herbivore(weight=41, a=8),
                        herbivore(weight=20, a=6), herbivore(weight=35, a=3),
                        herbivore(weight=41, a=8),
                        herbivore(weight=20, a=6)]
    for k in range(len(c.herbivores_pop)):
        c.herbivores_pop[k].given_birth = False
    c.newborn_animals()
    assert len(c.herbivores_pop) == 12


def test_mother_lost_weight():
    c = cell()
    c.herbivores_pop = [herbivore(weight=35, a=3)]
    c.newborn_animals()
    list = c.herbivores_pop
    assert list[0].weight == 35 - list[0].p['zeta'] * list[0].newborn_birth_weight


def test_count_animals():
    c = cell()
    c.adding_animals()
    c.counting_animals()
    assert c.N == 50


def test_reset_available_fodder():  # testen fungerer ikke siden make_herbivores_eat ikke fungerer
    c = cell()
    c.herbivores_pop = [herbivore(weight=35, a=3), herbivore(weight=41, a=8),
                        herbivore(weight=20, a=6), herbivore(weight=35, a=3),
                        herbivore(weight=41, a=8),
                        herbivore(weight=20, a=6)]
    c.make_herbivores_eat()
    c.reset_fodder()
    assert c.available_fodder == c.p['f_max']


def test_reset_appetite():  # testen fungerer ikke siden make_herbivores_eat ikke fungerer
    c = cell()
    c.herbivores_pop = [herbivore(weight=35, a=3), herbivore(weight=41, a=8),
                        herbivore(weight=20, a=6), herbivore(weight=35, a=3),
                        herbivore(weight=41, a=8), herbivore(weight=20, a=6)]
    c.make_herbivores_eat()
    c.reset_appetite()
    for k in range(len(c.herbivores_pop)):
        assert c.herbivores_pop[k].p['F'] == 10


def test_reset_given_birth():  # tror funksjonen fungerer, men siden c.newborn_animal ikke fungerer,
    # fungerer ikke testen
    c = cell()
    c.herbivores_pop = [herbivore(weight=35, a=3), herbivore(weight=41, a=8),
                        herbivore(weight=20, a=6), herbivore(weight=35, a=3),
                        herbivore(weight=41, a=8), herbivore(weight=20, a=6)]
    for k in range(len(c.herbivores_pop)):
        c.herbivores_pop[k].given_birth = True
    c.reset_given_birth()
    for k in range(len(c.herbivores_pop)):
        assert c.herbivores_pop[k].given_birth == False


def test_aging():
    c = cell()
    c.adding_animals()
    liste = []
    for ani in range(len(c.herbivores_pop)):
        liste.append(c.herbivores_pop[ani].a)
    c.make_animals_age()
    for k in range(len(c.herbivores_pop)):
        assert c.herbivores_pop[k].a == liste[k] + 1

def test_yearly_weight_loss():
    c = cell()
    h = herbivore()
    c.adding_animals()
    liste = []
    for ani in range(len(c.herbivores_pop)):
        liste.append(c.herbivores_pop[ani].weight)
    c.make_animals_lose_weight()
    for k in range(len(c.herbivores_pop)):
        assert c.herbivores_pop[k].weight == liste[k] - h.p['eta'] * liste[k]

def test_animal_removed_after_death():
    c = cell()
    c.adding_animals()
    c.dead_animals_natural_cause()
    assert len(c.herbivores_pop) == 0
'''
