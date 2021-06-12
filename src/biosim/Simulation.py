# -*- coding: utf-8 -*-

__author__ = 'Jorid Holmen'
__email__ = 'jorid.holmen@nmbu.no'

import math

from biosim.Animals import Herbivore, Carnivore
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
        random.seed(seed)

        self.island_map_graph = Map_Island(island_geo, init_pop)
        self.island_map_graph.create_map_dict()  # koordinatene i kart får tilhørende lister med dyr

        self.num_years_simulated = 0

    def set_animal_parameters(self, species, p): # skjønne denne
        """
        Set parameters for animal species.

        :param species: String, name of animal species
        :param p: Dict with valid parameter specification for species
        """

        class_names = {'Herbivores': Herbivore, 'Carnivore': Carnivore}
        for param_name in p.keys():
            if param_name in class_names[species].p:
                class_names[species].p[param_name] = p[param_name]

    def set_landscape_parameters(self, landscape, p):
        """
        Set parameters for landscape type.

        :param landscape: String, code letter for landscape
        :param p: Dict with valid parameter specification for landscape
        """
        class_names = {'L': Lowland, 'H': Highland, 'D': Desert, 'W': Water}
        for param_name in p.keys():
            if param_name in class_names[landscape].p.keys():
                class_names[landscape].p[param_name] = p[param_name]

    def simulate(self, years):
        """
        Run simulation while visualizing the result.

        :param years: number of years to simulate
        """
        phi_array_herb = []  # hvorfor kun for herb
        age_array_herb = []
        weight_array_herb = []
        N_herb = []
        N_carn = []
        N_herb_1 = 0
        N_carn_1 = 0

        phi_array_carn = []
        age_array_carn = []
        weight_array_carn = []
        N_total = [] # hvorfor brukes denne
        V_year = []

        # self.set_animal_parameters(species='Herbivore, Carnivore', p=)
        for year in range(years):

            self.island_map_graph.year_cycle()

            # creating arrays for plotting
            phi_array_herb = []
            age_array_herb = []
            weight_array_herb = []
            colors = []
            colors1 = []

            for loc, cell in self.island_map_graph.map.items():
                nr_herbs_cell = len(cell.herbivores_pop)
                nr_carns_cell = len(cell.carnivores_pop)
                colors.append(nr_herbs_cell)
                colors1.append(nr_carns_cell)
                for herb in cell.herbivores_pop:
                    phi_array_herb.append(herb.phi)
                    age_array_herb.append(herb.age)
                    weight_array_herb.append(herb.weight)
                    N_herb_1 += 1
                for carn in cell.carnivores_pop:
                    phi_array_herb.append(carn.phi)
                    age_array_herb.append(carn.age)
                    weight_array_herb.append(carn.weight)
                    N_herb_1 += 1

            N_herb.append(self.num_animals_per_species['Herbivore']) # Hvorfor kan vi bruke den metoden på den måten
            N_carn.append(self.num_animals_per_species['Carnivore'])
            N_total.append(self.num_animals)
            V_year.append(self.num_years_simulated)
            #phi_array_herb.append(total_phi)
            #age_array_herb.append(total_age)
            #weight_array_herb.append(total_weight)

            self.num_years_simulated += 1


        # values needed after stopping:
        number_of_simulated_years = self.num_years_simulated
        total_number_of_animals = self.num_animals
        total_number_of_herbivores = self.num_animals_per_species['Herbivore'] # Hvorfor kan vi bruke den metoden på den måten
        total_number_of_carnivores = self.num_animals_per_species['Carnivore']

        print('Number of animals:', total_number_of_animals)
        print(self.num_animals_per_species)
        print('Number of simulated years:', number_of_simulated_years)
        #print(\n) Hvordan få til at det blir mellomrom her





        self.fig = plt.figure()
        self.create_map()
        fig = self.fig
        #self.ax1 = fig.add_subplot(3, 3, 1)  # map
        ax2 = fig.add_subplot(3, 3, 3)  # animal count
        ax3 = fig.add_subplot(3, 3, 4)  # herbivore distribution
        ax4 = fig.add_subplot(3, 3, 6)  # carnivore distribution
        ax5 = fig.add_subplot(3, 3, 7)  # fitness
        ax6 = fig.add_subplot(3, 3, 8)  # age
        ax7 = fig.add_subplot(3, 3, 9)  # weight

        # time counter                                               # skjønne fra time counter til map
        axt = fig.add_axes([0.4, 0.8, 0.2, 0.2])  # llx, lly, w, h          
        axt.axis('off')

        '''
        template = 'Years: {:5d}'                         #er det her "years kommer inn?
        txt = axt.text(0.5, 0.5, template.format(0),
                       horizontalalignment='center',
                       verticalalignment='center',
                       transform=axt.transAxes)  # relative coordinates

        plt.pause(0.01)  # pause required to make figure visible

        input('Press ENTER to begin counting')

        for k in range(30):                           
            txt.set_text(template.format(k))
            plt.pause(0.1)  # pause required to make update visible
        
        
        # hvordan sette map her
        '''

        '''
        fig = plt.figure()
        ax1 = fig.add_subplot(3, 3, 1)  # map
        ax3 = fig.add_subplot(3, 3, 4)  # herbivore distribution
        ax4 = fig.add_subplot(3, 3, 5)  # carnivore distribution
        ax5 = fig.add_subplot(3,3, 6)   # fitness
        ax6 = fig.add_subplot(3, 3, 7)  # age
        ax7 = fig.add_subplot(3, 3, 8)  # weight
        '''
        self.create_map()
        ax2.plot(V_year, N_herb, 'b') # antall herb
        ax2.plot(V_year, N_carn, 'r') # antall carn
        ax2.legend('Animals')
        ax2.set_title('Animal count')

        listfarge = []
        for rute in colors:
            if 0 < rute < 50:
                listfarge.append([0.4, 0.0, 1.0])
            if 50 < rute < 100:
                listfarge.append([0.0, 0.6, 0.0])
            if 100 < rute < 150:
                listfarge.append([0.5, 1.0, 0.5])
            if 150 < rute < 200:
                listfarge.append([1.0, 1.0, 0.5])



        #ax3.set_xticks([1 5 10])                          # skjønne hva som skjer her, aka set_xticks()
        #ax3.set_yticks(1)
        ax3.set_title("Herbivore distribution")
        #fig.tight_layout()
        ax3.imshow(listfarge)

        #ax3.set_xticks([1 5 10])                         # skjønne hva som skjer her, aka set_xticks()
        #ax4.set_yticks(1)
        ax4.set_title("Carnivore distribution")
        #fig.tight_layout()
        ax3.imshow(listfarge)

        ax5.hist(phi_array_herb, bins= 20, label ='phi herbs', histtype ='step', edgecolor = 'b') # ordne bins,  int(math.sqrt(N_herb_1))
        ax5.hist(phi_array_carn, bins= 20,label ='phi carns', histtype ='step', edgecolor = 'r')     #int(math.sqrt(N_carn_1))
        ax5.set_title('fitness')
        handles, labels = ax5.get_legend_handles_labels()
        ax5.legend(labels = labels)


        ax6.hist(age_array_herb, bins= 20, label ='age herbs',histtype ='step', edgecolor = 'b')  # ordne bins, int(math.sqrt(N_herb_1))
        ax6.hist(age_array_carn, bins = 20, label ='age carns', histtype ='step', edgecolor = 'r') #int(math.sqrt(N_carn_1))
        ax6.set_title('age')
        handles, labels = ax6.get_legend_handles_labels()
        ax6.legend(handles = handles, labels =labels) # Kan ta med handles også, men blir d samme med og uten

        ax7.hist(weight_array_herb, bins= 20, label ='weight herbs',histtype ='step', edgecolor = 'b') #ordne bins, int(math.sqrt(N_herb_1))
        ax7.hist(weight_array_herb, bins= 20, label ='weight herbs',histtype ='step', edgecolor = 'r') #int(math.sqrt(N_carn_1))
        ax7.set_title('weight')
        handles, labels = ax7.get_legend_handles_labels()
        ax7.legend(labels = labels)
        fig.tight_layout()  # Fikk feilmld
        plt.show()



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
            for row in self.island_map_graph.geo.splitlines()] # vet ikke hv Map_Island returnere enda

        # lager tom figur
        #fig = plt.figure()

        # adder akser til tom figur (skal bli øy)
        ax_im = self.fig.add_axes([0.045, 0.65, 0.3, 0.3])  # llx, lly, w, h

        # viser øya m/vann
        ax_im.imshow(map_rgb)

        # hva gjør denne??????????????????
        ax_im.set_xticks(range(len(map_rgb[0])))
        ax_im.set_xticklabels(range(1, 1 + len(map_rgb[0])))
        ax_im.set_yticks(range(len(map_rgb)))
        ax_im.set_yticklabels(range(1, 1 + len(map_rgb)))

        # lager nytt koordinatsystem i figuren (x akse starter ved 80 % bredde (v->h) av figuren, y 
        # akse starter i 10 prosent høyde av figuren, har bredde som er på 10% av figuren, har høyde som er på 80% av figuren)
        ax_lg = self.fig.add_axes([0.35, 0.65, 0.1, 0.3])  # llx, lly, w, h
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




    def add_population(self, population):
        """
        Add a population to the island

        :param population: List of dictionaries specifying population
        """

        return self.island_map_graph.add_population(population)   # Blir brukt for å legge til carnivores

        # for k in range(50):
        # Lowland.herbivores_pop.append(Herbivore())

        # self.init_pop = l.adding_animals()
        # self.idk = len(self.init_pop)
        # return self.init_pop

   # @property
   # def year(self):
     #   """Last year simulated."""           # Denne kan egt fjernes
     #   return self.num_years_simulated

    @property
    def num_animals(self):
        """Total number of animals on island."""
        num_carnivores = 0
        num_herbivores = 0
        for cell in self.island_map_graph.map.values():         # hvorfor ikke kun den nederste
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


    #def make_movie(self): denne er fra Plesser
        #Create MPEG4 movie from visualization images saved."""

