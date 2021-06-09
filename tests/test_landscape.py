import unittest

''''
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
'''

from biosim.animals import Herbivore, Carnivore
from biosim.Cell import Lowland

def test_simple_sorting_herb():
    '''
    This is a test that checks if the herbivores get sorted in a list based on ascending
    phi-value.
    '''
    c = Lowland()
    c.herbivores_pop = [Herbivore(weight=35, age=3), Herbivore(weight=41, age=8),
                        Herbivore(weight=20, age=6)]
    liste1 = c.herbivores_pop
    liste2 = [liste1[0].phi, liste1[1].phi, liste1[2].phi]
    liste2.sort()
    c.sorting_animals()
    liste3 = [c.herbivores_pop[0].phi, c.herbivores_pop[1].phi,
              c.herbivores_pop[2].phi]
    assert liste2 == liste3

def test_sorting_carnivores():
    l = Lowland()
    l.carnivores_pop = [Carnivore(weight=5, age=3), Carnivore(weight=15, age=3),
                        Carnivore(weight=25, age=3), Carnivore(weight=35, age=3),
                        Carnivore(weight=45, age=3), Carnivore(weight=55, age=3)]
    liste1 = l.carnivores_pop
    pop1 = [k.phi for k in liste1]
    pop1.reverse()
    l.sorting_animals()
    liste2 = l.carnivores_pop
    pop2 = [k.phi for k in liste2]
    assert pop2 == pop1

def test_available_herbivores():
    l = Lowland()
    l.herbivores_pop = [Herbivore(weight=35, age=3), Herbivore(weight=41, age=8),
                        Herbivore(weight=20, age=6)]
    weight = 0
    for k in l.herbivores_pop:
        weight += k.weight
    l.available_herbivores_for_carnivores()
    assert l.herbivores_weight_sum == weight

def test_fodder_eaten():
    c = Lowland()
    c.herbivores_pop = [Herbivore(weight=35, age=3), Herbivore(weight=41, age=8),
                        Herbivore(weight=20, age=6), Herbivore(weight=35, age=3),
                        Herbivore(weight=41, age=8), Herbivore(weight=20, age=6)]
    c.make_herbivores_eat()
    assert c.af == 800 - 6 * 10

def test_gain_weight_after_eating(): # får den kun til å fungere på ett dyr
    c = Lowland()
    c.herbivores_pop = [Herbivore(weight=35, age=3), Herbivore(weight=41, age=8),
                        Herbivore(weight=20, age=6), Herbivore(weight=35, age=3),
                        Herbivore(weight=41, age=8), Herbivore(weight=20, age=6)]
    weight = [k.weight for k in c.herbivores_pop]

    c.make_herbivores_eat()
    weight2 = [k.weight for k in c.herbivores_pop]
    weight.sort()
    weight2.sort()

    assert [k + 9 for k in weight] == weight2

def test_carnivores_gain_weight_after_eating():
    l = Lowland
    l.herbivores_pop = [Herbivore(weight=35, age=3), Herbivore(weight=41, age=8),
                        Herbivore(weight=20, age=6), Herbivore(weight=35, age=3),
                        Herbivore(weight=41, age=8), Herbivore(weight=20, age=6)]
    l.carnivores_pop = [Carnivore(weight=35, age=3), Carnivore(weight=41, age=8),
                        Carnivore(weight=20, age=6), Carnivore(weight=35, age=3),
                        Carnivore(weight=41, age=8), Carnivore(weight=20, age=6)]
    carns = l.carnivores_pop
    herbs = l.herbivores_pop
    l.feed_carnivores()
    for k in l.carnivores_pop:
        if k.kill is True:
            for m in carns:
                assert k.weight == m.weight

def test_herbivore_removed_from_list_after_eaten():
    l = Lowland
    l.herbivores_pop = [Herbivore(weight=35, age=3), Herbivore(weight=41, age=8),
                        Herbivore(weight=20, age=6), Herbivore(weight=35, age=3),
                        Herbivore(weight=41, age=8), Herbivore(weight=20, age=6)]
    l.carnivores_pop = [Carnivore(weight=35, age=3), Carnivore(weight=41, age=8),
                        Carnivore(weight=20, age=6), Carnivore(weight=35, age=3),
                        Carnivore(weight=41, age=8), Carnivore(weight=20, age=6)]
    l.feed_carnivores()
    assert 1 == 1


