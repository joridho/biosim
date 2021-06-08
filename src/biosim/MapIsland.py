# -*- encoding: utf-8 -*-

"""
"""

__author__ = 'Christianie Torres'
__email__ = 'christianie.torres@nmbu.no'

from biosim.Cell import Lowland #highland, desert
from biosim.animals import Herbivore, Carnivore
import textwrap

class Map_Island:
    def __init__(self, island_geo, init_pop): # Usikker på om init_pop skal være argument her
        """
        Initialize map class with given island geography and initial population
        of the various cells.
        :param island_geography: Specifies island geography
        :type island_geography: multiline str
        :param initial_population: Specifies initial population of each cell
        :type initial_population: list of dicts
        """
        self.geography = {}
        self.population = {}
        self.map = {}
        self.geo = island_geo
        self.init_pop = init_pop
        # l = Lowland()
        # self.herbivores_pop = l.herbivores_pop
        #self.geo = textwrap.dedent(island_geo) #føler ikke denne burde funke
        #self.ini_pop = init_pop


    #MÅ fortsatt redigeres
    def check_island_boundaries(self):
        """
        This is a function that raises an error if the boundary cells are not water.
        """
        lines_map = []
        for line in self.geo.splitlines():
            lines_map.append(line)

        for line_nr in range(len(lines_map)):
            # checks all cells in first line of geography str
            if line_nr == 0: # sjekker linje nr 0 i string
                for cell_type in lines_map[line_nr]: # iterer gjennom hver bokstav i linjenr 0 og sjekker om det er W
                    if cell_type is not "W":
                        raise ValueError("Map boundary has to be only 'W'")
            # checks left- and rightmost cell in middle lines of geography str
            elif 0 < line_nr < (len(lines_map) - 1): # sjekker fra linje nr 1 til nest siste linje nr
                if lines_map[line_nr][0] is not "W": # sjekker om de første bokstavene i linjenr er lik W
                    raise ValueError("Map boundary has to be only 'W'")
                elif lines_map[line_nr][-1] is not "W": # SJEKKER OM DE SISTE BOKSTAVENE I LINJENR ER LIK W
                    raise ValueError("Map boundary has to be only 'W'")
            # checks all cells in last line of geography str
            else:
                for cell_type in lines_map[line_nr]: # sjekker siste linje i string
                    if cell_type is not "W": # iterer gjennom hver bokstav i linjenr 0 og sjekker om det er W
                        raise ValueError("Map boundary has to be only 'W'")

    def check_for_equal_map_lines(self):
        """
        This is a function that checks that all the lines in the map's geography string have equal
        length.
        """
        lengths_of_lines = []
        for l in self.geo.splitlines():
            lengths_of_lines.append(len(l))
        if len(set(lengths_of_lines)) != 1:
            raise ValueError('Map lines are not equal')


    # Gir koordinatene i et kart ulike cell_typer (avh av self.geo = island_geo)
    def create_geography_dict(self):
        """
        Converts geography string to a dictionary with coordinates as keys and
        the landscape types as values. Coordinates are a tuple of x and y
        coordinates.
        """
        self.check_island_boundaries()
        self.check_for_equal_map_lines()

        y_coord = 1 #orginalt er det motsatt: der y koordinatet står
        for line in self.geo.splitlines():
            x_coord = 1
            for cell_type in line:
                self.geography[(x_coord, y_coord)] = cell_type
                x_coord += 1
            y_coord += 1

    # Gir koordinatene flere lister med dyreinfo. et koordinat kan få flere lister med dyr (med ulik info)
    def create_population_dict(self): #### Når skal dette bli brukt???
        """
        Converts list of populations to a population dictionary that has coordinates as keys
        and lists of the properties of the animals at this location as values.
        """

        #self.population skal til slutt være en dictionary med
        #                  posisjoner som nøkler
        #                  lister med "properties" of the animal som verdier
        for pop_info in self.init_pop: # iterer gjennom elementene (dictionaries) i lista. init_pop er en liste med dictionaries
            if pop_info["loc"] in self.population.keys(): #vi sjekker om verdien som tilhører cell_info['loc'] er en nøkkel i dictionary. Vi sjekker altså om posisjonen allerede er en nøkkel i dictionary
                self.population[pop_info["loc"]].extend(pop_info["pop"]) # I en allerede eksisterende nøkkel i population, legger vi til den tilhørende lista med properties of animal
            else:
                self.population[pop_info["loc"]] = pop_info["pop"] # vi legger til posisjonen som ny nøkkel i population dictionary
# vi legger til den tilhørende lista av properties of animal som verdi til nøkkelen

    def add_population(self, population): # population her?!!!!!!!!!!!!!!!!!!!!!!!
        """
        Adds a new population to the already existing population of the island,
        in a manner similar to create_population_dict.
        :param population: Specifies the new population of one or more cells
        :type population: list of dicts
        """
        # population består av en liste av dictionaries
        new_population = {} # ny dictionary
        for pop_info in population: # iterer gjennom hvert element (dictionary) i lista
            if pop_info['loc'] in new_population.keys():
                new_population[pop_info['loc']].extend(pop_info['pop'])
            else:
                new_population[pop_info["loc"]] = pop_info["pop"] # vi legger posisjonen til pop_info som ny nøkkel i newpopulasjon. Her vil vi legge til den tilhørende lista av properties som verdi

        for location, population in new_population.items():
            for animal_info in population: # iterer gjennom elementene (listene med animal info) i lista population
                if animal_info["species"] == "Herbivore": # Hvis dyret er herbivore, blir den ....
                    self.map[location].pop_carn.append(Herbivore(animal_info)) # lagt i maper den skrevet riktig
                else:
                    self.map[location].pop_herb.append(Carnivore(animal_info)) # skjønne de her

    def create_map_dict(self):
        """
        Iterates through geography dictionary and creates a new dictionary of
        the entire map. This dict has coordinates as keys and
        instances of landscape classes as values. Each landscape instance has
        the population list of it's coordinate as input.
        :raise ValueError: if invalid landscape type is given in geography
            string
        """
        self.create_geography_dict() # hvert koordinat har sin celletype
        self.create_population_dict() # Hvert koordinat har sine lister med dyr (med ulik info)

        for location, cell_type in self.geography.items(): #
            if cell_type is "L": #celletype blir bestemt
                if location in self.population.keys(): #sjekker om koordinatet i self.geography er et koordinat i self.population
                    self.map[location] = Lowland(self.population[location]) # Vi gir koordinatet i et kart en celletype som tar inn en populasjon (som fins i det samme koordinatet) som argument. populasjon aka en flere lister med ulike dyr med ulik info
                else:
                    self.map[location] = Lowland([])
            elif cell_type is "H":
                if location in self.population.keys():
                    self.map[location] = Highland(self.population[location])
                else:
                    self.map[location] = Highland([])
            elif cell_type is "D":
                if location in self.population.keys():
                    self.map[location] = Desert(self.population[location])
                else:
                    self.map[location] = Desert([])
            elif cell_type is "W":
                self.map[location] = Water([])
            else:
                raise ValueError(f"Invalid landscape type {cell_type}")

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

        l = Lowland()

        l.herbivores_pop = self.init_pop

        l.make_herbivores_eat()
        l.newborn_animals()
        l.make_animals_age()
        l.make_animals_lose_weight()
        l.dead_animals_natural_cause()

        return l.herbivores_pop

    def add_population(self):
        for k in range(50):
            Lowland.herbivores_pop.append(Herbivore())






