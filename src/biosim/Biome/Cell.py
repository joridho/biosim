# -*- coding: utf-8 -*-


__author__ = 'Jorid Holmen', 'Christianie Torres'
__email__ = 'jorid.holmen@nmbu.no', 'christianie.torres@nmbu.no'

import random
from biosim.Animals import herbivores

class Cell:
    """
    Class for cells
    """

    p = {'f_max': 800.0}

    def __init__(self):
        self._F = self.p['f_max']
        self.herbivores = []

    def adding_animals(self):
        """
        Use of the animal class to add animals to the cell
        """


class Lowland(Cell):
    """
    subclass for lowlandcells
    """
