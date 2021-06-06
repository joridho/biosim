# -*- coding: utf-8 -*-

__author__ = 'Jorid Holmen'
__email__ = 'jorid.holmen@nmbu.no'

from biosim.animals import herbivore
from biosim.Cell import lowland, cell

import pandas
import matplotlib.pyplot as plt
import subprocess
import ran

class biosim:

    def __init__(self, init_pop, seed):  # mangler img og ymax

        self.seed = random.seed(10)

        self.init_pop = 2

    def add_pop(self):
        """
            Adds animal to the cell/island
            """
        self.init_pop = lowland.adding_animals()

    def feeding(self):
        """
            Herbivores eats yearly
            """

    def procreation(self):
        """
            Animals mate maximum once per year
            """

    # def migration(self):

    def year_cycle(self):
        """
            simulates one year

        Runs through each of the 6 yearly seasons for all cells.
        - Step 1: Animals feed
        - Step 2: Animals procreate
        - Step 3: Animals migrate
        - Step 4: Animals age
        - Step 5: Animals lose weight
        - Step 6: Animals die
            """
        l = lowland()
        l.make_herbivores_eat() # Animals feed
        l.reset_appetite()
        l.newborn_animals() #Animals procreate
        l.aging()           #Animals age
        l.make_animals_lose_weight() #Animals lose weight
        l.dead_animals_natural_cause() # Animals die
        l.counting_animals()

    def year(self):
        """
            Counts how many years to use in simulation
            """

    def num_animals(self):
        """
            Teller hvor mange dyr det er i cella/øya
            """

    def simulate(self):
        """
            function for simulating
            """

















