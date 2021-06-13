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
    def __init__(self, island_geo, init_pop):  # Tror init_pop skal være argument her
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
        lines_map = []
        for line in self.geo.splitlines():
            lines_map.append(line)

        for line_nr in range(len(lines_map)):
            if line_nr == 0:
                for cell_type in lines_map[line_nr]:
                    if cell_type != "W":
                        raise ValueError("Map boundary has to be only 'W'")
                    else:
                        return True
            elif line_nr == (len(lines_map) - 1):
                for cell_type in lines_map[line_nr]:
                    if cell_type != "W":
                        raise ValueError("Map boundary has to be only 'W'")
                    else:
                        return True
            elif 0 < line_nr < (len(lines_map) - 1):
                if lines_map[line_nr][0] != "W":
                    raise ValueError("Map boundary has to be only 'W'")
                elif lines_map[line_nr][-1] != "W":
                    raise ValueError("Map boundary has to be only 'W'")
                else:
                    return True


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
        a = "some string"
        self.letter_count = len(self.geo)
        self.geo.splitlines()

        self.y_coord = 1  # orginalt er det motsatt: der y koordinatet står
        for line in self.geo.splitlines():
            self.x_coord = 1
            for cell_type in list(line):
                self.geography[(self.x_coord, self.y_coord)] = cell_type
                self.x_coord += 1
                #self.letter_count += 1
            self.y_coord += 1

        '''
            for loc, cell_type in self.geography:
                if cell_type == 'W':
                    del self.geography[loc]
        '''

    def create_population_dict(self):
        """
        Converts list of populations to a population dictionary that has coordinates as keys
        and lists of the properties of the animals at this location as values.
        """

        # self.population skal til slutt være en dictionary med
        #                  posisjoner som nøkler
        #                  lister med "properties" of the animal som verdier

        for pop_info in self.init_pop:  # iterer gjennom elementene (dictionaries) i lista. init_pop er en liste med dictionaries
            if pop_info["loc"] in self.population.keys():  # vi sjekker om verdien som tilhører cell_info['loc'] er en nøkkel i dictionary. Vi sjekker altså om posisjonen allerede er en nøkkel i dictionary
                self.population[pop_info["loc"]].extend(pop_info["pop"])  # I en allerede eksisterende nøkkel i population, legger vi til den tilhørende lista med properties of animal
            else:
                self.population[pop_info["loc"]] = pop_info["pop"]  # vi legger til posisjonen som ny nøkkel i population dictionary


    def add_population(self, population):
        """
        Adds a new population to the already existing population of the island,
        in a manner similar to create_population_dict.
        :param population: Specifies the new population of one or more cells
        :type population: list of dicts
        """

        for pop_info in population:
            if pop_info['loc'] in  self.population.keys():
                self.population[pop_info['loc']].extend(pop_info['pop'])
            else:
                self.population[pop_info["loc"]] = pop_info["pop"]
        """
        new_population = {}
        for pop_info in population:
            if pop_info['loc'] in new_population.keys():
                new_population[pop_info['loc']].extend(pop_info['pop'])
            else:
                new_population[pop_info["loc"]] = pop_info["pop"]

        for location, population in new_population.items():
            for animal_info in population:
                if animal_info["species"] == "Herbivore":
                    #self.map[location].herbivores_pop.append(Herbivore(animal_info))
                    self.population[pop_info["loc"]] = pop_info["pop"]
                else:
                    self.map[location].carnivores_pop.append(Carnivore(animal_info)) 
    """

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
                    self.map[location] = Highland([])  # Har ikke highland enda
            elif cell_type == "D":
                if location in self.population.keys():
                    self.map[location] = Desert(self.population[location])
                else:
                    self.map[location] = Desert([])
            elif cell_type == "W":
                self.map[location] = Water([])
            else:
                raise ValueError(f"Invalid landscape type {cell_type}")


    def neighbours_of_current_cell(self, current_coordinates): # Hva skal input være her?
        """
        Finds all neighbouring coordinates of a given cell. Checks the landscape type of each
        coordinate. The neighbour switch landscape types an animal can move to, are returned.
        :param current_coordinates: Location of current cell
        :type current_coordinates: tuple
        :return: Locations as keys and landscape class instance as values
        :rtype: dict
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
        self.arrived_cell = random.choice(self.neighbour_cells)
        return self.arrived_cell

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
            if self.arrived_cell.Habitable() == True:
                list_of_moving_animals = cell.move_animals_from_cell()
                self.arrived_cell.move_animals_to_cell(list_of_moving_animals)

        for loc, cell in self.map.items():
            cell.reset_already_moved()

            '''
            for herb in cell.herbs_move:
                self.neighbours_of_current_cell(loc)  # Mangler input her
                arrived_cell = random.choice(self.neighbour_cells)
                if arrived_cell.Habitable() == True:
                    # self.move = True
                    arrived_cell.herbivores_pop.append(herb)
                    cell.herbivores_pop.remove(herb)
                # else:
                #   self.move = False

            for carn in cell.carns_move:
                self.neighbours_of_current_cell(loc)  # Mangler input her
                arrived_cell = random.choice(self.neighbour_cells)
                if arrived_cell.Habitable() == True:
                    # self.move = True
                    arrived_cell.carnivores_pop.append(carn)
                    cell.carnivores_pop.remove(carn)
                # else:
                #   self.move = False
        '''


        # AGING
        for cell in self.map.values():
            cell.make_animals_age()

        # LOSE WEIGHT
        for cell in self.map.values():
            cell.make_animals_lose_weight()

        #DEAD
        for cell in self.map.values():
            cell.dead_animals_natural_cause()


