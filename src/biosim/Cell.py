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

    def __init__(self, population):

        self.herbivores_pop = []
        self.carnivores_pop = []
        for animal_info in population:
            if animal_info['species'] == 'Herbivore':
                self.herbivores_pop.append(Herbivore(animal_info))
            else:
                self.carnivores_pop.append(Carnivore(animal_info))

    @classmethod
    def set_given_parameters(cls, params):
        """
            Saves the parameters for the different cells for use in Cell class
            """
        for parameter in params:
            if parameter in cls.p:
                cls.p[parameter] = params[parameter]

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

        for animal in self.herbivores_pop:
            animal.eat_fodder(F_cell=self.af)  # make the herbivore eat
            self.af -= animal.F_consumption  # change the amount of fodder in the cell

    def available_herbivores_for_carnivores(self):
        self.herbivores_weight_sum = 0
        for k in self.herbivores_pop:
            self.herbivores_weight_sum += k.weight

    def feed_carnivores(self):  # må testes!!
        """
            1. sort herbivores and carnivores by fitness
            2. make the carnivores eat
            3. make the carnivores gain weight
            4. remove all eaten herbivores
        """
        self.sorting_animals()
        #list_carn = []
        list_herb = self.herbivores_pop
        killed = []
        self.eaten = 0  # for testing


        for carn in self.carnivores_pop:
            for herb in self.herbivores_pop:
                if carn.probability_kill_herbivore(herb) is True:
                    if herb not in killed:
                        carn.weight_gain_after_eating_herb(herb)
                        killed.append(herb)
                        self.eaten +=1
            #list_carn.append(carn)
                    #eaten.append(carn)
                    #list_carn.remove(carn)

        self.herbivores_pop = list(set(list_herb) - set(killed))
        #for k in eaten:
            #list_carn.append(k)
        #self.carnivores_pop = list_carn

    def newborn_animals(self):  # make it work for both species
        """
            An animal gives birth maximum one time per year.The function birth_probability
            calculates if the animal will give birth or not and birth_weight_loss calculates the new
            weight for the mother.
            The newborn must be added to the list of either herbivores or carnivores
            """
        self.counting_animals()

        # for herbivores
        list_h = self.herbivores_pop
        self.new_h = 0  # for testing
        self.list_new_h = []
        for k in range(self.N_herb):
            list_h[k].will_the_animal_give_birth(n=self.N_herb)
            #list_h[k].birth = True # is there for testing since mocker doesn't work
            if list_h[k].birth is True:
                newborn = Herbivore(weight=list_h[k].newborn_birth_weight, age=0)
                list_h[k].birth_weight_loss(newborn_birth_weight=newborn.weight)
                self.list_new_h.append(newborn)
                self.new_h += 1  # for testing
        for k in self.list_new_h:
            list_h.append(k)
        self.herbivores_pop = list_h

        # for carnivores
        list_c = self.carnivores_pop
        self.new_c = 0  # for testing
        self.list_new_c = []  # for testing
        for k in range(self.N_carn):
            list_c[k].will_the_animal_give_birth(n=self.N_carn)
            # list_c[k].birth = True  # there for testing because mocker doesn't work
            if list_c[k].birth is True:
                newborn = Carnivore(weight=list_c[k].newborn_birth_weight, age=0)
                list_c[k].birth_weight_loss(newborn_birth_weight=newborn.weight)
                self.list_new_c.append(newborn)
                self.new_c += 1  # for testing
        for k in self.list_new_c:
            list_c.append(k)
        self.carnivores_pop = list_c

    def move_animals(self):
        herbs_move = []
        for herb in self.herbivores_pop:
            if herb.move_single_animal() == True:
                herbs_move.append(herb)

        herbs_stay_in_cell = self.herbivores_pop - herbs_move
        herbs_in_new_cell = herbs_move

        carns_move = []
        for carn in self.carnivores_pop:
            if carn.move_single_animal() == True:
                carns_move.append(carn)    # Hvordan få dem til å bevege seg til hver sin celle? Lister?

        carns_stay_in_cell = self.carnivores_pop - carns_move
        carns_in_new_cell = carns_move # Hvordan legge denne lista til i en ny celle`?


    def counting_animals(self):
        """
            A function for counting how many animals there are in the cell.
            We also need to differentiate between the different animals and provide to
            variables for this
            """
        self.N_herb = len(self.herbivores_pop)
        self.N_carn = len(self.carnivores_pop)

    # yearly activities:

    def make_animals_age(self):
        """
            Each year the animals ages. Here we use the aging function from the herbivore class
            """
        # animals = self.herbivores_pop + self.carnivores_pop
        for animal in self.herbivores_pop:
            animal.aging()
        for animal in self.carnivores_pop:
            animal.aging()

    def make_animals_lose_weight(self):
        """
            Each year the animal loses weight based on their own weight and eta
            """
        for animal in self.herbivores_pop:
            animal.weight_loss()
        for animal in self.carnivores_pop:
            animal.weight_loss()

    def dead_animals_natural_cause(self):
        """
        Each year some animals will die of natural causes. We check if the animal dies or not
        by using the function death_probability. After we need to remove them from the from the
        list of animals
        """
        self.dead = 0  # for testing

        herbs = []
        for herb in self.herbivores_pop:
            herb.death_probability()
            if herb.will_the_animal_die() is False:
                herbs.append(herb)
            else:
                self.dead += 1

        carns = []
        for carn in self.carnivores_pop:
            carn.death_probability()
            if carn.will_the_animal_die() is False:
                carns.append(carn)
            else:
                self.dead += 1

        self.herbivores_pop = herbs
        self.carnivores_pop = carns


class Lowland(Cell):
    """
    subclass for lowland cells
    """
    p = {'f_max': 800.0}

    def __init__(self, population):
        """
            Initialises lowland class
            """
        super().__init__(population)


class Highland(Cell):
    """
    subclass for highland class
    """
    p = {'f_max': 300.0}

    def __init__(self, population):
        """
            Initialises highland class
            """
        super().__init__(population)


class Desert(Cell):
    """
    subclass for highland class
    """
    p = {'f_max': 0}

    def __init__(self, population):
        """
            Initialises desert class
            """
        super().__init__(population)


class Water(Cell):
    """
    subclass for highland class
    """
    p = {'f_max': 0}

    def __init__(self, population):
        """
            Initialises water class
            """
        super().__init__(population)
