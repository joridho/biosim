# -*- coding: utf-8 -*-

__author__ = 'Jorid Holmen'
__email__ = 'jorid.holmen@nmbu.no'

from biosim.animals import herbivore
from biosim.Cell import lowland

import pandas
import matplotlib.pyplot as plt
import subprocess
import random
'''
<<<<<<< HEAD
=======

>>>>>>> origin/Simulation
'''
class biosim:

    def __init__(self, init_pop, seed = 10):  # mangler img og ymax

        #self.seed = random.seed(10)
        #self.init_pop = 2
        self.seed = random.seed(seed)
        if init_pop is None:
            self.init_pop = self.add_pop()

        self.init_pop = init_pop
        self.year = 0

    def add_pop(self):
        """
        Adds animal to the cell/island. These animals become the initial population
        """
        l = lowland()
        self.init_pop = l.adding_animals()
        #self.idk = len(self.init_pop)
        return self.init_pop

    #def feeding(self):
        """
            Herbivores eat yearly
            """

    #def procreation(self):
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

        l.make_herbivores_eat()
        l.newborn_animals()
        l.make_animals_age()
        l.make_animals_lose_weight()
        l.dead_animals_natural_cause()

        # reset
        l.reset_fodder()
        l.reset_appetite()
        l.reset_given_birth()

        self.year += 1

        return l.herbivores_pop


    def year(self):
        """
            Counts how many years to use in simulation
            """
        # n_year =

    def num_animals(self):
        """
            Counts how many animals there are in the cell/island, for use in simulation
            """
        self.N_animals = lowland.counting_animals()

    def simulate(self):
        """
            function for simulating

            1. start time
            2. add arrays for plotting
            3. add initial population (i eksempelet fra Plesser er dette i island class)
            4. initiate year_cycle
            5. plot

            plots:
            1. line graph for number of animals
            2. heat map for one cell with distribution of herbivores
            3. write down number of years
            4. map of island
            5. later heat map for one cell with distribution of carnivores
            """












