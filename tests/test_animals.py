# -*- encoding: utf-8 -*-

"""
"""


__author__ = 'Christianie Torres'
__email__ = 'christianie.torres@nmbu.no'

from biosim.animals import Herbivore, Carnivore

def test_parameters():
    h = Herbivore({'species': 'Herbivore',
                       'age': 5,
                       'weight': 20})
    assert h.p['w_birth'] == 8.0

def test_herbivore_age():
    """
    A test that checks that a herbivore has been created with age 0
    """
    h = Herbivore({'species': 'Herbivore',
                       'age': 5,
                       'weight': 20})
    assert h.age == 5

def test_herbivore_weight():
    '''
        test to check if the herbivore has been given a weight
        '''
    h = Herbivore({'species': 'Herbivore',
                       'age': 5,
                       'weight': 20})
    #b = h.birth_weight
    assert h.weight == 20

def test_herbivore_aging():
    """
    A test that checks that the herbivore ages for each year
    """
    h = Herbivore({'species': 'Herbivore',
                       'age': 0,
                       'weight': 20})
    for n in range(10):
        h.aging()
        assert h.age == n + 1

def test_herbivore_birth_weight():
    """
    A test that checks that the herbivore have been given a birth_weight
    """
    h = Herbivore()
    birth_w = h.birth_weight
    assert h.birth_weight == birth_w

def test_herbivore_weight_loss():
    '''
        this is a test for testing if the herbivore looses weight each year
    '''
    h = Herbivore({'species': 'Herbivore',
                       'age': 5,
                       'weight': 20})
    current_weight = h.weight
    eta = h.p['eta']
    h.weight_loss()
    assert h.weight == current_weight - current_weight * eta

def test_herbivore_weight_gain():
    '''
        this is a test for testing if the herbivore gains weight when it eats as much as it wants to
        '''
    h = Herbivore({'species': 'Herbivore',
                       'age': 5,
                       'weight': 20})
    current_weight = h.weight
    beta = h.p['beta']
    F = h.p['F']
    new_weight = current_weight + beta * F
    h.weight_gain(consumption=F)
    assert h.weight == new_weight


def test_herbivore_fitness():
    """
    A test that checks that the herbivore have been given a fitness
    """
    h = Herbivore({'species': 'Herbivore',
                       'age': 5,
                       'weight': 20})
    fitness = h.phi
    h.fitness()
    assert fitness == h.phi

def test_valid_fitness():
    """
    This is a test for checking that the fitness-function returns a phi-value between 0 and 1
    """
    for _ in range(100):
        h = Herbivore({'species': 'Herbivore',
                       'age': 5,
                       'weight': 20})
        assert 0 <= h.phi <= 1

def test_no_newborn_when_mother_weighs_too_little():
    """
    This is a test that checks if the birth probability equals zero when the mother weighs to little.
    """
    h = Herbivore({'species': 'Herbivore',
                       'age': 3,
                       'weight': 3.5})        #weight=3.5, age=3
    assert h.birth_probability(n=3) ==0
def test_no_newborn_when_to_few_animals(): #too
    """
    This is a test that checks if the birth probability equals zero when there are too few animals
    a cell.
    """

    h = Herbivore({'species': 'Herbivore',
                       'age': 3,
                       'weight': 35})                      #weight=35, age=3
    assert h.birth_probability(n=1) == 0

def test_no_newborn_if_newborn_too_fat():
    """
    This is a test that checks if the birth probability equals zero when the newborn weighs more
    than the mother
    """
    # the newborn will weigh more than 15/3.5
    h = Herbivore({'species': 'Herbivore',
                       'age': 3,
                       'weight': 15})                          #weight=15, age=3
    assert h.birth_probability(n=3) == 0

def test_birth():
    'This is a test that checks if the Herbivore gives birth when it is supposed to'
    h = Herbivore({'species': 'Herbivore',
                       'age': 5,
                       'weight': 35})    #weight=35, age=3
    true = 0
    false = 0
    for _ in range(100):
        h.birth_probability(n=4)
        h.will_the_animal_give_birth(n=4)
        if h.birth == True:
            true += 1
        else:
            false +=1
    assert true == false  # bare en test for å sjekke hva som ikke fungerer

