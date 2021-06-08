# -*- encoding: utf-8 -*-

"""
"""

__author__ = 'Christianie Torres'
__email__ = 'christianie.torres@nmbu.no'

from biosim.Cell import lowland #highland, water, desert
from biosim.animals import herbivore #Carnivore
import textwrap

class map_island:
    def __init__(self, island_geo, init_pop): # Usikker på om init_pop skal være argument her
        """
        Initialize map class with given island geography and initial population
        of the various cells.
        :param island_geography: Specifies island geography
        :type island_geography: multiline str
        :param initial_population: Specifies initial population of each cell
        :type initial_population: list of dicts
        """
        #self.geography = {}
        #self.population = {}
        self.map = {}
        self.geo = island_geo
        self.geog = textwrap.dedent(island_geo)
        #self.ini_pop = init_pop

        self.year = 0




#INSP fra ida. MÅ fortsatt redigeres
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

    def check_map_lines_have_equal_length(self):
        """
        Checks that all lines in the map's geography string are of equal
        length.
        :raise ValueError: if lines in map str are more than one length
        """
        line_lengths = []
        for line in self.geo.splitlines():
            line_lengths.append(len(line))

        if len(set(line_lengths)) != 1:
            raise ValueError(f"Inconsistent line length.")



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
        l.herbivores_pop = self.init_pop  # må fjernes

        l.make_herbivores_eat()
        self.population_herb = l.herbivores_pop
        self.weight_year_cycle = [k.weight for k in l.herbivores_pop]  # for testing
        self.available_fodder = l.af  # for testing

        l.newborn_animals()
        l.make_animals_age()
        l.make_animals_lose_weight()
        l.dead_animals_natural_cause()

        # reset
        # l.reset_fodder()
        # l.reset_appetite()
        l.reset_given_birth()

        self.year += 1

        return l.herbivores_pop

    def add_population(self):
        l = lowland()
        self.init_pop = l.adding_animals()

