# -*- encoding: utf-8 -*-

"""
"""

__author__ = 'Christianie Torres'
__email__ = 'christianie.torres@nmbu.no'

from biosim.animals import herbivore

import math
import random
import pytest

def test_herbivore_created():
    """
    A test that checks that a herbivore has been created
    """

    h = herbivore()
    assert h.a == 0

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
    w_birth = h.p['w_birth']
    sigma_birth = h.p['sigma_birth']
    min_weight = w_birth - sigma_birth * 3
    max_weight = w_birth + sigma_birth * 3
    w = gauss(w_birth, sigma_birth)
    h.birth_weight()
    assert h.birth_weight in w


#def test_herbivore_death(mocker):
    #mocker.patch('random.random', return_values=1)
    #h = herbivore()
    #for _ in range(100):
        #assert h.death_probability() == True







