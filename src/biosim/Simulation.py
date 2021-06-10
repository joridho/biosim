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

    def __init__(self, island_geo, init_pop, seed,
                 vis_years=1, ymax_animals=None, cmax_animals=None, hist_specs=None,
                 img_dir=None, img_base=None, img_fmt='png', img_years=None,
                 log_file=None):

        """
        :param island_geo: Multi-line string specifying island geography
        :param init_pop: List of dictionaries specifying initial population
        :param seed: Integer used as random number seed
        :param ymax_animals: Number specifying y-axis limit for graph showing animal numbers
        :param cmax_animals: Dict specifying color-code limits for animal densities
        :param hist_specs: Specifications for histograms, see below
        :param vis_years: years between visualization updates (if 0, disable graphics)
        :param img_dir: String with path to directory for figures
        :param img_base: String with beginning of file name for figures
        :param img_fmt: String with file type for figures, e.g. 'png'
        :param img_years: years between visualizations saved to files (default: vis_years)
        :param log_file: If given, write animal counts to this file

        If ymax_animals is None, the y-axis limit should be adjusted automatically.
        If cmax_animals is None, sensible, fixed default values should be used.
        cmax_animals is a dict mapping species names to numbers, e.g.,
           {'Herbivore': 50, 'Carnivore': 20}

        hist_specs is a dictionary with one entry per property for which a histogram shall be shown.
        For each property, a dictionary providing the maximum value and the bin width must be
        given, e.g.,
            {'weight': {'max': 80, 'delta': 2}, 'fitness': {'max': 1.0, 'delta': 0.05}}
        Permitted properties are 'weight', 'age', 'fitness'.

        If img_dir is None, no figures are written to file. Filenames are formed as

            f'{os.path.join(img_dir, img_base}_{img_number:05d}.{img_fmt}'

        where img_number are consecutive image numbers starting from 0.

        img_dir and img_base must either be both None or both strings.
        """

        self.island_map_graph = Map_Island(island_geo, init_pop)
        self.island_map_graph.create_map_dict() # koordinatene i kart får tilhørende lister med dyr

        self.num_years_simulated = 0


    def set_animal_parameters(self, species, p):
        """
        Set parameters for animal species.

        :param species: String, name of animal species
        :param p: Dict with valid parameter specification for species
        """
        # we think that we do this in the respective classes

    def set_landscape_parameters(self, landscape, params):
        """
        Set parameters for landscape type.

        :param landscape: String, code letter for landscape
        :param params: Dict with valid parameter specification for landscape
        """
        # we think that we do this in the respective classes

    def simulate(self, years):
        """
        Run simulation while visualizing the result.

        :param years: number of years to simulate
        """
        # phi_array_herb = []
        # age_array_herb = []
        # weight_array_herb = []
        # N_herb = []
        # N_carn = []
        # V year = []

        for year in range(years):
            self.island_map_graph.year_cycle()
            self.num_years_simulated += 1

        print(self.num_animals_per_species)


        # values needed after stopping:
        number_of_simulated_years = self.num_years_simulated
        total_number_of_animals = self.num_animals
        total_number_of_herbivores = self.num_animals_per_species['Herbivore']
        total_number_of_carnivores = self.num_animals_per_species['Carnivore']
        #print(number_of_simulated_years)
        #print(total_number_of_animals)
        #print(total_number_of_herbivores)
        #print(total_number_of_carnivores)
        '''
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

    def add_population(self, population):
        """
        Add a population to the island

        :param population: List of dictionaries specifying population
        """

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
        num_carnivores = 0
        num_herbivores = 0
        for cell in self.island_map_graph.map.values():
            num_carnivores += len(cell.carnivores_pop)
            num_herbivores += len(cell.herbivores_pop)
        number_of_animals = num_carnivores + num_herbivores
        return number_of_animals

    @property
    def num_animals_per_species(self):
        """Number of animals per species in island, as dictionary."""
        num_animals_per_species = {"Herbivore": 0, "Carnivore": 0}
        for cell in self.island_map_graph.map.values():
            num_animals_per_species["Herbivore"] += len(cell.herbivores_pop)
            num_animals_per_species["Carnivore"] += len(cell.carnivores_pop)
        return num_animals_per_species


    '''
    def make_movie(self): denne er fra Plesser 
        """Create MPEG4 movie from visualization images saved."""
    '''

