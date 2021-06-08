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

    def sorting_animals(self):  # pop, sort_by):  # do we need property here?
        """
            A function for sorting the animals.
            Herbivores are sorted weakest to fittest, since the weakest are eaten first
            Carnivores are sorted fittest to weakest, since the fittest eats first
            """
        sorted_herbivores_pop = sorted(self.herbivores_pop, key=operator.attrgetter('phi'))
        sorted_carnivores_pop = sorted(self.carnivores_pop, key=operator.attrgetter('phi'))
        sorted_carnivores_pop.reverse()
        self.herbivores_pop = sorted_herbivores_pop
        self.carnivores_pop = sorted_carnivores_pop
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

    def feed_carnivores(self):  # må testes!!
        '''
            1. sort herbivores and carnivores by fitness
            2. make the carnivores eat
            3. remove all eaten herbivores
        '''
        self.sorting_animals()
        list_carn = self.carnivores_pop
        list_herb = self.herbivores_pop
        killed = []

        for carn in list_carn:
            for herb in list_herb:
                carn.probability_kill_herbivore()
                if carn.kill == True:
                    carn.weight_weight_gain_after_eating_herb()
                    killed.append(herb)

        self.herbivores_pop = list(set(list_herb) - set(killed))
        self.carnivores_pop = list_carn

    def newborn_animals(self):  # make it work for both species
        """
            An animal gives birth maximum one time per year.The function birth_probability
            calculates if the animal will give birth or not and birth_weightloss calculates the new
            weight for the mother.
            The newborn must be added to the list of either herbivores or carnivores
            """
        self.counting_animals()

        # for herbivores
        list_h = self.herbivores_pop
        self.new_h = 0  # for testing
        list_new = []
        for k in range(self.N_herb):
            list_h[k].birth_probability(n=self.N_herb)
            # list_h[k].birth = True # har den der for testing siden jeg ikke får til mocker
            if list_h[k].birth is True:
                newborn = Herbivore(weight=list_h[k].newborn_birth_weight, age=0)
                list_h[k].birth_weight_loss(n=self.N_herb)
                list_new.append(newborn)
                self.new_h += 1  # for testing
        for k in list_new:
            list_h.append(k)
        self.herbivores_pop = list_h

        # for carnivores
        list_c = self.carnivores_pop
        self.new_c = 0  # for testing
        list_new = []
        for k in range(self.N_carn):
            list_c[k].birth_probability(n=self.N_carn)
            #  list_c[k].birth = True  # har den der for testing siden jeg ikke får til mocker
            if list_c[k].birth is True:
                newborn = Carnivore(weight=list_c[k].newborn_birth_weight, age=0)
                list_c[k].birth_weight_loss(n=self.N_carn)
                list_new.append(newborn)
                self.new_c += 1  # for testing
        for k in list_new:
            list_c.append(k)
        self.carnivores_pop = list_c

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

    def make_animals_age(self):  # blir alderen bare oppdatert på herbivore_pop nå? testes!
        """
            Each year the animals ages. Here we use the aging function from the herbivore class
            """
        animals = self.herbivores_pop + self.carnivores_pop
        for animal in animals:
            animal.aging()

    def make_animals_lose_weight(self):  # testes!!
        """
            Each year the animal loses weight based on their own weight and eta
            """
        animals = self.herbivores_pop + self.carnivores_pop
        for animal in animals:
            animal.weight_loss()

    def dead_animals_natural_cause(self):
        """
        Each year some animals will die of natural causes. We check if the animal dies or not
        by using the function death_probability. After we need to remove them from the from the
        list of animals
        """

        '''
        list_animals = self.herbivores_pop + self.carnivores_pop
        length = len(list_animals)
        list_dead = []
        self.dead = 0  # for testing?

        for k in range(length):
            list_animals[k].death_probability()
            if list_animals[k].death is True:
                list_dead.append(list_animals[k])
                self.dead += 1  # for testing

        self.herbivores_pop = list(set(list_a) - set(list_dead))
        '''
        # bruke death_probability

        # self.herbivores_pop = [herb for herb in self.herbivores_pop
                                # if herb.death is True]
        # self.carnivores_pop = [carn for carn in self.carnivores_pop
                                # if carn.death is True]


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
