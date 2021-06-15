# -*- encoding: utf-8 -*-

"""
"""

__author__ = 'Christianie Torres'
__email__ = 'christianie.torres@nmbu.no'

from biosim.Cell import Cell, Lowland, Highland, Desert, Water
from biosim.Animals import Herbivore, Carnivore
import textwrap
import random


class Map_Island:
    def __init__(self, island_geo, init_pop):
        """
        Initialize map class with given island geography and initial population
        of the various cells.
        :param island_geo: Specifies island geography
        :type island_geo: multiline str
        :param init_pop: Specifies initial population of each cell
        :type init_pop: list of dicts
        """
        random.seed()
        self.geography = {}
        self.population = {}
        self.map = {}
        self.geo = textwrap.dedent(island_geo)
        self.init_pop = init_pop

    def check_island_boundaries(self):
        """
        This is a function that raises an error if the boundary cells are not water.
        """
        self.lines_map = []
        for line in self.geo.splitlines():
            self.lines_map.append(line)

        for self.line_nr in range(len(self.lines_map)):
            if self.line_nr == 0:
                for cell_type in self.lines_map[self.line_nr]:
                    if cell_type != "W":
                        raise ValueError("Map boundary has to be only 'W'")
                    # else:
                    #   return True
            elif self.line_nr == (len(self.lines_map) - 1):
                for cell_type in self.lines_map[self.line_nr]:
                    if cell_type != "W":
                        raise ValueError("Map boundary has to be only 'W'")
                    # else:
                    #    return True
            else:
                if self.lines_map[self.line_nr][0] != "W":
                    raise ValueError("Map boundary has to be only 'W'")
                elif self.lines_map[self.line_nr][-1] != "W":
                    raise ValueError("Map boundary has to be only 'W'")
                # else:
                # return True

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
        else:
            return True

    def create_geography_dict(self):
        """
        Converts geography string to a dictionary with coordinates as keys and
        the landscape types as values. Coordinates are a tuple of x and y
        coordinates.
        """
        self.check_island_boundaries()
        self.check_for_equal_map_lines()
        # self.letter_count = 0
        self.geo.splitlines()

        self.y_coord = 1
        for line in self.geo.splitlines():
            self.x_coord = 1
            for cell_type in list(line):
                self.geography[(self.x_coord, self.y_coord)] = cell_type
                if len(list(line)) > self.x_coord:
                    self.x_coord += 1
                    # self.letter_count += 1
            if len(self.geo.splitlines()) > self.y_coord:
                self.y_coord += 1

    def create_population_dict(self):
        """
        Converts list of populations to a population dictionary that has coordinates as keys
        and lists of the properties of the animals at this location as values.
        """
        for pop_info in self.init_pop:
            if pop_info["loc"] in self.population.keys():
                self.population[pop_info["loc"]].extend(pop_info["pop"])
            else:
                self.population[pop_info["loc"]] = pop_info["pop"]

    def add_population(self, population):
        """
        Creates a dictionary with the new population.

        Next the dictionary is added to the map dictionary

        :param population: Specifies the new population of one or more cells
        :type population: list of dicts
        """
        self.new_population = {}
        for self.pop_info in population:
            self.new_population[self.pop_info["loc"]] = self.pop_info["pop"]

        for self.location, self.population1 in self.new_population.items():
            for self.animal_info in self.population1:
                if self.animal_info["species"] == "Carnivore":
                    self.map[self.location].carnivores_pop.append(Carnivore(self.animal_info))
                else:
                    self.map[self.location].herbivores_pop.append(Herbivore(self.animal_info))

    def create_map_dict(self):
        """
        Iterates through geography dictionary and creates a new dictionary of
        the entire map. This dict has coordinates as keys and
        instances of landscape classes as values. Each landscape instance has
        the population list of it's coordinate as input.
        :raise ValueError: if invalid landscape type is given in geography string
        """
        self.create_geography_dict()
        self.create_population_dict()

        for location, cell_type in self.geography.items():
            if cell_type == "L":
                if location in self.population.keys():
                    self.map[location] = Lowland(self.population[location])
                else:
                    self.map[location] = Lowland([])
            elif cell_type == "H":
                if location in self.population.keys():
                    self.map[location] = Highland(self.population[location])
                else:
                    self.map[location] = Highland([])
            elif cell_type == "D":
                if location in self.population.keys():
                    self.map[location] = Desert(self.population[location])
                else:
                    self.map[location] = Desert([])
            elif cell_type == "W":
                self.map[location] = Water([])
            else:
                raise ValueError(f"Invalid landscape type {cell_type}")

    def neighbours_of_current_cell(self, current_coordinates):
        """
        Finds all neighbouring coordinates of a given cell. Checks the landscape type of each
        coordinate. The neighbour switch landscape types an animal can move to, are returned.
        :param current_coordinates: Location of current cell
        :type current_coordinates: tuple
        :return: list of neighbour cells
        :rtype: list
        """
        # neighbours_of_current_cell = {}
        (x, y) = current_coordinates
        neighbours = [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]
        self.neighbour_cells = []
        for neighbour_cell in neighbours:
            if neighbour_cell in self.map.keys():
                self.neighbour_cells.append(self.map[neighbour_cell])
        '''
        for cell in self.neighbour_cells:
            d = random.choice(list)
            if cell.Habitable() == True:
                cell.herbivores_pop.extend(d)
                list.remove(d)
            else:
                return 
        '''
        # return self.neighbour_cells

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

        # FEEDING
        for cell in self.map.values():
            cell.make_herbivores_eat()

        for cell in self.map.values():
            cell.feed_carnivores()

        # PROCREATION
        for cell in self.map.values():
            cell.newborn_animals()

        # MIGRATION
        for loc, cell in self.map.items():
            self.neighbours_of_current_cell(loc)
            cell.move_animals_from_cell()
            for herb in cell.herbs_move:
                nr = random.choice([0, 1, 2, 3])
                # self.neighbour_cells[nr].move_to_cell_herb(herb)
                if self.neighbour_cells[nr].Habitable():
                    self.neighbour_cells[nr].herbivores_pop.append(herb)
                    cell.herbivores_pop.remove(herb)
            for carn in cell.carns_move:
                nr = random.choice([0, 1, 2, 3])

                # self.neighbour_cells[nr].move_to_cell_carn(carn)
                if self.neighbour_cells[nr].Habitable():
                    self.neighbour_cells[nr].carnivores_pop.append(carn)
                    cell.carnivores_pop.remove(carn)

            cell.reset_already_moved()

        # AGING
        for cell in self.map.values():
            cell.make_animals_age()

        # LOSE WEIGHT
        for cell in self.map.values():
            cell.make_animals_lose_weight()

        # DEAD
        for cell in self.map.values():
            cell.dead_animals_natural_cause()
