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
        # self._F = self.p['f_max']
        self.af = self.p['f_max']
        self._accessible = True
        self.herbivores_pop = []
        self.carnivores_pop = []

    def adding_animals(self):
        """
            Use of the animal class to add animals to the cell.
            """
        for k in range(50):
            self.herbivores_pop.append(herbivore())

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
        self.af = self.p['f_max']

    def make_herbivores_eat(self):

        """
            The animals eats available fodder until their appetite is filled.
            The eat_fodder-function from the Herbivore class does this.
            Herbivores eat in a random order, and therefore need to be randomised

            This function can only be used once per year because of the available_fodder_function

   
         """
        self.available_fodder_function()
        length = len(self.herbivores_pop)
        still_alive = []
        apetite = self.herbivores_pop[0].p['F']
        for _ in range(length):
            herb = random.choice(self.herbivores_pop)
            if self.af >= 0:
                herb.p['F'] = apetite
                herb.eat_fodder(F_cell=self.af)
                self.af -= herb.F_consumption
                still_alive.append(herb)
                self.herbivores_pop.remove(herb)
        self.herbivores_pop.extend(still_alive)



    def newborn_animals(self):
        """
            An animal gives birth maximum one time per year.The function birth_probability
            calculates if the animal will give birth or not and birth_weightloss calculates the new
            weight for the mother.
            The newborn must be added to the list of either herbivores or carnivores
            """
        list_h = self.herbivores_pop
        self.counting_animals()
        self.reset_given_birth() # must be removed later
        length = len(list_h)
        for k in range(length):
            list_h[k].birth_probability(n=self.N)
            list_h[k].prob_birth = True
            if list_h[k].given_birth is False and list_h[k].prob_birth is True:
                newborn = herbivore(weight=list_h[k].newborn_birth_weight, a=0)
                list_h[k].birth_weight_loss(n=self.N)
                list_h[k].given_birth is True # burde være riktig
                list_h.append(newborn)  # skal være riktig
        self.herbivores_pop = list_h

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
        for k in range(len(self.herbivores_pop)):
            herbivore.p['F'] = 10.0
            self.herbivores_pop[k].p['F'] = 10.0

    def reset_given_birth(self):
        """
            An animal can only give birth once per year
            """
        for k in range(len(self.herbivores_pop)):
            self.herbivores_pop[k].given_birth = False

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
        for k in range(length):
            list_a[k].death_probability()
            if list_a[k].prob_death is True:
                # self.remove is True
                # self.remove_animals()
                list_a.remove(list_a[k])
        self.herbivores_pop = list_a

    def remove_animals(self):
        """
            When an animal dies, either natural causes or eaten, it needs to be taken of the
            list of animals.
            Animal also needs to be taken of the list when migrating
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
