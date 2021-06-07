# -*- coding: utf-8 -*-

__author__ = 'Jorid Holmen'
__email__ = 'jorid.holmen@nmbu.no'

import biosim.animals
from biosim.Cell import lowland
from biosim.Map_Island import Map_Island

import pandas
import matplotlib.pyplot as plt
# import subprocess
import random
import time
# import os
import textwrap

'''
<<<<<<< HEAD
=======

>>>>>>> origin/Simulation
'''
class biosim:

    def __init__(self, island_geo, init_pop, seed = 10, ymaxanimals=None, cmaxanimals=None):  # mangler img og ymax

        #self.seed = random.seed(10)
        #self.init_pop = 2
        self.seed = random.seed(seed)
        if init_pop is None:
            self.init_pop = self.add_pop()

        if island_geo == None:
            island_geo = '-----' # vet ikke helt hva det skal bli enda
            self._island_map_graph = Map_Island(island_geo)
        else: #Går også an å inkl en elif som skal sjekke om island_geo er string
            self._island_map_graph = Map_Island(island_geo, init_pop)

        #ELSE RAISE VALUE ERROR

        self.init_pop = init_pop
        self.year = 0
        self.af_bio = 800



    def add_pop(self):
        """
        Adds animal to the cell/island. These animals become the initial population
        """
        l = lowland()
        self.init_pop = l.adding_animals()
        #self.idk = len(self.init_pop)
        #return self.init_pop

    #def feeding(self):
        """
            Herbivores eat yearly
            """

    #def procreation(self):
        """
            Animals mate maximum once per year
            """

    # def migration(self):

    def year_cycle(self):
        """
            simulates one year

        Runs through each of the 6 yearly seasons for all cells.
        - Step 1: Animals feed
        - Step 2: Animals procreate
        - Step 3: Animals migrate
        - Step 4: Animals age
        - Step 5: Animals lose weight
        - Step 6: Animals die
            """

        l = lowland()
        # l.herbivores_pop = self.init_pop  # må fjernes

        l.make_herbivores_eat()
        self.population_herb = l.herbivores_pop
        self.weight_year_cycle = [k.weight for k in l.herbivores_pop]  # for testing
        self.available_fodder = l.af  # for testing

        l.newborn_animals()
        l.make_animals_age()
        l.make_animals_lose_weight()
        l.dead_animals_natural_cause()

        # reset
        l.reset_fodder()
        #l.reset_appetite()
        l.reset_given_birth()

        self.year += 1

        return l.herbivores_pop


    def num_animals(self):
        """
            Counts how many animals there are in the cell/island, for use in simulation
            """
        self.N_animals = lowland().counting_animals()

'''
    def simulate(self):
        """
            function for simulating

            1. start time
            2. add arrays for plotting
            3. add initial population (i eksempelet fra Plesser er dette i island class)
            4. initiate year_cycle
            5. plot

            plots:
            1. line graph for number of animals
            2. heat map for one cell with distribution of herbivores
            3. write down number of years
            4. map of island
            5. later heat map for one cell with distribution of carnivores
            """

        phi_array_herb = []
        age_array_herb = []
        weight_array_herb = []
        N_herb = []
        N_carn = []
        year = []

        # values needed after stopping:
        number_of_simulated_years = 0
        total_number_of_animals = 0
        total_number_of_herbivores = 0
        total_number_of_carnivores = 0

        fig = plt.figure()
        ax1 = fig.add_subplot(3, 3, 1)  # map
        ax2 = fig.add_subplot(3, 3, 3)  # animal count
        ax3 = fig.add_subplot(3, 3, 4)  # herbivore distribution
        ax4 = fig.add_subplot(3, 3, 5)  # carnivore distribution
        ax5 = fig.add_subplot(3, 3, 6)  # fitness
        ax6 = fig.add_subplot(3, 3, 7)  # age
        ax7 = fig.add_subplot(3, 3, 8)  # weight

        # time counter
        axt = fig.add_axes([0.4, 0.8, 0.2, 0.2])  # llx, lly, w, h
        axt.axis('off')

        template = 'Count: {:5d}'
        txt = axt.text(0.5, 0.5, template.format(0),
                       horizontalalignment='center',
                       verticalalignment='center',
                       transform=axt.transAxes)  # relative coordinates

        plt.pause(0.01)  # pause required to make figure visible

        input('Press ENTER to begin counting')

        for k in range(30):
            txt.set_text(template.format(k))
            plt.pause(0.1)  # pause required to make update visible

        ax2.plt.plot(N_herb, self.year, 'b')
        ax2.plt.plot(N_carn, self.year, 'r')
        ax2.legend('Animals')

        ax3.set_xticks(1)
        ax3.set_xticks(1)
        ax3.set_title("Herbivore distribution")
        fig.tight_layout()
        ax3.plt.imshow(N_herb,)
'''


def setup_graphics(self):
    self.create_map()

def create_map(self):
    # geography
    #island_map = """WWWWW
    #WWLHW
    #WDDLW
    #WWWWW
    #"""
    # hver bokstav for fargeverdi
    #                R    G    B
    rgb_value = {'W': (0.0, 0.0, 1.0),  # blue
                 'L': (0.0, 0.6, 0.0),  # dark green
                 'H': (0.5, 1.0, 0.5),  # light green
                 'D': (1.0, 1.0, 0.5)}  # light yellow

    # hver bokstav I geography får rgb_value
    map_rgb = [[rgb_value[column] for column in row]
               for row in self.island_map_graph.splitlines()] # vet ikke hv Map_Island returnere enda

    # lager tom figur
    fig = plt.figure()

    # adder akser til tom figur (skal bli øy)
    ax_im = fig.add_axes([0.1, 0.1, 0.7, 0.8])  # llx, lly, w, h

    # viser øya m/vann
    ax_im.imshow(map_rgb)

    # hva gjør denne??????????????????
    ax_im.set_xticks(range(len(map_rgb[0])))
    ax_im.set_xticklabels(range(1, 1 + len(map_rgb[0])))
    ax_im.set_yticks(range(len(map_rgb)))
    ax_im.set_yticklabels(range(1, 1 + len(map_rgb)))

    # lager nytt koordinatsystem i figuren (x akse starter ved 80 % bredde (v->h) av figuren, y akse starter i 10 prosent høyde av figuren, har bredde som er på 10% av figuren, har høyde som er på 80% av figuren)
    ax_lg = fig.add_axes([0.85, 0.1, 0.1, 0.8])  # llx, lly, w, h
    ax_lg.axis('off')  # fjerner selve koordinatsystemet
    for ix, name in enumerate(('Water', 'Lowland',
                               'Highland',
                               'Desert')):  # enumarte gir tall/indeks til elementene i en liste ['katt', 'skole'] blir til ['0', 'katt', '1', 'skole']
        ax_lg.add_patch(plt.Rectangle((0., ix * 0.2), 0.3, 0.1,
                                      # tilsetter rektangler med x akse.. yakse ... bredde... og høyde..(samme som over)
                                      edgecolor='none',  # ingen ytterkant
                                      facecolor=rgb_value[
                                          name[0]]))  # første element i navn feks 'W'
        ax_lg.text(0.35, ix * 0.2, name,
                   transform=ax_lg.transAxes)  # legger til navn ved x akse... og yakse ...

    plt.show()  # viser plott











