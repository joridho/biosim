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



