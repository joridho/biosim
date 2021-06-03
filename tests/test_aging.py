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

#def test_herbivore_birth_weight():
    #assert 1 == 1

#def test_herbivore_weight_loss():
    # tror koden er feil,
    #h = herbivore()
    current_weight = h.weight
    #eta = h.p['eta']
    #h.weight_loss()
    #assert h.weight == current_weight - current_weight * eta

def test_herbivore_weight_gain():
    '''
        this is a test for testing if the herbivore gains weight when it eats as much as it wants to
        '''
    h = herbivore()
    current_weight = h.weight
    beta = h.p['beta']
    F = h.p['F']
    new_weight = current_weight + beta * F
    h.weight_gain()
    assert h.weight == new_weight


#def test_herbivore_fitness():



#def test_herbivore_birth():



#def test_herbivore_birth_weightloss():



def test_herbivore_death(mocker):
    mocker.patch('random.random', return_values=1)
    h = herbivore()
    for _ in range(100):
        assert h.death_probability() == True



#def test_herbivore_eat_fodder():












