import unittest

''''
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
'''

from biosim.animals import Herbivore
from biosim.Cell import Lowland

def test_simple_sorting():
    '''
    This is a test that checks if the herbivores get sorted in a list based on ascending
    phi-value.
    '''
    c = Lowland()
    c.herbivores_pop = [Herbivore(weight=35, a=3), Herbivore(weight=41, a=8),
                        Herbivore(weight=20, a=6)]
    liste1 = c.herbivores_pop
    liste2 = [liste1[0].phi, liste1[1].phi, liste1[2].phi]
    liste2.sort()
    c.sorting_animals(pop=c.herbivores_pop, sort_by='phi')
    liste3 = [c.sorted_herbivores_pop[0].phi, c.sorted_herbivores_pop[1].phi,
              c.sorted_herbivores_pop[2].phi]
    assert liste2 == liste3

'''
def test_available_fodder_function():
    
    #This is a test that checks if the cell gets it maximum amount of fodder back
    #with the help of the available fodder function
    
    c = Lowland()
    available_fodder = 800
    c.available_fodder_function()
    assert c.af == available_fodder
'''

def test_fodder_eaten():
    c = Lowland()
    c.herbivores_pop = [Herbivore(weight=35, a=3), Herbivore(weight=41, a=8),
                        Herbivore(weight=20, a=6), Herbivore(weight=35, a=3),
                        Herbivore(weight=41, a=8), Herbivore(weight=20, a=6)]
    c.make_herbivores_eat()
    assert c.af == 800 - 6 * 10

def test_gain_weight_after_eating(): # får den kun til å fungere på ett dyr
    c = Lowland()
    c.herbivores_pop = [Herbivore(weight=36, a=3), Herbivore(weight=41, a=8),
                        Herbivore(weight=20, a=6), Herbivore(weight=35, a=3),
                        Herbivore(weight=41, a=8), Herbivore(weight=20, a=6)]
    weight = [k.weight for k in c.herbivores_pop]

    c.make_herbivores_eat()
    weight2 = [k.weight for k in c.herbivores_pop]
    weight.sort()
    weight2.sort()

    assert [k + 9 for k in weight] == weight2


def test_newborn_added_to_list():
    c = Lowland()
    c.herbivores_pop = [Herbivore(weight=35, a=3), Herbivore(weight=41, a=8),
                        Herbivore(weight=20, a=6), Herbivore(weight=35, a=3),
                        Herbivore(weight=41, a=8), Herbivore(weight=20, a=6)]
    length = len(c.herbivores_pop)
    #for k in range(len(c.herbivores_pop)):
        #c.herbivores_pop[k].given_birth = False
    c.newborn_animals()
    assert len(c.herbivores_pop) == length + c.new


def test_mother_lost_weight():  # fungerer hver gang om mocker fungerer
    c = Lowland()
    c.herbivores_pop = [Herbivore(weight=50, a=3), Herbivore(weight=40, a=3)]
    weight = [k.weight for k in c.herbivores_pop]

    c.newborn_animals()
    after = [c.herbivores_pop[0], c.herbivores_pop[1]]

    newborn_weight = [k.newborn_birth_weight for k in after]
    after_weight = [k.weight for k in after]

    for k in range(len(weight)):
        assert after_weight[k] == weight[k] - Herbivore.p['zeta'] * newborn_weight[k]


def test_count_animals():
    c = Lowland()
    c.herbivores_pop = [Herbivore(weight=35, a=3), Herbivore(weight=41, a=8),
                        Herbivore(weight=20, a=6), Herbivore(weight=35, a=3),
                        Herbivore(weight=41, a=8), Herbivore(weight=20, a=6)]
    c.counting_animals()
    assert c.N == len(c.herbivores_pop)

def test_aging():
    c = Lowland()
    c.herbivores_pop = [Herbivore(weight=35, a=3), Herbivore(weight=41, a=8),
                        Herbivore(weight=20, a=6), Herbivore(weight=35, a=3),
                        Herbivore(weight=41, a=8), Herbivore(weight=20, a=6)]
    liste = []
    for ani in range(len(c.herbivores_pop)):
        liste.append(c.herbivores_pop[ani].a)
    c.make_animals_age()
    for k in range(len(c.herbivores_pop)):
        assert c.herbivores_pop[k].a == liste[k] + 1

def test_yearly_weight_loss():
    c = Lowland()
    h = Herbivore()

    liste = []
    for ani in range(len(c.herbivores_pop)):
        liste.append(c.herbivores_pop[ani].weight)
    c.make_animals_lose_weight()
    for k in range(len(c.herbivores_pop)):
        assert c.herbivores_pop[k].weight == liste[k] - h.p['eta'] * liste[k]

def test_animal_removed_after_death():
    c = Lowland()
    c.herbivores_pop = [Herbivore(weight=35, a=3), Herbivore(weight=41, a=8),
                        Herbivore(weight=20, a=6), Herbivore(weight=35, a=3),
                        Herbivore(weight=41, a=8), Herbivore(weight=20, a=6)]
    list = c.herbivores_pop
    c.dead_animals_natural_cause()

    assert len(c.herbivores_pop) == len(list) - c.dead

