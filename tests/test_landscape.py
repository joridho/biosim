import unittest

''''
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
'''

from biosim.animals import herbivore
from biosim.Cell import lowland

def test_adding_animals():
    l = lowland()
    l.adding_animals()
    assert len(l.herbivores_pop) == 50

def test_simple_sorting():
    '''
    This is a test that checks if the herbivores get sorted in a list based on ascending
    phi-value.
    '''
    c = lowland()
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
    
    c = lowland()
    available_fodder = 800
    c.available_fodder_function()
    assert c.af == available_fodder


def test_fodder_eaten():
    c = lowland()
    c.herbivores_pop = [herbivore(weight=35, a=3), herbivore(weight=41, a=8),
                        herbivore(weight=20, a=6), herbivore(weight=35, a=3),
                        herbivore(weight=41, a=8), herbivore(weight=20, a=6)]
    c.make_herbivores_eat()
    assert c.af == 800 - 6 * 10

def test_gain_weight_after_eating():
    c = lowland()
    c.adding_animals()
    list = c.herbivores_pop
    weight = []
    for k in range(len(list)):
        weight.append(list[k].weight)
    c.make_herbivores_eat()
    list_after = c.herbivores_pop
    for k in range(len(list)):
        assert list_after[k].weight == weight[k] + list[k].p['beta'] * 10#list[k].F_consumption


def test_fodder_eaten():
    'Check if there all the animals are still in herbivores_pop after make herbivores eat'
    l = lowland()
    l.herbivores_pop = [herbivore(weight=35, a=3), herbivore(weight=41, a=8),
                        herbivore(weight=20, a=6), herbivore(weight=35, a=3),
                        herbivore(weight=41, a=8), herbivore(weight=20, a=6)]
    l.make_herbivores_eat()
    assert len(l.herbivores_pop) == 6


def test_newborn_added_to_list():
    c = lowland()
    c.herbivores_pop = [herbivore(weight=35, a=3), herbivore(weight=41, a=8),
                        herbivore(weight=20, a=6), herbivore(weight=35, a=3),
                        herbivore(weight=41, a=8), herbivore(weight=20, a=6)]
    length = len(c.herbivores_pop)
    #for k in range(len(c.herbivores_pop)):
        #c.herbivores_pop[k].given_birth = False
    c.newborn_animals()
    assert len(c.herbivores_pop) == length + c.new


def test_mother_lost_weight():
    c = lowland()
    c.herbivores_pop = [herbivore(weight=36, a=3), herbivore(weight=40, a=3)]
    list = c.herbivores_pop
    weight = []
    for k in range(len(list)):
        weight.append(list[k].weight)
    c.newborn_animals()
    list2 = c.herbivores_pop
    for k in range(len(weight)):
        assert list2[k].weight == weight[k] - list[k].p['zeta'] * list[k].newborn_birth_weight


def test_count_animals():
    c = lowland()
    c.adding_animals()
    c.counting_animals()
    assert c.N == 50


def test_reset_available_fodder():  # testen fungerer ikke siden make_herbivores_eat ikke fungerer
    c = lowland()
    c.herbivores_pop = [herbivore(weight=35, a=3), herbivore(weight=41, a=8),
                        herbivore(weight=20, a=6), herbivore(weight=35, a=3),
                        herbivore(weight=41, a=8),
                        herbivore(weight=20, a=6)]
    c.make_herbivores_eat()
    c.reset_fodder()
    assert c.af == c.p['f_max']


def test_reset_appetite():  # testen fungerer ikke siden make_herbivores_eat ikke fungerer
    c = lowland()
    c.herbivores_pop = [herbivore(weight=35, a=3), herbivore(weight=41, a=8),
                        herbivore(weight=20, a=6), herbivore(weight=35, a=3),
                        herbivore(weight=41, a=8), herbivore(weight=20, a=6)]
    c.make_herbivores_eat()
    c.reset_appetite()
    for k in range(len(c.herbivores_pop)):
        assert c.herbivores_pop[k].p['F'] == 10


def test_reset_given_birth():
    c = lowland()
    c.herbivores_pop = [herbivore(weight=35, a=3), herbivore(weight=41, a=8),
                        herbivore(weight=20, a=6), herbivore(weight=35, a=3),
                        herbivore(weight=41, a=8), herbivore(weight=20, a=6)]
    for k in range(len(c.herbivores_pop)):
        c.herbivores_pop[k].given_birth = True
    c.reset_given_birth()
    for k in range(len(c.herbivores_pop)):
        assert c.herbivores_pop[k].given_birth == False


def test_aging():
    c = lowland()
    c.adding_animals()
    liste = []
    for ani in range(len(c.herbivores_pop)):
        liste.append(c.herbivores_pop[ani].a)
    c.make_animals_age()
    for k in range(len(c.herbivores_pop)):
        assert c.herbivores_pop[k].a == liste[k] + 1

def test_yearly_weight_loss():
    c = lowland()
    h = herbivore()
    c.adding_animals()
    liste = []
    for ani in range(len(c.herbivores_pop)):
        liste.append(c.herbivores_pop[ani].weight)
    c.make_animals_lose_weight()
    for k in range(len(c.herbivores_pop)):
        assert c.herbivores_pop[k].weight == liste[k] - h.p['eta'] * liste[k]

def test_animal_removed_after_death():
    c = lowland()
    c.adding_animals()
    list = c.herbivores_pop
    c.dead_animals_natural_cause()

    assert len(c.herbivores_pop) == len(list) - c.dead

