# -*- encoding: utf-8 -*-

"""
"""


__author__ = 'Christianie Torres'
__email__ = 'christianie.torres@nmbu.no'

from biosim.animals import herbivore, carnivore

def test_herbivore_age():
    """
    A test that checks that a herbivore has been created with age 0
    """
    h = herbivore()
    assert h.a == 0

def test_herbivore_weight():
    '''
        test to check if the herbivore has been given a weight
        '''
    h = herbivore()
    b = h.birth_weight
    assert h.weight == b

def test_herbivore_aging():
    """
    A test that checks that the herbivore ages for each year
    """
    h = herbivore()
    for n in range(10):
        h.aging()
        assert h.a == n + 1

def test_herbivore_birth_weight():
    """
    A test that checks that the herbivore have been given a birth_weight
    """
    h = herbivore()
    birth_w = h.birth_weight
    assert h.birth_weight == birth_w

def test_herbivore_weight_loss():
    '''
        this is a test for testing if the herbivore looses weight each year
    '''
    h = herbivore()
    current_weight = h.weight
    eta = h.p['eta']
    h.weight_loss()
    assert h.weight == current_weight - current_weight * eta

def test_herbivore_weight_gain():
    '''
        this is a test for testing if the herbivore gains weight when it eats as much as it wants to
        '''
    h = herbivore()
    current_weight = float(h.weight)
    beta = h.p['beta']
    F = h.p['F']
    new_weight = current_weight + beta * F
    h.weight_gain()
    assert h.weight == new_weight


def test_herbivore_fitness():
    """
    A test that checks that the herbivore have been given a fitness
    """
    h = herbivore()
    fitness = h.phi
    h.fitness()
    assert fitness == h.phi

def test_valid_fitness():
    """
    This is a test for checking that the fitness-function returns a phi-value between 0 and 1
    """
    for _ in range(100):
        h = herbivore()
        h.fitness()
        assert 0 <= h.phi <= 1

def test_no_newborn_when_mother_weighs_too_little():
    """
    This is a test that checks if the birth probability equals zero when the mother weighs to little.
    """
    h = herbivore(weight=3.5, a=3)
    h.birth_probability(n=3)
    assert h.prob_birth == 0

def test_no_newborn_when_to_few_animals(): #too
    """
    This is a test that checks if the birth probability equals zero when there are too few animals
    a cell.
    """

    h = herbivore(weight=32, a=3)
    h.birth_probability(n=1)
    assert h.prob_birth == 0

def test_no_newborn_if_newborn_too_fat():
    """
    This is a test that checks if the birth probability equals zero when the newborn weighs more
    than the mother
    """
    h = herbivore(weight=3, a=3)
    h.birth_probability(n=3)
    h.newborn_birth_weight = 5
    assert h.prob_birth == 0


def test_birth():
    'This is a test that checks if the Herbivore gives birth when it is supposed to'
    h = herbivore(weight=35, a=3)
    for _ in range(100):
        h.birth_probability(n=4)
        if h.birth_probability(n=4) == True:
            assert h.r < h.prob_birth
        else:
            assert h.r >= h.prob_birth

def test_herbivore_birth_weight_loss():
    ' This is a test that checks if the Mother looses the right amount of weight after giving birth'
    h = herbivore()
    current_weight = h.weight
    h.birth_weight_loss(n=40)
    assert h.weight == current_weight - h.p['zeta'] * h.newborn_birth_weight


def test_death():
    '''
    This is a test that checks if the Herbivore dies when it is supposed to'
    '''
    h = herbivore(weight=10)
    for _ in range(100):
        h.death_probability()
        if h.death == True:
            assert h.d < h.prob_death
        else:
            assert h.d >= h.prob_death

def test_herbivore_eat_fodder():
    h = herbivore()
    current_weight = h.weight
    h.eat_fodder(F_cell = h.p['F']) 
    #assert h.weight == current_weight + h.p['beta'] * h.f
    assert h.F_cell == 0   #apetiten F skal være tom 0. 
    # og F_celle skal være lik celle i start minus apetit (men blir 0 her pga de er like store duhhh)

def test_herbivore_gains_weight_after_eat_fodder():
    #Kan hende det er samme som weight_gain funksjonen
    '''
    This is a test that checks if the Herbivore gains the right amount of weight
    when it eats in a cell that has enough fodder that satisfies the Herbivore apetite
    '''
    h = herbivore()
    current_weight = h.weight
    h.eat_fodder(F_cell = h.p['F'])
    assert h.weight == current_weight + h.p['beta'] * h.f

def test_cell_empty_after_herbivore_eat_fodder():
    '''
    This is a test that checks if the cell is empty after the Herbivore has eaten in a cell that
     has enough fodder that satisfies the herbivores apetite'
    '''
    h = herbivore()
    h.eat_fodder(F_cell=h.p['F'])
    assert h.F_cell == 0


def test_weight_gain_after_eating():
    
    # This is a test that checks if the Herbivore gains the right amount of weight
    #when it eats in a cell that does not have enough fodder that satisfies the Herbivore apetite
    
    h = herbivore()
    current_weight = h.weight
    beta = h.p['beta']
    F = 8

    new_weight = current_weight + beta * F
    h.eat_fodder(F_cell= F)
    assert h.weight == new_weight
    #assert h.F_cell ==0
    #assert h.F_consumption == 8

def test_update_appetite():
    h = herbivore()
    h.eat_fodder(F_cell=4)
    assert h.p['F'] == 6


def test_update_F_cell():
    h = herbivore()
    h.eat_fodder(F_cell=800)
    assert h.F_cell == 800-10

def test_if_carnivore_gains_correct_weight():
    carn = carnivore()
    w = carn.weight
    herb = herbivore(weight=35)
    carn.weight_gain_after_eating_herb(herb)
    assert carn.weight == w + herb.weight * herb.p['beta']

def test_prob_kill():
    herb = herbivore(weight=35, a=3)
    carn = carnivore()
    for _ in range(100):
        carn.probability_kill_herbivore(herb)
        if carn.kill == True:
            assert carn.r < carn.prob_kill
        else:
            assert carn.r >= carn.prob_kill









