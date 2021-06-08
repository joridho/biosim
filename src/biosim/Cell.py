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

    ''' skal ikke være her, brukes senere 
    def adding_animals(self):
        """
            Use of the animal class to add animals to the cell.
            """
        for k in range(50):
            self.herbivores_pop.append(Herbivore())
        return self.herbivores_pop
    '''

    def sorting_animals(self, pop, sort_by):  # do we need property here?
        """
            A function for sorting the animals.
            Herbivores are sorted weakest to fittest, since the weakest are eaten first
            Carnivores are sorted fittest to weakest, since the fittest eats first
            """
        self.sorted_herbivores_pop = sorted(pop, key=operator.attrgetter(sort_by))
        # my get an error later, just read the error and we will be good



    ''' usikker på behovet for denne 
    def available_fodder_function(self):
        """
            At the beginning of the year the available fodder is f_max
            """
        self.af = self.p['f_max']
    '''



    def make_herbivores_eat(self):

        """
            The animals eats available fodder until their appetite is filled.
            The eat_fodder-function from the Herbivore class does this.
            Herbivores eat in a random order, and therefore need to be randomised

            This function can only be used once per year because of the available_fodder_function
         """
        self.af = self.p['f_max']
        list = self.herbivores_pop
        random.shuffle(list)

        for k in list:
            # make the herbivore eat:
            k.eat_fodder(F_cell=self.af)

            consumption = k.F_consumption
            # self.spist.append(consumption)  # for testing

            # make the herbivore gain weight:
            k.weight_gain(consumption)

            # change the amount of fodder in the cell:
            self.af -= consumption

        self.herbivores_pop = list

    def newborn_animals(self):
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
                newborn = Herbivore(weight=list_h[k].newborn_birth_weight, a=0)
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
        self.N = len(self.herbivores_pop)


    # yearly activities:

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

    def remove_animals(self):
        """
            When an animal dies, either natural causes or eaten, it needs to be taken of the
            list of animals.
            Animal also needs to be taken of the list when migrating
            """


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
