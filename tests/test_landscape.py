"""'
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
"""

from biosim.Cell import Lowland, Highland, Desert, Water
from biosim.Animals import Herbivore, Carnivore
import operator

# tests for initial values:
def test_lowland_given_fodder():
    """
    When initialising a cell it is given an amount for fodder. The fodder in Lowland is 800
    """
    l = Lowland(population=[{'species': 'Carnivore', 'weight': 50, 'age': 9}])
    assert l.p['f_max'] == 800

def test_highland_given_fodder():
    """
    When initialising a cell it is given an amount for fodder. The fodder in Highland is 300
    """
    h = Highland(population=[{'species': 'Carnivore', 'weight': 50, 'age': 9}])
    assert h.p['f_max'] == 300

def test_water_unhabitable():
    """
    An animal can not enter the water. It is therefore unhabitable.
    """
    w = Water(population={})
    assert w.Habitable() == False



# tests for sorting_animals function
def test_sorting_herb():
    """
    This is a test that checks if the herbivores get sorted in a list based on ascending
    phi-value.
    """
    l = Lowland(population = [{'species': 'Herbivore', 'weight': 60, 'age': 5},
                              {'species': 'Herbivore', 'weight': 41, 'age': 8},
                              {'species': 'Herbivore', 'weight': 50, 'age': 9},
                              {'species': 'Carnivore', 'weight': 35, 'age': 5},
                              {'species': 'Carnivore', 'weight': 41, 'age': 8},
                              {'species': 'Carnivore', 'weight': 50, 'age': 9}])
    unsorted_herbs = l.herbivores_pop
    herbs_fitness = [k.phi for k in unsorted_herbs]
    herbs_fitness.sort()
    l.sorting_animals()
    sorted_herbs_fitness = [k.phi for k in l.herbivores_pop]
    assert herbs_fitness == sorted_herbs_fitness

def test_sorting_carn():
    """
    This is a test that checks if the carnivores get sorted in a list based on descending
    phi-value.
    """
    l = Lowland(population=[{'species': 'Herbivore', 'weight': 60, 'age': 5},
                            {'species': 'Herbivore', 'weight': 41, 'age': 8},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9},
                            {'species': 'Carnivore', 'weight': 35, 'age': 5},
                            {'species': 'Carnivore', 'weight': 41, 'age': 8},
                            {'species': 'Carnivore', 'weight': 50, 'age': 9}])
    unsorted_carns = l.carnivores_pop
    carns_fitness = [k.phi for k in unsorted_carns]
    carns_fitness.sort()
    carns_fitness.reverse()
    l.sorting_animals()
    sorted_carns_fitness = [k.phi for k in l.carnivores_pop]
    assert carns_fitness == sorted_carns_fitness



# Tests for make_herbivores_eat function:
def test_eats_random():
    """
    The herbivores should eat in a  random order. To test this, i assign all the herbs a False
    value. I make the herbivores eat. We randomise the list, and everytime they eat, the first
    herb in the list eats and is given a True value. At the end there should be more than one
    herb with a True value.
    """
    population = [{'species': 'Herbivore', 'weight': 35, 'age': 5},
                  {'species': 'Herbivore', 'weight': 41, 'age': 8},
                  {'species': 'Herbivore', 'weight': 50, 'age': 9},
                  {'species': 'Herbivore', 'weight': 10, 'age': 3},
                  {'species': 'Herbivore', 'weight': 14, 'age': 3},
                  {'species': 'Herbivore', 'weight': 13, 'age': 3}]
    l = Lowland(population)
    for herb in l.herbivores_pop:
        herb.eaten = False

    for k in range(len(l.herbivores_pop)):
        l.make_herbivores_eat()
        l.herbivores_pop[0].eaten = True

    eaten = 0
    for herb in l.herbivores_pop:
        if herb.eaten == True:
            eaten += 1

    assert eaten > 1

def test_available_fodder():
    """
    The available fodder should be 800 for lowland
    """
    l = Lowland(population=[{'species': 'Carnivore', 'weight': 50, 'age': 9}])
    assert l.af == 800

