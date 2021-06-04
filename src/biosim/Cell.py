# -*- coding: utf-8 -*-


__author__ = 'Jorid Holmen', 'Christianie Torres'
__email__ = 'jorid.holmen@nmbu.no', 'christianie.torres@nmbu.no'

import random
import operator

from biosim.animals import herbivore


class cell:
    """
        Class for cells
        """

    p = {'f_max': 800.0}

    def __init__(self):
        self._F = self.p['f_max']
        self._accessible = True
        self.herbivores_pop = []
        self.carnivores_pop = []

    def adding_animals(self):
        """
            Use of the animal class to add animals to the cell.
            """

    def sorting_animals(self):  # do we need property here?
        """
            A function for sorting the animals.
            Herbivores are sorted weakest to fittest, since the weakest are eaten first
            Carnivores are sorted fittest to weakest, since the fittest eats first
            """
        self.sorted_herbivores_pop = sorted(self.herbivores_pop, key=operator.attrgetter('phi'))

    def available_fodder_function(self):
        """
            At the beginning of the year the available fodder is f_max
            """
        self.available_fodder = self.p['f_max']

    def make_herbivores_eat(self):
        """
            The animals eats available fodder until their appetite is filled.
            The eat_fodder-function from the Herbivore class does this.
            Herbivores eat in a random order, and therefore need to be randomised

            This function can only be used once per year because of the available_fodder_function

            """
        self.available_fodder_function()
        while self.available_fodder >= 0:
            self.herb = random.choice(self.herbivores_pop)
            self.herb.eat_fodder(F_cell=25)
            self.available_fodder = self.herb.F_cell
            self.herbivores_pop.remove(self.herb)

    def newborn_animals(self):
        """
            An animal gives birth maximum one time per year.The function birth_probability
            calculates if the animal will give birth or not and birth_weightloss calculates the new
            weight for the mother.
            The newborn must be added to the list of either herbivores or carnivores
            """
        for ani in self.herbivores_pop:
            if ani.given_birth == False:
                if herbivore.birth_probability == True:
                    newborn = herbivore(weight=ani.newborn_birth_weight, a=0)
                    self.herbivores_pop.append(newborn)
                    ani.birth_weight_loss(N=self.N)
                    ani.given_birth == True

    def counting_animals(self):
        """
            A function for counting how many animals there are in the cell.
            We also need to differentiate between the different animals and provide to
            variables for this
            """
        # do we need to use property here?
        self.N = len(self.herbivores_pop)

    # yearly activities:

    def reset_fodder(self):
        """
            At the beginning of the year the amount of fodder resets to the default value
            """
        self.available_fodder_function()

    def reset_appetite(self):
        """
            The appetite is filled every year
            """

    def reset_given_birth(self):
        """
            An animal can only give birth once per year
            """
        for ani in self.herbivores_pop:
            ani.given_birth = False

    def make_animals_age(self):
        """
            Each year the animals ages. Here we use the aging function from the herbivore class
            """

    def make_animals_lose_weight(self):
        """
            Each year the animal loses weight based on their own weight and eta
            """

    def remove_animals(self):
        """
            When an animal dies, either natural causes or eaten, it needs to be taken of the
            list of animals.
            Animal also needs to be taken of the list when migrating
            """

    def dead_animals_natural_cause(self):
        """
            Each year some animals will die of natural causes. We check if the animal dies or not
            by using the function death_probability. After we need to remove them from the from the
            list of animals
            """


class lowland(cell):
    """
    subclass for lowland cells
    """

    # should have amount of fodder down here, not up in the cell class

    def __init__(self):
        """
            Initialises lowland class
            """
        super().__init__()
