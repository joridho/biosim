# -*- coding: utf-8 -*-

__author__ = 'Jorid Holmen'
__email__ = 'jorid.holmen@nmbu.no'

from biosim.animals import Herbivore, Carnivore
from biosim.Cell import Lowland, Highland, Desert, Water
from biosim.MapIsland import Map_Island
import operator

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


class BioSim:

    def __init__(self, island_geo, init_pop, seed=10, img_dir=None, img_base=None, img_years=None):
        # self.seed = random.seed(10)
        # self.init_pop = 2
        # self.seed = random.seed(seed)
        random.seed(seed)  # ??

        #if init_pop is None:
         #   self.init_pop = self.add_population()  # Trengs ikke

        # init_pop = Herbivore(weight=init_pop['weight'], a=init_pop['age'])

        self.island_map_graph = Map_Island(island_geo, init_pop)
        self.island_map_graph.create_map_dict() # koordinatene i kart får tilhørende lister med dyr

        self.num_years_simulated = 0

        # if island_geo == None:  # trenger vi denne? er jo input senere
        # island_geo = '-----' # vet ikke helt hva det skal bli enda, noe med random?
        # self._island_map_graph = Map_Island(island_geo)
        # else: #Går også an å inkl en elif som skal sjekke om island_geo er string

    '''
    def set_animal_parameters(self, species, p):
        """
        Set parameters for animal species.

        :param species: String, name of animal species
        :param p: Dict with valid parameter specification for species
        """
        
        class_names = {'Herbivores': Herbivore,
                       'Carnivore': Carnivore}
        for param_name in p.keys():
            if param_name in class_names[species].p:
                if p[param_name] >= 0 and param_name is not "DeltaPhiMax" \
                        and param_name is not "eta" and param_name is not "F":
                    class_names[species].p[param_name] = p[
                        param_name]
                # checks special criteria for eta
                elif param_name is "eta" and 0 <= p[param_name] <= 1:
                    class_names[species].p[param_name] = p[
                        param_name]
                # checks special criteria for F
                elif param_name is "F" and 0 < p[param_name]:
                    class_names[species].p[param_name] = p[
                        param_name]
                # checks special criteria for DeltaPhiMax
                elif param_name is "DeltaPhiMax" and p[param_name] > 0:
                    class_names[species].p[param_name] = p[
                        param_name]
                else:
                    raise ValueError(f'{p[param_name]} is an invalid '
                                     f'parameter value for parameter '
                                     f'{param_name}!')
            else:
                raise ValueError(f'{param_name} is an invalid parameter name!')

    def set_landscape_parameters(self, landscape, params):
        """
        Set parameters for landscape type.

        :param landscape: String, code letter for landscape
        :param params: Dict with valid parameter specification for landscape
        """
    '''

    def simulate(self, years):
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

        # phi_array_herb = []
        # age_array_herb = []
        # weight_array_herb = []
        # N_herb = []
        # N_carn = []
        # V year = []

        self.island_map_graph.year_cycle()

        pop = []
        for cell in self.island_map_graph.map.values():
            pop += cell.herbivores_pop

        self.island_map_graph.create_population_dict()
        assert len(m.population[(2, 2)]) == 50

        print(len(self.island_map_graph.population([2, 2])))

        #print("herbivores: ", len(pop))

        self.num_years_simulated += 1

        '''
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

        ax2.plot(N_herb, self.num_years_simulated, 'b')
        ax2.plot(N_carn, self.num_years_simulated, 'r')
        ax2.legend('Animals')

        ax3.set_xticks(1)
        ax3.set_xticks(1)
        ax3.set_title("Herbivore distribution")
        fig.tight_layout()
        ax3.plt.imshow(N_herb,)
        '''

    '''
    def setup_graphics(self): ikke fra plesser 
        self.create_map()

    def create_map(self): ikke fra plesser 
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
    '''

    def adding_population(self, population):
        """
            Adds animal to the cell/island. These animals become the initial population
            """
        #self.herbivores_pop = self.island_map_graph.add_population() # feil
        return self.island_map_graph.add_population(population)

        #for k in range(50):
            #Lowland.herbivores_pop.append(Herbivore())

        # self.init_pop = l.adding_animals()
        # self.idk = len(self.init_pop)
        # return self.init_pop

    @property
    def year(self):
        """Last year simulated."""
        return self.num_years_simulated

    @property
    def num_animals(self):
        """Total number of animals on island."""
        num_carnivores = 0  # len(lowland.carnivores_pop)
        num_herbivores = len(self.island_map_graph.year_cycle())
        num_animals = num_carnivores + num_herbivores
        return num_animals

    @property
    def num_animals_per_species(self):
        """Number of animals per species in island, as dictionary."""
        '''
        num_animals_per_species = {"Herbivore": 0, "Carnivore": 0}
        for k in self.island_map.map.values():
            num_animals_per_species["Herbivore"] += len(lowland.pop_herb)
            num_animals_per_species["Carnivore"] += 0  # len(lowland.pop_carn)
        return num_animals_per_species()
        '''
        #num_animals_per_species = {"Herbivore": 0, "Carnivore": 0}
        #num_animals_per_species["Herbivore"] = len(Lowland.herbivore_pop)
        #num_animals_per_species["Carnivore"] = 0  # len(lowland.carnivore_pop)

        '''
    def make_movie(self): denne er fra Plesser 
        """Create MPEG4 movie from visualization images saved."""
    '''