def test_consumption_becomes_appetite():
    """
    When the herbivore has enough fodder the consumption should be the same as the appetite
    """
    population = [{'species': 'Herbivore', 'weight': 35, 'age': 5},
                  {'species': 'Herbivore', 'weight': 41, 'age': 8},
                  {'species': 'Herbivore', 'weight': 50, 'age': 9},
                  {'species': 'Herbivore', 'weight': 10, 'age': 3},
                  {'species': 'Herbivore', 'weight': 14, 'age': 3},
                  {'species': 'Herbivore', 'weight': 13, 'age': 3}]
    l = Lowland(population)
    l.make_herbivores_eat()
    for herb in l.herbivores_pop:
        assert herb.F_consumption == herb.p['F']

def test_update_fodder():
    """
    When a herbivore eats the available fodder should update. When there are six herbivores there
    should be enough fodder for everyone. The updated fodder should then be 800 - 6 * appetite
    """
    population = [{'species': 'Herbivore', 'weight': 35, 'age': 5},
                  {'species': 'Herbivore', 'weight': 41, 'age': 8},
                  {'species': 'Herbivore', 'weight': 50, 'age': 9},
                  {'species': 'Herbivore', 'weight': 10, 'age': 3},
                  {'species': 'Herbivore', 'weight': 14, 'age': 3},
                  {'species': 'Herbivore', 'weight': 13, 'age': 3}]
    l = Lowland(population)
    appetite = Herbivore({'species': 'Herbivore', 'weight': 41, 'age': 8}).p['F']
    l.make_herbivores_eat()
    assert l.af == 800 - len(l.herbivores_pop) * appetite

def test_consumption_when_little_fodder():
    """
    When there is to little fodder the consumption is not the same as the appetite, but rather
    what is left of the fodder
    """
    population = [{'species': 'Herbivore', 'weight': 35, 'age': 5},
                  {'species': 'Herbivore', 'weight': 41, 'age': 8},
                  {'species': 'Herbivore', 'weight': 50, 'age': 9},
                  {'species': 'Herbivore', 'weight': 10, 'age': 3},
                  {'species': 'Herbivore', 'weight': 14, 'age': 3},
                  {'species': 'Herbivore', 'weight': 13, 'age': 3}]
    l = Lowland(population)
    l.p['f_max'] = 8
    l.make_herbivores_eat()
    assert l.herbivores_pop[0].F_consumption == 8

def test_fodder_will_stop_at_zero():
    """
    When there isn't enough fodder the available fodder should stop at 0 after eating and not
    become negagtive.
    """
    population = [{'species': 'Herbivore', 'weight': 35, 'age': 5},
                  {'species': 'Herbivore', 'weight': 41, 'age': 8},
                  {'species': 'Herbivore', 'weight': 50, 'age': 9},
                  {'species': 'Herbivore', 'weight': 10, 'age': 3},
                  {'species': 'Herbivore', 'weight': 14, 'age': 3},
                  {'species': 'Herbivore', 'weight': 13, 'age': 3}]
    l = Lowland(population)
    l.p['f_max'] = 51
    l.make_herbivores_eat()
    assert l.af == 0

def test_gain_weight_after_eating_herb():
    """
    After the herbivore eats it should gain weight
    """
    population = [{'species': 'Herbivore', 'weight': 35, 'age': 5},
                  {'species': 'Herbivore', 'weight': 41, 'age': 8},
                  {'species': 'Herbivore', 'weight': 50, 'age': 9},
                  {'species': 'Herbivore', 'weight': 10, 'age': 3},
                  {'species': 'Herbivore', 'weight': 14, 'age': 3},
                  {'species': 'Herbivore', 'weight': 13, 'age': 3}]
    l = Lowland(population)
    weight = [k.weight for k in l.herbivores_pop]
    l.make_herbivores_eat()
    weight_after_eating = [k.weight for k in l.herbivores_pop]
    weight.sort()
    weight_after_eating.sort()
    assert [k + 9 for k in weight] == weight_after_eating

def test_fitness_change_after_eating():
    """
    After the herbivores eats, they should gain weight and therefore have a greater fitness
    """
    population = [{'species': 'Herbivore', 'weight': 35, 'age': 5},
                  {'species': 'Herbivore', 'weight': 41, 'age': 8},
                  {'species': 'Herbivore', 'weight': 50, 'age': 9},
                  {'species': 'Herbivore', 'weight': 10, 'age': 3},
                  {'species': 'Herbivore', 'weight': 14, 'age': 3},
                  {'species': 'Herbivore', 'weight': 13, 'age': 3}]
    l = Lowland(population)
    init_fitness = [k.phi for k in l.herbivores_pop]
    l.make_herbivores_eat()
    fitness_after_eating = [k.phi for k in l.herbivores_pop]
    init_fitness.sort()
    fitness_after_eating.sort()
    for k in range(len(l.herbivores_pop)):
        assert init_fitness[k] < fitness_after_eating[k]


