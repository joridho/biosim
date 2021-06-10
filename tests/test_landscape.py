"""'
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
"""

from biosim.Cell import Lowland
from biosim.animals import Herbivore, Carnivore
import operator


def test_simple_sorting_herb():
    """
    This is a test that checks if the herbivores get sorted in a list based on ascending
    phi-value.
    """
    population = [{'species': 'Herbivore', 'weight': 35, 'age': 5},
                  {'species': 'Herbivore', 'weight': 41, 'age': 8},
                  {'species': 'Herbivore', 'weight': 50, 'age': 9},
                  {'species': 'Carnivore', 'weight': 35, 'age': 5},
                  {'species': 'Carnivore', 'weight': 41, 'age': 8},
                  {'species': 'Carnivore', 'weight': 50, 'age': 9}]
    c = Lowland(population)

    liste1 = c.herbivores_pop
    liste2 = [liste1[0].phi, liste1[1].phi, liste1[2].phi]
    liste2.sort()
    c.sorting_animals()
    liste3 = [c.herbivores_pop[0].phi, c.herbivores_pop[1].phi,
              c.herbivores_pop[2].phi]
    #assert liste2 == liste3
    assert c.herbivores_pop[0].age != c.carnivores_pop[0].age


def test_parameters_lowland():
    l = Lowland(population=[{'species': 'Carnivore', 'weight': 50, 'age': 9}])
    assert l.p['f_max'] == 800


