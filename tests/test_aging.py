# -*- encoding: utf-8 -*-

"""
"""

__author__ = 'Christianie Torres'
__email__ = 'christianie.torres@nmbu.no'

from biosim.animals import animal

import math
import random
import pytest

def test_herbivore_created():
    h = animal(weight= 5, a = 0)
    assert h.a == 0

#def test_fitness():
    #for anim
