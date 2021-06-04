# -*- encoding: utf-8 -*-

"""
"""

__author__ = 'Christianie Torres'
__email__ = 'christianie.torres@nmbu.no'

from biosim.animals import herbivore

import math
import random
import pytest
import scipy.stats as stats

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
    h = herbivore()
    birth_w = h.birth_weight
    assert h.birth_weight == birth_w

def test_herbivore_weight_loss():
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
    h = herbivore()
    fitness = h.phi
    h.fitness()
    assert fitness == h.phi

def test_valid_fitness():
    for _ in range(100):
        h = herbivore()
        h.fitness()
        assert 0 <= h.phi <= 1

def test_no_newborn_when_mother_weighs_too_little():
    h = herbivore(weight=3.5, a=3)
    h.birth_probability(N=3)
    assert h.prob_birth == 0

def test_no_newborn_when_to_few_animals():
    h = herbivore(weight=4, a=3)
    h.birth_probability(N=1)
    assert h.prob_birth == 0

def test_no_newborn_if_newborn_too_fat():
    h = herbivore(weight=20, a=3)
    h.birth_probability(N=3)
    h.newborn_birth_weight = 5
    assert h.prob_birth == 0

def test_birth():
    h = herbivore(weight=35, a=3)
    for _ in range(100):
        assert h.birth_probability(N=4) == True

def test_herbivore_birth_weight_loss():
    h = herbivore()
    w = h.weight
    h.birth_weight_loss(N=40)
    assert h.weight == w - h.p['zeta'] * h.newborn_birth_weight

def test_death():
    h = herbivore(weight=10)
    for _ in range(100):
        assert h.death_probability() == True

def test_herbivore_eat_fodder():
    h = herbivore()
    h.eat_fodder(F_cell = h.p['F'])
    assert h.F_cell == 0

def test_weight_gain_after_eating():
    h = herbivore()
    current_weight = float(h.weight)
    beta = h.p['beta']
    F = 8
    new_weight = current_weight + beta * F
    h.eat_fodder(F_cell=8)
    assert h.weight == new_weight










