# -*- encoding: utf-8 -*-

"""
This is a file that creates Herbivores by using the class function
"""

__author__ = 'Christianie Torres'
__email__ = 'christianie.torres@nmbu.no'

import random

class herbivore():
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
        #self.DeltaPhiMax =

        @classmethod
        def age(cls, a_init, year):
            self.a = a_init
            self.a += year

        @classmethod
        def birthweight(cls, sigma_birth, w_birth):
            min_weight = w_birth - sigma_birth
            max_weight = w_birth + sigma_birth
            birthweight = random.randint(min_weight, max_weight)

        @classmethod
        def weightloss(cls, weight, year, eta):
            # self.weight = weight   # Need to find weight
            self.weight -= eta*weight
            # Make this happen each year

        @classmethod
        def weightgain(cls, weight, F, beta):
            self.weight += beta*F
            # Mkae this happen each time they eat




