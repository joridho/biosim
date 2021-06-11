"""'
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
"""

from biosim.Cell import Lowland
from biosim.Animals import Herbivore, Carnivore
import operator


def test_simple_sorting_herb():
    """
    This is a test that checks if the herbivores get sorted in a list based on ascending
    phi-value.
    """
    population = [{'species': 'Herbivore', 'weight': 60, 'age': 5},
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
    assert liste2 == liste3

def test_simple_sorting_herb():
    """
    This is a test that checks if the carnivores get sorted in a list based on descending
    phi-value.
    """
    population = [{'species': 'Herbivore', 'weight': 60, 'age': 5},
                  {'species': 'Herbivore', 'weight': 41, 'age': 8},
                  {'species': 'Herbivore', 'weight': 50, 'age': 9},
                  {'species': 'Carnivore', 'weight': 35, 'age': 5},
                  {'species': 'Carnivore', 'weight': 41, 'age': 8},
                  {'species': 'Carnivore', 'weight': 50, 'age': 9}]
    c = Lowland(population)

    liste1 = c.carnivores_pop
    liste2 = [liste1[0].phi, liste1[1].phi, liste1[2].phi]
    liste2.sort()
    c.sorting_animals()
    liste3 = [c.carnivores_pop[0].phi, c.carnivores_pop[1].phi,
              c.carnivores_pop[2].phi]
    assert liste2 != liste3


def test_parameters_lowland():
    l = Lowland(population=[{'species': 'Carnivore', 'weight': 50, 'age': 9}])
    assert l.p['f_max'] == 800


def test_sorting_carnivores():
    l = Lowland(population=[{'species': 'Carnivore', 'weight': 35, 'age': 5},
                            {'species': 'Carnivore', 'weight': 41, 'age': 8},
                            {'species': 'Carnivore', 'weight': 50, 'age': 9}])
    liste1 = l.carnivores_pop
    pop1 = [k.phi for k in liste1]
    pop1.sort()
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

def test_fodder_will_stop_at_zero():
    l = Lowland(population=[{'species': 'Herbivore', 'weight': 35, 'age': 5},
                            {'species': 'Herbivore', 'weight': 41, 'age': 8},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    l.make_herbivores_eat()
    assert l.af == 0  # to test this I changed self.af to 25 in cell class. Not optimal, i know.


def test_gain_weight_after_eating_herb():  # får den kun til å fungere på ett dyr
    l = Lowland(population=[{'age': 5, 'species': 'Herbivore', 'weight': 20},
                            {'species': 'Herbivore', 'weight': 41, 'age': 8},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    weight = [k.weight for k in l.herbivores_pop]
    l.make_herbivores_eat()
    weight2 = [k.weight for k in l.herbivores_pop]
    weight.sort()
    weight2.sort()
    assert [k + 9 for k in weight] == weight2
    # if i change the available fodder to 25, the last herb will not gain 9 kg, as the other two

def test_fitness_change_after_eating():
    l = Lowland(population=[{'age': 5, 'species': 'Herbivore', 'weight': 20},
                            {'species': 'Herbivore', 'weight': 41, 'age': 8},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    fitness1 = [k.phi for k in l.herbivores_pop]
    l.make_herbivores_eat()
    fitness2 = [k.phi for k in l.herbivores_pop]
    fitness1.sort()
    fitness2.sort()
    for k in range(len(fitness1)):
        assert fitness1[k] < fitness2[k]

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

def test_eats_random():
    population = [{'species': 'Herbivore', 'weight': 35, 'age': 5},
                  {'species': 'Herbivore', 'weight': 41, 'age': 8},
                  {'species': 'Herbivore', 'weight': 50, 'age': 9},
                  {'species': 'Herbivore', 'weight': 10, 'age': 3},
                  {'species': 'Herbivore', 'weight': 14, 'age': 3},
                  {'species': 'Herbivore', 'weight': 13, 'age': 3}]
    l = Lowland(population)
    liste = l.herbivores_pop
    l.make_herbivores_eat()
    for k in range(len(l.herbivores_pop)):
        assert l.herbivores_pop[k].weight > liste[k].weight




def test_carnivore_weight_gain():  # de går opp i vekt, men ikke hver gang, og det er forsåvidt riktig
    population = [{'species': 'Carnivore', 'weight': 35, 'age': 5},
                  {'species': 'Carnivore', 'weight': 41, 'age': 8},
                  {'species': 'Carnivore', 'weight': 50, 'age': 9},
                  {'species': 'Herbivore', 'weight': 10, 'age': 3},
                  {'species': 'Herbivore', 'weight': 14, 'age': 3},
                  {'species': 'Herbivore', 'weight': 13, 'age': 3}]
    l = Lowland(population)
    #l.sorting_animals()
    liste = l.carnivores_pop
    l.feed_carnivores()
    #l.sorting_animals()
    for k in range(len(l.carnivores_pop)):
        assert l.carnivores_pop[k].weight > liste[k].weight

def test_herbivores_removed_after_feed_carnivores():  # fungerer ikke hver gang, men det er fordi de ikke spiser hver gang
    population = [{'species': 'Carnivore', 'weight': 35, 'age': 5},
                  {'species': 'Carnivore', 'weight': 41, 'age': 8},
                  {'species': 'Carnivore', 'weight': 50, 'age': 9},
                  {'species': 'Herbivore', 'weight': 10, 'age': 3},
                  {'species': 'Herbivore', 'weight': 14, 'age': 3},
                  {'species': 'Herbivore', 'weight': 13, 'age': 3}]
    l = Lowland(population)
    l.sorting_animals()
    liste2 = l.herbivores_pop
    l.make_herbivores_eat()
    l.feed_carnivores()
    l.sorting_animals()
    if l.herbivores_pop[0].weight > liste2[0].weight:
        assert len(liste2) > len(l.herbivores_pop)
    else:
        assert 1 == 2  # for å vite om de blir fjerna fra lista når vekta til carn går opp

def test_update_fitness_carnivores():  # fungerer ikke hver gang, men det er fordi den ikke spiser hver gang
    population = [{'species': 'Carnivore', 'weight': 35, 'age': 5},
                  {'species': 'Carnivore', 'weight': 41, 'age': 8},
                  {'species': 'Carnivore', 'weight': 50, 'age': 9},
                  {'species': 'Herbivore', 'weight': 10, 'age': 3},
                  {'species': 'Herbivore', 'weight': 14, 'age': 3},
                  {'species': 'Herbivore', 'weight': 13, 'age': 3}]
    l = Lowland(population)
    l.sorting_animals()
    liste2 = l.herbivores_pop
    l.make_herbivores_eat()
    l.feed_carnivores()
    l.sorting_animals()
    for k in range(len(l.herbivores_pop)):
        assert l.herbivores_pop[k].phi > liste2[k].phi

def test_available_fodder():
    l = Lowland(population=[{'species': 'Herbivore', 'weight': 35, 'age': 5},
                            {'species': 'Herbivore', 'weight': 41, 'age': 8},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    food = l.af
    l.make_herbivores_eat()
    assert l.af == food - 3 * 10


def test_newborn_added_to_list_herb():
    l = Lowland(population=[{'species': 'Herbivore', 'weight': 15, 'age': 3},
                            {'species': 'Herbivore', 'weight': 41, 'age': 3},
                            {'species': 'Herbivore', 'weight': 50, 'age': 3},
                            {'species': 'Herbivore', 'weight': 0, 'age': 3},
                            {'species': 'Herbivore', 'weight': 41, 'age': 3},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9},
                            {'species': 'Herbivore', 'weight': 67, 'age': 5},
                            {'species': 'Herbivore', 'weight': 21, 'age': 8},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    length = len(l.herbivores_pop)
    l.newborn_animals()
    assert len(l.herbivores_pop) > length


def test_newborn_added_to_list_carn():
    population = [{'species': 'Carnivore', 'weight': 35, 'age': 5},
                  {'species': 'Carnivore', 'weight': 41, 'age': 8},
                  {'species': 'Carnivore', 'weight': 50, 'age': 9}]
    l = Lowland(population)
    length = len(l.carnivores_pop)
    l.newborn_animals()
    assert len(l.carnivores_pop) == 7 #length + l.new_c



def test_mother_lost_weight_herb():  # fungerer om mocker fungerer
    c = Lowland(population = [{'species': 'Herbivore', 'weight': 35, 'age': 5},
                              {'species': 'Herbivore', 'weight': 41, 'age': 8},
                              {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    weight = [k.weight for k in c.herbivores_pop]
    c.newborn_animals()
    for k in range(len(weight)):
        assert weight[k] > c.herbivores_pop[k].weight

def test_criteria_for_birth1():
    c = Lowland(population = [{'species': 'Herbivore', 'weight': 35, 'age': 5},
                              {'species': 'Herbivore', 'weight': 0, 'age': 8},
                              {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    for k in c.herbivores_pop:
        if k.phi == 0:
            k.will_the_animal_give_birth(n=len(c.herbivores_pop))
            assert k.birth == False

def test_criteria_for_birth2():
    c = Lowland(population = [{'species': 'Herbivore', 'weight': 35, 'age': 5},
                              {'species': 'Herbivore', 'weight': 10, 'age': 8},
                              {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    for k in c.herbivores_pop:
        k.will_the_animal_give_birth(n=len(c.herbivores_pop))
        if k.weight <= k.newborn_birth_weight * k.p['zeta']:
            assert k.birth == False

def test_criteria_for_birth2():
    c = Lowland(population = [{'species': 'Herbivore', 'weight': 75, 'age': 5},
                              {'species': 'Herbivore', 'weight': 60, 'age': 8},
                              {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    for k in c.herbivores_pop:
        if k.birth_probability(n=len(c.herbivores_pop)) != 0:
            assert k.birth_probability(n=len(c.herbivores_pop)) == k.p['gamma'] * k.phi * (len(c.herbivores_pop) - 1)
        else:
            assert 1 == 2

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

def test_fitness_when_aging():
    c = Lowland(population=[{'species': 'Herbivore', 'weight': 35, 'age': 5},
                            {'species': 'Herbivore', 'weight': 35, 'age': 6},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    c.make_animals_age()
    assert Herbivore({'species': 'Herbivore', 'weight': 35, 'age': 6}).phi == c.herbivores_pop[0].phi


def test_yearly_weight_loss_herb():
    c = Lowland(population=[{'species': 'Herbivore', 'weight': 35, 'age': 5},
                            {'species': 'Herbivore', 'weight': 41, 'age': 8},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9}])

    liste = [animal.weight for animal in c.herbivores_pop]
    c.make_animals_lose_weight()
    for k in range(len(c.herbivores_pop)):
        assert c.herbivores_pop[k].weight == liste[k] - Herbivore.p['eta'] * liste[k]

def test_update_fitness_during_weight_loss():
    c = Lowland(population=[{'species': 'Herbivore', 'weight': 35, 'age': 5},
                            {'species': 'Herbivore', 'weight': 41, 'age': 8},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    liste = [animal.phi for animal in c.herbivores_pop]
    c.make_animals_lose_weight()
    for k in range(len(liste)):
        assert c.herbivores_pop[k].phi < liste[k]


def test_animal_removed_after_death_herb():
    c = Lowland(population=[{'species': 'Herbivore', 'weight': 5, 'age': 60},
                            {'species': 'Herbivore', 'weight': 41, 'age': 8},
                            {'species': 'Herbivore', 'weight': 0, 'age': 9}])
    liste = c.herbivores_pop
    c.dead_animals_natural_cause()
    assert len(c.herbivores_pop) == len(liste) - c.dead


def test_animal_removed_after_death_carn():
    population = [{'species': 'Carnivore', 'weight': 35, 'age': 5},
                  {'species': 'Carnivore', 'weight': 0, 'age': 8},
                  {'species': 'Carnivore', 'weight': 50, 'age': 9}]
    l = Lowland(population)
    liste = l.carnivores_pop
    l.dead_animals_natural_cause()

    assert len(l.carnivores_pop) == len(liste) - l.dead
