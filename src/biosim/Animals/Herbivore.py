# -*- encoding: utf-8 -*-

"""
This is a file that creates Herbivores by using the class function
"""

__author__ = 'Christianie Torres', 'Jorid Holmen'
__email__ = 'christianie.torres@nmbu.no', 'jorid.holmen@nmbu.no'

import random
import math

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
        self.DeltaPhiMax = None

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
        } # har ikke inkludert a.init og deltaphimax

        @classmethod
        def age(cls, a_init, year):
            self.a = a_init
            self.a += year

        def birthweight(self, sigma_birth, w_birth):
            min_w = w_birth - sigma_birth
            max_w = w_birth + sigma_birth
            birthweight = random.randint(min_w, max_w)

        @classmethod
        def weightloss(cls, w, year, eta):
            # self.w = w  # Need to find weight
            self.w -= eta*w
            # Make this happen each year

        @classmethod
        def weightgain(cls, w, F, beta):
            self.w += beta*F
            # Make this happen each time they eat

        @classmethod
        def fitness(cls, a, a_half, phi_age, w, w_half, phi_weight):
            if w <= 0:
                phi = 0
            else:
                phi = 1/(1+math.exp(phi_age(a-a_half)))*1/(1+math.exp(-phi_weight(w-w_half)))

            if 0 <= phi <= 1:
                True
            else:
                return False

        @classmethod
        def birth_probability(cls, gamma, phi, N, omega, zeta, w_birth, sigma_birth):
            variabel = gamma * phi * (N-1)

            if variabel < 1:
                p_birth = variabel
            elif omega  < zeta * (w_birth + sigma_birth):
                p_birth = 0
            else:
                p_birth = 1

            # How to make this happen maximum once per year

        @classmethod
        def birth_weightloss(cls, birthweight, zeta, w):
            self.w -= zeta*birthweight

        @classmethod
        def death(cls, w, phi, omega):
            if w == 0:
                p_death = 1
            else:
                p_death = omega * (1-phi)














