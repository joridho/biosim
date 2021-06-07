# -*- encoding: utf-8 -*-

"""
"""

__author__ = 'Christianie Torres'
__email__ = 'christianie.torres@nmbu.no'

from biosim.Cell import lowland #highland, water, desert
from biosim.animals import herbivore #Carnivore
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
        #self.geography = {}
        #self.population = {}
        self.map = {}
        self.geo = island_geo
        self.geog = textwrap.dedent(island_geo)
        #self.ini_pop = init_pop

        def check_boundaries_are_ocean(self):
            """
            Checks that all boundary cells for the map are Ocean.
            :raise ValueError: if a boundary cell is other landscape type than
                Ocean
            """
            map_lines = []
            for line in self.geo.splitlines():
                map_lines.append(line)

            for line_num in range(len(map_lines)):
                # checks all cells in first line of geography str
                if line_num == 0:
                    for landscape_type in map_lines[line_num]:
                        if landscape_type is not "O":
                            raise ValueError("Map boundary has to be only 'O'")
                # checks left- and rightmost cell in middle lines of geography str
                elif 0 < line_num < (len(map_lines) - 1):
                    if map_lines[line_num][0] is not "O":
                        raise ValueError("Map boundary has to be only 'O'")
                    elif map_lines[line_num][-1] is not "O":
                        raise ValueError("Map boundary has to be only 'O'")
                # checks all cells in last line of geography str
                else:
                    for landscape_type in map_lines[line_num]:
                        if landscape_type is not "O":
                            raise ValueError("Map boundary has to be only 'O'")

        def check_map_lines_have_equal_length(self):
            """
            Checks that all lines in the map's geography string are of equal
            length.
            :raise ValueError: if lines in map str are more than one length
            """
            line_lengths = []
            for line in self.geogr.splitlines():
                line_lengths.append(len(line))

            if len(set(line_lengths)) != 1:
                raise ValueError(f"Inconsistent line length.")