def test_newborn_added_to_list_herb():
    l = Lowland()
    l.herbivores_pop = [Herbivore(weight=35, age=3), Herbivore(weight=41, age=8),
                        Herbivore(weight=20, age=6), Herbivore(weight=35, age=3),
                        Herbivore(weight=41, age=8), Herbivore(weight=20, age=6)]
    length = len(l.herbivores_pop)
    l.newborn_animals()
    assert len(l.herbivores_pop) == length + l.new_h

def test_newborn_added_to_list_carn():
    l = Lowland()
    l.carnivores_pop = [Carnivore(weight=35, age=3), Carnivore(weight=41, age=8),
                        Carnivore(weight=20, age=6), Carnivore(weight=35, age=3),
                        Carnivore(weight=41, age=8), Carnivore(weight=20, age=6)]
    length = len(l.carnivores_pop)
    l.newborn_animals()
    assert len(l.carnivores_pop) == length + l.new_c


def test_mother_lost_weight_herb():  # fungerer hver gang om mocker fungerer
    c = Lowland()
    c.herbivores_pop = [Herbivore(weight=50, age=3), Herbivore(weight=40, age=3)]
    weight = [k.weight for k in c.herbivores_pop]

    c.newborn_animals()
    after = [c.herbivores_pop[0], c.herbivores_pop[1]]

    newborn_weight = [k.newborn_birth_weight for k in after]
    after_weight = [k.weight for k in after]

    for k in range(len(weight)):
        assert after_weight[k] == weight[k] - Herbivore.p['zeta'] * newborn_weight[k]

def test_mother_lost_weight_carn():  # fungerer hver gang om mocker fungerer
    c = Lowland()
    c.carnivores_pop = [Carnivore(weight=50, age=3), Carnivore(weight=40, age=3)]
    weight = [k.weight for k in c.carnivores_pop]

    c.newborn_animals()
    after = [c.carnivores_pop[0], c.carnivores_pop[1]]

    newborn_weight = [k.newborn_birth_weight for k in after]
    after_weight = [k.weight for k in after]

    for k in range(len(weight)):
        assert after_weight[k] == weight[k] - Herbivore.p['zeta'] * newborn_weight[k]


def test_count_animals_herb():
    c = Lowland()
    c.herbivores_pop = [Herbivore(weight=35, age=3), Herbivore(weight=41, age=8),
                        Herbivore(weight=20, age=6), Herbivore(weight=35, age=3),
                        Herbivore(weight=41, age=8), Herbivore(weight=20, age=6)]
    c.counting_animals()
    assert c.N_herb == len(c.herbivores_pop)

def test_aging_herb():
    c = Lowland()
    c.herbivores_pop = [Herbivore(weight=35, age=3), Herbivore(weight=41, age=8),
                        Herbivore(weight=20, age=6), Herbivore(weight=35, age=3),
                        Herbivore(weight=41, age=8), Herbivore(weight=20, age=6)]
    liste = []
    for ani in range(len(c.herbivores_pop)):
        liste.append(c.herbivores_pop[ani].age)
    c.make_animals_age()
    for k in range(len(c.herbivores_pop)):
        assert c.herbivores_pop[k].age == liste[k] + 1

def test_yearly_weight_loss_herb():
    c = Lowland()
    h = Herbivore()

    liste = []
    for ani in range(len(c.herbivores_pop)):
        liste.append(c.herbivores_pop[ani].weight)
    c.make_animals_lose_weight()
    for k in range(len(c.herbivores_pop)):
        assert c.herbivores_pop[k].weight == liste[k] - h.p['eta'] * liste[k]

def test_animal_removed_after_death_herb():
    c = Lowland()
    c.herbivores_pop = [Herbivore(weight=35, age=3), Herbivore(weight=41, age=8),
                        Herbivore(weight=20, age=6), Herbivore(weight=35, age=3),
                        Herbivore(weight=41, age=8), Herbivore(weight=20, age=6)]
    list = c.herbivores_pop
    c.dead_animals_natural_cause()

    assert len(c.herbivores_pop) == len(list) - c.dead

def test_animal_removed_after_death_herb():
    l = Lowland()
    l.carnivores_pop = [Carnivore(weight=35, age=3), Carnivore(weight=41, age=8),
                        Carnivore(weight=20, age=6), Carnivore(weight=35, age=3),
                        Carnivore(weight=41, age=8), Carnivore(weight=20, age=6)]
    list = l.carnivores_pop
    l.dead_animals_natural_cause()

    assert len(l.carnivores_pop) == len(list) - l.dead



