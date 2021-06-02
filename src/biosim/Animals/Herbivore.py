# -*- encoding: utf-8 -*-

"""
This is a file that creates Herbivores by using the class function
"""

__author__ = 'Christianie Torres', 'Jorid Holmen'
__email__ = 'christianie.torres@nmbu.no', 'jorid.holmen@nmbu.no'

import random
import math


class herbivore:
    """
        def __init__(self):
            self.a_init = 0
            self.w_birth = 8.0
            self.sigma_birth = 1.5
            self.beta = 0.9
            self.eta = 0.05
            self.a_half = 40.0
            self.phi_age = 0.6
            self.w_half = 10.0
            self.phi_weight = 0.1
            self.mu = 0.25
            self.gamma = 0.2
            self.zeta = 3.5
            self.xi = 1.2
            self.omega = 0.4
            self.F = 10.0
            self.DeltaPhiMax = None
        """

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
    }  # har ikke inkludert a.init og deltaphimax

    random.seed(1)

    def aging(self):
        """
        A function for aging the animal
        """
        self.a += 1

    def birth_weight(self):
        """
            Sets value of birth weight from a gaussian distribution
            """
        # min_w = w_birth - sigma_birth
        # max_w = w_birth + sigma_birth
        # birthweight = random.randint(min_w, max_w)
        self.birth_weight = random.gauss(self.p['w_birth'], self.p['sigma_birth'])

    def weight_loss(self):
        """
            The animal loses weight each year
            """
        self.weight -= self.p['eta'] * self.weight

    def weight_gain(self):
        """
            The animal gains weight everytime they eat
            """
        self.weight += self.p['beta'] * self.p['F']

    def fitness(self):
        """
            The animal has a certain fitness. This function calculates the fitness for one animal,
            but does not update continously
            """
        q_plus = 1 / (1 + math.exp(self.p['phi_age'] * (self.a - self.p['a_half'])))
        q_minus = 1 / (1 + math.exp(-self.p['phi_weight'] * (self.weight - self.p['w_half'])))

        if self.weight <= 0:
            self.phi = 0
        else:
            self.phi = q_plus * q_minus

        if 0 >= self.phi or self.phi >= 1:
            return False

    def birth_probability(self):
        """
            Animals can mate if there are two or more animals of the same species in the same cell.
            The animals can give birth with a probability, which depends on fitness and weight.
            If the newborn weighs more than the mother, the probability of birth is zero.
            """
        variabel = self.p['gamma'] * self.phi * (N - 1)  # hvordan få tak i N
        birth_weight = self.birth_weight  # this is the weight of the possible newborn

        if variabel < 1:
            prob_birth = variabel
        elif self.p['omega'] < self.p['zeta'] * (self.p['w_birth'] + self.p['sigma_birth']):
            prob_birth = 0
        elif self.weight <= birth_weight:  # birth weight til nytt barn?
            prob_birth = 0
        elif N < 2:
            prob_birth = 0
        else:
            prob_birth = 1

        if random.random() < prob_birth:
            return True

    def birth_weightloss(self, birth_weight):
        """
            If the mother gives birth, she looses weight
            """
        self.weight -= self.p['zeta'] * birth_weight

    def death_probality(self):
        """
            The animal dies if it weighs nothing, but also with a probability of prob_death
            """
        if self.weight == 0:
            prob_death = 1
        else:
            prob_death = self.p['omega'] * (1 - self.phi)

        if random.random() < prob_death:
            return True

    # def migration(self):

    def __init__(self, weight=None, age=0):
        """

            """
        super().__init__(weight, age)

    def eat_fodder(self):
        """
            Herbivores tries to eat a certain amount in a year. However, how much the animal
            actually consumes depends on how much fodder is available in the cell.

            After it

            F_cell: how much food in the cell
            F: how much the herbivore wants to eat in a year (appetite)
            F_consumption: how much the herbivore actually eats

            after the consumption the herbivore gains weight
            """

        if F_cell >= self.p['F']:  # Hvordan skal vi kalle på F_cell
            F_cell -= self.p['F']
            herbivore.weight_gain()
        else:
            F_consumption = F_cell
            F_cell = 0
            self.weight += self.p[
                               'beta'] * F_consumption  # kunne kanskje brukt funskjonen til dette
