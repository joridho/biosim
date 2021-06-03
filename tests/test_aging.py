# -*- encoding: utf-8 -*-

"""
"""

__author__ = 'Christianie Torres'
__email__ = 'christianie.torres@nmbu.no'

from biosim.animals import herbivore

def test_aging():
    h = herbivore()
    assert h.age == 0

def test_