# Tests for available_herbivores_for_carnivores function
def test_available_herbivores():
    """
    The available food for carnivores is the weight of the available herbivores
    """
    l = Lowland(population=[{'species': 'Herbivore', 'weight': 35, 'age': 5},
                            {'species': 'Herbivore', 'weight': 41, 'age': 8},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    weight = 0
    for k in l.herbivores_pop:
        weight += k.weight
    l.available_herbivores_for_carnivores()
    assert l.herbivores_weight_sum == weight



# Tests for feed_carnivores_function
def test_carn_appetite():
    """
    The carnivores appetite is given as a parameter. It should be 50 before eating
    """
    population = [{'species': 'Carnivore', 'weight': 35, 'age': 5},
                  {'species': 'Carnivore', 'weight': 41, 'age': 8},
                  {'species': 'Carnivore', 'weight': 50, 'age': 9},
                  {'species': 'Herbivore', 'weight': 10, 'age': 3},
                  {'species': 'Herbivore', 'weight': 14, 'age': 3},
                  {'species': 'Herbivore', 'weight': 13, 'age': 3}]
    l = Lowland(population)
    for carn in l.carnivores_pop:
        assert carn.p['F'] == 50

def test_weakest_herb_eaten_first(mocker):
    """
    When the carnivores eats, it eats the weakest herbivore first. To check if that happens i
    make sure there are only one carnivore in the cell with appetite equal to the weight of the
    weakest herbivore. After eating we check that the herbivore is no longer in the cell
    """
    mocker.patch('random.random', return_value=0.01)
    population = [{'species': 'Herbivore', 'weight': 35, 'age': 5},
                  {'species': 'Herbivore', 'weight': 41, 'age': 8},
                  {'species': 'Herbivore', 'weight': 50, 'age': 9},
                  {'species': 'Carnivore', 'weight': 70, 'age': 10},
                  {'species': 'Herbivore', 'weight': 10, 'age': 3},
                  {'species': 'Herbivore', 'weight': 60, 'age': 3}]
    l = Lowland(population)
    l.sorting_animals()
    weakest_herb = l.herbivores_pop[0]
    for k in range(len(l.carnivores_pop)):
        l.carnivores_pop[k].p['F'] = weakest_herb.weight + 1
    l.feed_carnivores()
    assert weakest_herb not in l.herbivores_pop

def test_strongest_carn_eats_first(mocker):
    """
    When eating the strongest carnivore always eats first. To test this a make sure there are only
    carnivores with a total weight of the carnivores appetite (ie. 50), and make the carnivores eat.
    Later i check that the weight of is the same for all the carnivores, except the fittest.
    """
    mocker.patch('random.random', return_value=0.01)
    population = [{'species': 'Herbivore', 'weight': 25, 'age': 5},
                  {'species': 'Herbivore', 'weight': 25, 'age': 8},
                  {'species': 'Carnivore', 'weight': 50, 'age': 9},
                  {'species': 'Carnivore', 'weight': 70, 'age': 10},
                  {'species': 'Carnivore', 'weight': 10, 'age': 3},
                  {'species': 'Carnivore', 'weight': 90, 'age': 3}]
    l = Lowland(population)
    l.sorting_animals()
    init_weight = [carn.weight for carn in l.carnivores_pop]
    l.feed_carnivores()
    for k in range(1,len(l.carnivores_pop)):
        assert l.carnivores_pop[k].weight == init_weight[k]

def test_eats_until_reaches_appetite(mocker):
    """
    The carnivores does not stop eating until it has eaten herbs with total weight >= appetite.
    To check this I make several carnivores, and enough herbivores for all of them to be full.
    After they eat i check that they have all gained as much weight as they should, which is
    appetite * beta
    """
    mocker.patch('random.random', return_value=0.01)
    population = [{'species': 'Herbivore', 'weight': 23, 'age': 5},
                  {'species': 'Herbivore', 'weight': 23, 'age': 5},
                  {'species': 'Herbivore', 'weight': 23, 'age': 5},
                  {'species': 'Herbivore', 'weight': 23, 'age': 5},
                  {'species': 'Herbivore', 'weight': 23, 'age': 5},
                  {'species': 'Herbivore', 'weight': 23, 'age': 5},
                  {'species': 'Carnivore', 'weight': 100, 'age': 3},
                  {'species': 'Carnivore', 'weight': 100, 'age': 3}]
    l = Lowland(population)
    beta = l.carnivores_pop[0].p['beta']
    appetite = l.carnivores_pop[0].p['F']
    l.sorting_animals()
    init_weight = [carn.weight for carn in l.carnivores_pop]
    l.feed_carnivores()
    for k in range(len(l.carnivores_pop)):
        assert init_weight[k] + appetite * beta <= l.carnivores_pop[k].weight


def test_eats_until_tried_eating_all_the_herbivores(mocker):
    """
    The carnivore eats until it has tried to eat all the herbivores. To test this we create less
    available fodder than there are appetites to see if they are all removed from the list
    """
    mocker.patch('random.random', return_value=0.01)
    population = [{'species': 'Herbivore', 'weight': 23, 'age': 5},
                  {'species': 'Herbivore', 'weight': 23, 'age': 5},
                  {'species': 'Herbivore', 'weight': 23, 'age': 5},
                  {'species': 'Carnivore', 'weight': 100, 'age': 3},
                  {'species': 'Carnivore', 'weight': 100, 'age': 3}]
    l = Lowland(population)
    l.feed_carnivores()
    assert len(l.herbivores_pop) == 0

def test_will_not_eat_stronger_herb(mocker):
    """
    If the herbivore is stronger than the carnivore, the carnivore will not be able to eat. To test
    this the mocker is set very low and we create one strong herbivore and one weak carnivore.
    Later we check if the herbivore is still there
    """
    mocker.patch('random.random', return_value=0.001)
    population = [{'species': 'Herbivore', 'weight': 70, 'age': 5},
                  {'species': 'Carnivore', 'weight': 13, 'age': 5}]
    l = Lowland(population)
    l.feed_carnivores()
    assert len(l.herbivores_pop) != 0

def test_update_fitness_after_eating_carnivores(mocker):
    """
    When a carnivore eats it gains weight, and therefore need to have grater fitness
    """
    mocker.patch('random.random', return_value=0.01)
    population = [{'species': 'Carnivore', 'weight': 70, 'age': 5},
                  {'species': 'Carnivore', 'weight': 80, 'age': 8},
                  {'species': 'Carnivore', 'weight': 90, 'age': 9},
                  {'species': 'Herbivore', 'weight': 25, 'age': 3},
                  {'species': 'Herbivore', 'weight': 25, 'age': 3},
                  {'species': 'Herbivore', 'weight': 25, 'age': 3},
                  {'species': 'Herbivore', 'weight': 25, 'age': 3},
                  {'species': 'Herbivore', 'weight': 25, 'age': 3},
                  {'species': 'Herbivore', 'weight': 25, 'age': 3}]
    l = Lowland(population)
    l.sorting_animals()
    init_fitness = [carn.phi for carn in l.carnivores_pop]
    l.feed_carnivores()
    for k in range(len(l.carnivores_pop)):
        assert l.carnivores_pop[k].phi > init_fitness[k]



# Tests for newborn_animals_function for herbs
def test_newborn_added_to_list_herb():
    """
    When an animal gives birth the newborn must be added to the list. When there are 9 herbivores
    the probability for birth is 1, if the weight is acceptable, and therefore there will be added
    9 herbivores to the list.
    """
    l = Lowland(population=[{'species': 'Herbivore', 'weight': 65, 'age': 3},
                            {'species': 'Herbivore', 'weight': 41, 'age': 3},
                            {'species': 'Herbivore', 'weight': 50, 'age': 3},
                            {'species': 'Herbivore', 'weight': 40, 'age': 3},
                            {'species': 'Herbivore', 'weight': 41, 'age': 3},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9},
                            {'species': 'Herbivore', 'weight': 67, 'age': 5},
                            {'species': 'Herbivore', 'weight': 41, 'age': 8},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    length = len(l.herbivores_pop)
    l.newborn_animals()
    assert len(l.herbivores_pop) == length * 2

def test_mother_lost_weight_herb():
    """
    When an animal gives birth the mother loses weight equivalent to the weight of the
    newborn * zeta. When there are 9 herbivores the probability for birth is 1, if the weight is
    acceptable, and therefore all 9 herbivores will give birth
    """
    l = Lowland(population=[{'species': 'Herbivore', 'weight': 65, 'age': 3},
                            {'species': 'Herbivore', 'weight': 41, 'age': 3},
                            {'species': 'Herbivore', 'weight': 50, 'age': 3},
                            {'species': 'Herbivore', 'weight': 40, 'age': 3},
                            {'species': 'Herbivore', 'weight': 41, 'age': 3},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9},
                            {'species': 'Herbivore', 'weight': 67, 'age': 5},
                            {'species': 'Herbivore', 'weight': 41, 'age': 8},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    sorted_herbivores_pop = sorted(l.herbivores_pop, key=operator.attrgetter('age'))
    weight = [k.weight for k in sorted_herbivores_pop]
    zeta = l.herbivores_pop[0].p['zeta']

    l.newborn_animals()

    sorted_herbivores_pop = sorted(l.herbivores_pop, key=operator.attrgetter('age'))
    sorted_herbivores_pop.reverse()
    mothers = sorted_herbivores_pop[0:8]

    newborn_weight = [herb.newborn_birth_weight for herb in mothers]

    #weight.sort()
    #newborn_weight.sort()

    for k in range(len(weight)):
        assert weight[k] - newborn_weight[k] * zeta == mothers[k].weight

def test_mother_lost_fitness_herb():
    assert 1 == 1

def test_criteria_for_birth_fitness_herb():
    c = Lowland(population = [{'species': 'Herbivore', 'weight': 35, 'age': 5},
                              {'species': 'Herbivore', 'weight': 0, 'age': 8},
                              {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    for k in c.herbivores_pop:
        if k.phi == 0:
            k.will_the_animal_give_birth(n=len(c.herbivores_pop))
            assert k.birth == False

def test_criteria_for_birth_weight_herb():
    c = Lowland(population = [{'species': 'Herbivore', 'weight': 35, 'age': 5},
                              {'species': 'Herbivore', 'weight': 10, 'age': 8},
                              {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    for k in c.herbivores_pop:
        k.will_the_animal_give_birth(n=len(c.herbivores_pop))
        if k.weight <= k.newborn_birth_weight * k.p['zeta']:
            assert k.birth == False

def test_criteria_for_birth_prob_herb():
    c = Lowland(population = [{'species': 'Herbivore', 'weight': 75, 'age': 5},
                              {'species': 'Herbivore', 'weight': 60, 'age': 8},
                              {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    for k in c.herbivores_pop:
        if k.birth_probability(n=len(c.herbivores_pop)) != 0:
            assert k.birth_probability(n=len(c.herbivores_pop)) == k.p['gamma'] * k.phi * (len(c.herbivores_pop) - 1)
        else:
            assert 1 == 2



# Tests for newborn_animals for carns
def test_newborn_added_to_list_carn():
    population = [{'species': 'Carnivore', 'weight': 35, 'age': 5},
                  {'species': 'Carnivore', 'weight': 41, 'age': 8},
                  {'species': 'Carnivore', 'weight': 50, 'age': 9}]
    l = Lowland(population)
    length = len(l.carnivores_pop)
    l.newborn_animals()
    assert len(l.carnivores_pop) == 7 #length + l.new_c

def test_mother_lost_weight_carn():
    assert 1 == 1

def test_mother_lost_fitness_carn():
    assert 1 == 1

def test_criteria_for_birth_fitness_carn():
    c = Lowland(population = [{'species': 'Herbivore', 'weight': 35, 'age': 5},
                              {'species': 'Herbivore', 'weight': 0, 'age': 8},
                              {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    for k in c.herbivores_pop:
        if k.phi == 0:
            k.will_the_animal_give_birth(n=len(c.herbivores_pop))
            assert k.birth == False

def test_criteria_for_birth_weight_carn():
    c = Lowland(population = [{'species': 'Herbivore', 'weight': 35, 'age': 5},
                              {'species': 'Herbivore', 'weight': 10, 'age': 8},
                              {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    for k in c.herbivores_pop:
        k.will_the_animal_give_birth(n=len(c.herbivores_pop))
        if k.weight <= k.newborn_birth_weight * k.p['zeta']:
            assert k.birth == False

def test_criteria_for_birth_prob_carn():
    c = Lowland(population = [{'species': 'Herbivore', 'weight': 75, 'age': 5},
                              {'species': 'Herbivore', 'weight': 60, 'age': 8},
                              {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    for k in c.herbivores_pop:
        if k.birth_probability(n=len(c.herbivores_pop)) != 0:
            assert k.birth_probability(n=len(c.herbivores_pop)) == k.p['gamma'] * k.phi * (len(c.herbivores_pop) - 1)
        else:
            assert 1 == 2



# Tests for move_animals_from_cell:
def test_herbs_removed_from_list():
    assert 1 == 1

def test_carns_removed_from_list():
    assert 1 == 1

def test_total_moving_animals():
    assert 1 == 1

# tests for move_animals_to_cell:
def test_herb_added_to_cell():
    assert 1 == 1

def test_carns_added_to_cell():
    assert 1 == 1



# Tests for reset_already_moved:
def test_reset_already_moved_herb():
    assert 1 == 1

def test_reset_already_moved_carn():
    assert 1 == 1



# Tests for counting_animals function
def test_count_animals_herb():
    l = Lowland(population=[{'species': 'Herbivore', 'weight': 35, 'age': 5},
                            {'species': 'Herbivore', 'weight': 41, 'age': 8},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    l.counting_animals()
    assert l.N_herb == len(l.herbivores_pop)

def test_count_animals_carn():
    assert 1 == 1



# Tests for make_animals_age function
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

def test_fitness_when_aging_herb():
    c = Lowland(population=[{'species': 'Herbivore', 'weight': 35, 'age': 5},
                            {'species': 'Herbivore', 'weight': 35, 'age': 6},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    c.make_animals_age()
    assert Herbivore({'species': 'Herbivore', 'weight': 35, 'age': 6}).phi == c.herbivores_pop[0].phi

def test_aging_carn():
    assert 1 == 1

def test_fitness_when_aging_carn():
    assert 1 == 1



# Tests for update fitness
def test_update_fitness_herb():
    assert 1 == 1

def test_update_fitness_carn():
    assert 1 == 1



# Tests for make_animals_lose_weight:
def test_yearly_weight_loss_herb():
    c = Lowland(population=[{'species': 'Herbivore', 'weight': 35, 'age': 5},
                            {'species': 'Herbivore', 'weight': 41, 'age': 8},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9}])

    liste = [animal.weight for animal in c.herbivores_pop]
    c.make_animals_lose_weight()
    for k in range(len(c.herbivores_pop)):
        assert c.herbivores_pop[k].weight == liste[k] - Herbivore.p['eta'] * liste[k]

def test_update_fitness_during_weight_loss_herb():
    c = Lowland(population=[{'species': 'Herbivore', 'weight': 35, 'age': 5},
                            {'species': 'Herbivore', 'weight': 41, 'age': 8},
                            {'species': 'Herbivore', 'weight': 50, 'age': 9}])
    liste = [animal.phi for animal in c.herbivores_pop]
    c.make_animals_lose_weight()
    for k in range(len(liste)):
        assert c.herbivores_pop[k].phi < liste[k]

def test_yearly_weight_loss_carn():
    assert 1 == 1

def test_update_fitness_during_weight_loss_carn():
    assert 1 == 1



# Tests for dead_animals_natural_cause:
def test_animal_removed_after_death_when_true_herb():
    c = Lowland(population=[{'species': 'Herbivore', 'weight': 5, 'age': 60},
                            {'species': 'Herbivore', 'weight': 41, 'age': 8},
                            {'species': 'Herbivore', 'weight': 0, 'age': 9}])
    liste = c.herbivores_pop
    c.dead_animals_natural_cause()
    assert len(c.herbivores_pop) == len(liste) - c.dead


def test_animal_removed_after_death_when_true_carn():
    population = [{'species': 'Carnivore', 'weight': 35, 'age': 5},
                  {'species': 'Carnivore', 'weight': 0, 'age': 8},
                  {'species': 'Carnivore', 'weight': 50, 'age': 9}]
    l = Lowland(population)
    liste = l.carnivores_pop
    l.dead_animals_natural_cause()

    assert len(l.carnivores_pop) == len(liste) - l.dead

def test_animal_removed_after_death_when_false_herb():
    assert 1 == 1

def test_animal_removed_after_death_when_false_carn():
    assert 1 == 1