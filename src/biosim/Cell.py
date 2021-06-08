# -*- coding: utf-8 -*-


__author__ = 'Jorid Holmen', 'Christianie Torres'
__email__ = 'jorid.holmen@nmbu.no', 'christianie.torres@nmbu.no'

import random
import operator

from biosim.animals import Herbivore, Carnivore


class Cell:
    """
        Class for cells
        """

    p = {'f_max': 800.0}

    def __init__(self):

        self._accessible = True
        self.herbivores_pop = []
        self.carnivores_pop = []

    def sorting_animals(self, pop, sort_by):  # do we need property here?
        """
            A function for sorting the animals.
            Herbivores are sorted weakest to fittest, since the weakest are eaten first
            Carnivores are sorted fittest to weakest, since the fittest eats first
            """
        self.sorted_herbivores_pop = sorted(pop, key=operator.attrgetter(sort_by))
        self.sorted_carnivores_pop = sorted(pop, key=operator.attrgetter(sort_by))
        self.sorted_carnivores_pop.reverse()
        # my get an error later, just read the error and we will be good

    def make_herbivores_eat(self):

        """
            The animals eats available fodder until their appetite is filled.
            The eat_fodder-function from the Herbivore class does this.
            Herbivores eat in a random order, and therefore need to be randomised

            This function can only be used once per year because of the available_fodder_function
         """
        self.af = self.p['f_max']
        random.shuffle(self.herbivores_pop)

        for k in self.herbivores_pop:
            k.eat_fodder(F_cell=self.af)  # make the herbivore eat
            self.af -= k.F_consumption  # change the amount of fodder in the cell

    def available_herbivores_for_carnivores(self):
        self.herbivores_weight_sum = 0
        for k in self.herbivores_pop:
            self.herbivores_weight_sum += k.weight

    def feed_carnivores(self):
        '''
            1. sort herbivores and carnivores by fitness
            2. make the carnivores eat
            3. remove all eaten herbivores
        '''


    def newborn_animals(self):  # make it work for bort species
        """
            An animal gives birth maximum one time per year.The function birth_probability
            calculates if the animal will give birth or not and birth_weightloss calculates the new
            weight for the mother.
            The newborn must be added to the list of either herbivores or carnivores
            """
        list_h = self.herbivores_pop
        self.counting_animals()

        self.new = 0  # for testing
        list_new = []

        for k in range(self.N):
            list_h[k].birth_probability(n=self.N)

            if list_h[k].birth is True:
                newborn = Herbivore(weight=list_h[k].newborn_birth_weight, age=0)
                list_h[k].birth_weight_loss(n=self.N)
                list_new.append(newborn)
                self.new += 1  # for testing

        for k in list_new:
            list_h.append(k)

        self.herbivores_pop = list_h

    def counting_animals(self):
        """
            A function for counting how many animals there are in the cell.
            We also need to differentiate between the different animals and provide to
            variables for this
            """
        self.N_herb = len(self.herbivores_pop)
        self.N_carn = len(self.carnivores_pop)


    # yearly activities:

    # make the yealy activities work for both species

    def make_animals_age(self):
        """
            Each year the animals ages. Here we use the aging function from the herbivore class
            """
        for k in range(len(self.herbivores_pop)):
            self.herbivores_pop[k].aging()

    def make_animals_lose_weight(self):
        """
            Each year the animal loses weight based on their own weight and eta
            """
        for k in range(len(self.herbivores_pop)):
            self.herbivores_pop[k].weight_loss()

    def dead_animals_natural_cause(self):
        """
        Each year some animals will die of natural causes. We check if the animal dies or not
        by using the function death_probability. After we need to remove them from the from the
        list of animals
        """
        list_a = self.herbivores_pop
        length = len(list_a)
        list_dead = []
        self.dead = 0
        for k in range(length):
            list_a[k].death_probability()
            if list_a[k].death is True:
                list_dead.append(list_a[k])
                self.dead += 1  # for testing
        self.herbivores_pop = list(set(list_a) - set(list_dead))


class Lowland(Cell):
    """
    subclass for lowland cells
    """

    # should have amount of fodder down here, not up in the cell class

    def __init__(self):
        """
            Initialises lowland class
            """
        super().__init__()