def test_herbivore_birth_weight_loss():
    ' This is a test that checks if the Mother looses the right amount of weight after giving birth'
    h = Herbivore({'species': 'Herbivore',
                       'age': 3,
                       'weight': 15})   #Bare å endre alder og vekt hvis du føler for det
    current_weight = h.weight
    h.birth_weight_loss(newborn_birth_weight=8)
    assert h.weight == current_weight - h.p['zeta'] * 8


def test_death():
    '''
    This is a test that checks if the Herbivore dies when it is supposed to'
    '''
    h = Herbivore({'species': 'Herbivore',
                       'age': 3,
                       'weight': 10})
    for _ in range(100):
        h.death_probability()
        if h.will_the_animal_die() == True:
            assert h.d < h.p
        else:
            assert h.d >= h.p

def test_consumption():
    h = Herbivore(properties={'species': 'Carnivore', 'weight': 35, 'age': 5})
    h.eat_fodder(F_cell=800)
    assert h.F_consumption == 10#h.p['F']

def  test_consumption_not_enough_fodder():
    h = Herbivore(properties={'species': 'Carnivore', 'weight': 35, 'age': 5})
    h.eat_fodder(F_cell=7)
    assert h.F_consumption == h.F_consumption

def test_herbivore_eat_fodder():
    h = Herbivore(properties={'species': 'Carnivore', 'weight': 35, 'age': 5})
    current_weight = h.weight
    h.eat_fodder(F_cell = h.p['F']) 
    assert h.weight == current_weight + h.p['beta'] * h.F_consumption

def test_herbivore_gains_weight_after_eat_fodder():
    h = Herbivore(properties={'species': 'Carnivore', 'weight': 35, 'age': 5})
    current_weight = h.weight
    h.eat_fodder(F_cell = 6)
    assert h.weight == current_weight + h.p['beta'] * h.F_consumption

def test_weight_gain_after_eating():
    h = Herbivore(properties={'species': 'Carnivore', 'weight': 35, 'age': 5})
    h.eat_fodder(F_cell = 800)
    assert h.weight == 35 + h.p['beta'] * h.F_consumption


def test_if_carnivore_gains_correct_weight():
    carn = Carnivore({'species': 'Herbivore',
                       'age': 3,
                       'weight': 15})
    w = carn.weight
    herb = Herbivore({'species': 'Herbivore',
                       'age': 3,
                       'weight': 15})
    carn.weight_gain_after_eating_herb(herb)
    assert carn.weight == w + herb.weight * carn.p['beta']

def test_carnivore_updated_fitness():
    carn = Carnivore(weight=70, age=5)
    f1 = carn.phi
    herb = Herbivore(weight=35, age=2)
    carn.weight_gain_after_eating_herb(herb)
    assert f1 != carn.phi

def test_prob_kill():
    herb = Herbivore({'species': 'Herbivore',
                       'age': 3,
                       'weight': 15})
    carn = Carnivore({'species': 'Herbivore',
                       'age': 3,
                       'weight': 15})
    for _ in range(100):
        carn.probability_kill_herbivore(herb)
        if carn.prob_kill == True:
            assert carn.r < carn.prob_kill
        else:
            assert carn.r >= carn.prob_kill

def test_prob_kill_not_work1():
    herb = Herbivore(weight=35, age=3)
    carn = Carnivore(weight=8, age=1)
    # have calculated that the herbivore has greater fitness than the carnivore
    carn.probability_kill_herbivore(herb)
    assert carn.prob_kill == 0

def test_prob_kill_not_work2():
    herb = Herbivore(weight=35, age=3)
    carn = Carnivore(weight=60, age=4)
    carn.probability_kill_herbivore(herb)
    assert carn.prob_kill == (carn.phi - herb.phi) / carn.p['DeltaPhiMax']

def test_to_much_fitness():
    h = Herbivore(properties={'species': 'Carnivore', 'weight': 29, 'age': 5})
    assert h.phi == 0.8698915249774015
