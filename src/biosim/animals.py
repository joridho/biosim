# -*- encoding: utf-8 -*-

"""
This is a file that creates animals by using the class function
"""

__author__ = 'Christianie Torres', 'Jorid Holmen'
__email__ = 'christianie.torres@nmbu.no', 'jorid.holmen@nmbu.no'

import random
import math


class animal:
    """
    This i a class for animals on the island
    """

    random.seed(1)

    p = {  # Dictionary of parameters belonging to the Herbivore class
        "w_birth": 8.0,
        "sigma_birth": 1.5,
        "beta": 0.9,
        "eta": 0.05,
        "a_half": 40.0,
        "phi_age": 0.6,
        "w_half": 10.0,
        "phi_weight": 0.1,
        "mu": 0.25,
        "gamma": 0.2,
        "zeta": 3.5,
        "xi": 1.2,
        "omega": 0.4,
        "F": 10.0,
    }

    def __init__(self, weight, a):
        self.a = a

        if weight is None:
            self.birth_weight_function()
            self.weight = self.birth_weight
        else:
            self.weight = float(weight)  # unsure about float

        # self.phi = self.fitness()
        self.fitness()
        self.given_birth = False

        # self.birth_weight = self.birth_weight()

    def aging(self):
        """
            A function for aging the animal
            """
        self.a += 1

    def birth_weight_function(self):
        """
            Sets value of birth weight from a gaussian distribution
            """
        self.birth_weight = random.gauss(self.p['w_birth'], self.p['sigma_birth'])
        return self.birth_weight

    def weight_loss(self):
        """
            The animal loses weight each year
            """
        weight_minus = self.p['eta'] * self.weight  # self.weight is method. Does not work in test
        self.weight -= weight_minus

    def weight_gain(self):
        """
            The animal gains weight everytime they eat. In this function, appetite is described as
            what is eaten, but in some cases that is not possible.
            """
        weight_plus = self.p['beta'] * self.p['F']
        self.weight += weight_plus

    def fitness(self):
        """
            The animal has a certain fitness. This function calculates the fitness for one animal,
            but does not update continuously
            """
        q_plus = 1 / (1 + math.exp(self.p['phi_age'] * (self.a - self.p['a_half'])))
        q_minus = 1 / (1 + math.exp(-self.p['phi_weight'] * (self.weight - self.p['w_half'])))

        if self.weight <= 0:
            self.phi = 0
        else:
            self.phi = q_plus * q_minus

        if 0 >= self.phi or self.phi >= 1:
            return False
        else:
            return self.phi

    def birth_probability(self,n):
        """
            Animals can mate if there are two or more animals of the same species in the same cell.
            The animals can give birth with a probability, which depends on fitness and weight.
            If the newborn weighs more than the mother, the probability of birth is zero.
            """
        self.variable = self.p['gamma'] * self.phi * (n - 1)
        self.newborn_birth_weight = self.birth_weight_function()
                                                          # this is the weight of the possible newborn

        if self.weight < self.p['zeta'] * (self.p['w_birth'] + self.p['sigma_birth']):
            self.prob_birth = 0
        elif self.weight <= self.newborn_birth_weight:  # birth weight to newborn
            self.prob_birth = 0
        elif n < 2:
            self.prob_birth = 0
        elif self.variable < 1:
            self.prob_birth = self.variable
        else:
            self.prob_birth = 1

        self.r = random.random()

        if self.r < self.prob_birth:
            self.birth = True
        else:
            self.birth = False

    def birth_weight_loss(self,n):
        """
            If the mother gives birth, she looses weight
            """
        self.birth_probability(n)
        self.weight -= self.p['zeta'] * self.newborn_birth_weight

    def death_probability(self):
        """
            The animal dies if it weighs nothing, but also with a probability of prob_death
            """
        if self.weight == 0:
            self.prob_death = 1
        else:
            self.prob_death = self.p['omega'] * (1 - self.phi)

        self.d = random.random()

        if self.d < self.prob_death:
            self.death = True
        else:
            self.death = False #self.prob_death

    # def migration(self):


class herbivore(animal):
    """
    this is a class for herbivores on the island
    """

    def __init__(self, weight=None, a=0):
        """
        initialisation of weight and age for a new herbivore
            """
        super().__init__(weight, a)

    def eat_fodder(self, F_cell):
        """
            Herbivores tries to eat a certain amount in a year. However, how much the animal
            actually consumes depends on how much fodder is available in the cell.

            After it

            F_cell: how much food in the cell
            F: how much the herbivore wants to eat in a year (appetite)
            F_consumption: how much the herbivore actually eats

            after the consumption the herbivore gains weight
            """
        self.F_cell = F_cell
        if self.F_cell >= self.p['F']:
            self.F_cell -= self.p['F']
            self.weight_gain()
            #self.f = self.p['F']
            self.F_consumption = self.p['F']
            self.p['F'] = 0
        else:
            self.F_consumption = self.F_cell
            self.F_cell = 0
            self.weight += self.p['beta'] * self.F_consumption
                                            # could use weight_gain function for this
            self.p['F'] -= self.F_consumption