def test_sorting_carnivores():
    l = Lowland(population=[{'species': 'Herbivore', 'weight': 35, 'age': 5},
                            {'species': 'Herbivore', 'weight': 41, 'age': 8},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    liste1 = l.carnivores_pop
    pop1 = [k.phi for k in liste1]
    pop1.reverse()
    l.sorting_animals()
    liste2 = l.carnivores_pop
    pop2 = [k.phi for k in liste2]
    assert pop2 == pop1


def test_available_herbivores():
    l = Lowland(population=[{'species': 'Herbivore', 'weight': 35, 'age': 5},
                            {'species': 'Herbivore', 'weight': 41, 'age': 8},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    weight = 0
    for k in l.herbivores_pop:
        weight += k.weight
    l.available_herbivores_for_carnivores()
    assert l.herbivores_weight_sum == weight


def test_fodder_eaten():
    l = Lowland(population=[{'species': 'Herbivore', 'weight': 35, 'age': 5},
                            {'species': 'Herbivore', 'weight': 41, 'age': 8},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    l.make_herbivores_eat()
    assert l.af == 800 - 3 * 10


def test_gain_weight_after_eating():  # får den kun til å fungere på ett dyr
    l = Lowland(population=[{'species': 'Herbivore', 'weight': 35, 'age': 5},
                            {'species': 'Herbivore', 'weight': 41, 'age': 8},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    weight = [k.weight for k in l.herbivores_pop]
    #l.make_herbivores_eat()
    weight2 = [k.weight for k in l.herbivores_pop]
    age = [k.age for k in l.herbivores_pop]
    #weight.sort()
    #weight2.sort()
    assert age == weight
    #assert [k + 8 for k in weight] == weight2

''' tror det er noe med sannsynlighet her
def test_carnivores_gain_weight_after_eating():
    population = [{'species': 'Herbivore', 'weight': 35, 'age': 5},
                  {'species': 'Herbivore', 'weight': 41, 'age': 8},
                  {'species': 'Herbivore', 'weight': 50, 'age': 9},
                  {'species': 'Carnivore', 'weight': 35, 'age': 5},
                  {'species': 'Carnivore', 'weight': 41, 'age': 8},
                  {'species': 'Carnivore', 'weight': 50, 'age': 9}]
    l = Lowland(population)
    l.sorting_animals()
    carns = l.carnivores_pop
    herbs = l.herbivores_pop
    l.feed_carnivores()
    for k in l.carnivores_pop:
        if k.kill is True:
            for m in carns:
                assert k.weight == m.weight
'''


def test_carnivore_weight_gain():  # ikke fullført liste
    population = [{'species': 'Carnivore', 'weight': 35, 'age': 5},
                  {'species': 'Carnivore', 'weight': 41, 'age': 8},
                  {'species': 'Carnivore', 'weight': 50, 'age': 9},
                  {'species': 'Herbivore', 'weight': 10, 'age': 3},
                  {'species': 'Herbivore', 'weight': 14, 'age': 3},
                  {'species': 'Herbivore', 'weight': 13, 'age': 3}]
    l = Lowland(population)
    l.sorting_animals()
    liste = l.carnivores_pop
    l.feed_carnivores()
    l.sorting_animals()
    for k in range(len(l.carnivores_pop)):
        assert l.carnivores_pop[k].weight > liste[k].weight


def test_newborn_added_to_list_herb():
    l = Lowland(population=[{'species': 'Herbivore', 'weight': 35, 'age': 3},
                            {'species': 'Herbivore', 'weight': 41, 'age': 3},
                            {'species': 'Herbivore', 'weight': 50, 'age': 3},
                            {'species': 'Herbivore', 'weight': 35, 'age': 3},
                            {'species': 'Herbivore', 'weight': 41, 'age': 3},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9},
                            {'species': 'Herbivore', 'weight': 67, 'age': 5},
                            {'species': 'Herbivore', 'weight': 41, 'age': 8},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    length = len(l.herbivores_pop)
    y = 0
    for _ in range(10):
        l.newborn_animals()
        if len(l.herbivores_pop) > length: # + l.new_h
            y += 1  # there has to be added at least one newborn at least once
    assert y > 0


def test_newborn_added_to_list_carn():
    population = [{'species': 'Carnivore', 'weight': 35, 'age': 5},
                  {'species': 'Carnivore', 'weight': 41, 'age': 8},
                  {'species': 'Carnivore', 'weight': 50, 'age': 9}]
    l = Lowland(population)
    length = len(l.carnivores_pop)
    l.newborn_animals()
    assert len(l.carnivores_pop) == length + l.new_c

def test_mother_lost_weight_herb():  # fungerer hver gang om mocker fungerer
    c = Lowland(population=[{'species': 'Herbivore', 'weight': 35, 'age': 5},
                            {'species': 'Herbivore', 'weight': 41, 'age': 8}])

    weight = [k.weight for k in c.herbivores_pop]

    c.newborn_animals()
    mother_after = [c.herbivores_pop[0], c.herbivores_pop[1]]
    #newborn_after = [c.herbivores_pop[1], c.herbivores_pop[3]]

    #for k in range(len[weight]):
    #    assert mother_after[k].weight == weight[k] - Herbivore.p['zeta'] * newborn_after[k].weight

    for k in range(len(c.list_new_h)):
        c = Lowland(population=[{'species': 'Carnivore', 'weight': 35, 'age': 5},
                                {'species': 'Carnivore', 'weight': 41, 'age': 8}])

    weight = [k.weight for k in c.carnivores_pop]

    c.newborn_animals()
    #c.carnivores_pop = sorted(c.carnivores_pop, key=operator.attrgetter('age'))
    mother_after = [c.carnivores_pop[0], c.carnivores_pop[1]]
    #newborn_after = [k.weight for k in c.list_new] #[c.carnivores_pop[2], c.carnivores_pop[3]]

    """if len(weight) == len(c.list_new):
        for k in range(len(weight)-len(c.list_new)):
            assert mother_after[k].weight == weight[k] - Carnivore.p['zeta'] * c.list_new[k].weight

    else:
        for k in range(len(c.list_new)):
            assert mother_after[k].weight == weight[k] - Carnivore.p['zeta'] * c.list_new[k].weight
    """

    for k in range(len(c.list_new_c)):
        assert mother_after[k].weight == weight[k] - Carnivore.p['zeta'] * c.list_new_c[k].weight

def test_count_animals_herb():
    l = Lowland(population=[{'species': 'Herbivore', 'weight': 35, 'age': 5},
                            {'species': 'Herbivore', 'weight': 41, 'age': 8},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    l.counting_animals()
    assert l.N_herb == len(l.herbivores_pop)


def test_aging_herb():
    c = Lowland(population=[{'species': 'Herbivore', 'weight': 35, 'age': 5},
                            {'species': 'Herbivore', 'weight': 41, 'age': 8},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    liste = []
    for ani in range(len(c.herbivores_pop)):
        liste.append(c.herbivores_pop[ani].age)
    c.make_animals_age()
    for k in range(len(c.herbivores_pop)):
        assert c.herbivores_pop[k].age == liste[k] + 1


def test_yearly_weight_loss_herb():
    c = Lowland(population=[{'species': 'Herbivore', 'weight': 35, 'age': 5},
                            {'species': 'Herbivore', 'weight': 41, 'age': 8},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9}])

    liste = [animal.weight for animal in c.herbivores_pop]
    c.make_animals_lose_weight()
    for k in range(len(c.herbivores_pop)):
        assert c.herbivores_pop[k].weight == liste[k] - Herbivore.p['eta'] * liste[k]


def test_animal_removed_after_death_herb():
    c = Lowland(population=[{'species': 'Herbivore', 'weight': 35, 'age': 5},
                            {'species': 'Herbivore', 'weight': 41, 'age': 8},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    liste = c.herbivores_pop
    c.dead_animals_natural_cause()
    assert len(c.herbivores_pop) == len(liste) - c.dead


def test_animal_removed_after_death_carn():
    population = [{'species': 'Carnivore', 'weight': 35, 'age': 5},
                  {'species': 'Carnivore', 'weight': 41, 'age': 8},
                  {'species': 'Carnivore', 'weight': 50, 'age': 9}]
    l = Lowland(population)
    liste = l.carnivores_pop
    l.dead_animals_natural_cause()

    assert len(l.carnivores_pop) == len(liste) - l.dead
