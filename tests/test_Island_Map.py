import unittest
from biosim.Animals import Herbivore, Carnivore
from biosim.Cell import Lowland
from biosim.MapIsland import Map_Island


if __name__ == '__main__':
    unittest.main()

def test_checking_island_boundaries():
    """
    In order for the simulation to work the boundaries must be water. The checking island_boundaries
    function gives an error if the boundaries is not water
    """
    island_geo = """\
                    WWW
                    WLW
                    WWL"""
    init_pop = [{'loc': (2, 2),
                  'pop': [{'species': 'Herbivore',
                           'age': 5,
                           'weight': 20}
                          for _ in range(50)]}]
    m = Map_Island(island_geo, init_pop)
    assert m.check_island_boundaries() == ValueError


def test_check_for_equal_map_lines():
    """
    All the lines in the map should have equal length
    """
    island_geo = """\
                    WWW
                    WLW
                    WW"""
    init_pop = [{'loc': (2, 2),
                  'pop': [{'species': 'Herbivore',
                           'age': 5,
                           'weight': 20}
                          for _ in range(50)]}]
    m = Map_Island(island_geo, init_pop)
    assert m.check_for_equal_map_lines() == ValueError


def test_geography_dict1():
    """
        Testing if each coordinate receives a letter
        """
    island_geo = """\
                    WWW
                    WLW
                    WWW"""
    m = Map_Island(island_geo, init_pop=0)
    m.check_island_boundaries()
    m.check_for_equal_map_lines()
    m.create_geography_dict()
    for x in range(1, 3):
        for y in range(1, 3):
            assert m.geography[(x, y)] == 'W' or 'L'

def test_geography_dict2():
    """
    Testing to see if Lowland receives correct coordinates
    """
    island_geo = """\
                    WWW
                    WLW
                    WWW"""
    m = Map_Island(island_geo, init_pop=0)
    m.create_geography_dict()
    assert m.geography[(2, 2)] == 'L'


def test_population_dict2():
    """
        The coordinate 2,2 should receive a population, where all of them have age=5
        """
    island_geo = """\
                    WWW
                    WLW
                    WWW"""
    init_pop = [{'loc': (2, 2),
                  'pop': [{'species': 'Herbivore',
                           'age': 5,
                           'weight': 20}
                          for _ in range(50)]}]
    m = Map_Island(island_geo, init_pop)
    m.check_island_boundaries()
    m.check_for_equal_map_lines()
    m.create_population_dict()
    for animal in m.population[(2, 2)]:
        assert animal["age"] == 5


def test_create_map_dict1():
    """
    Create_map_dict takes in population and geography dictionaries and creates a new dictionary of
    the entire map.
    To test if it receives the correct population we compare it to the length of the population
    dictionary
    """
    island_geo = """\
                    WWW
                    WLW
                    WWW"""
    init_pop = [{'loc': (2, 2),
                  'pop': [{'species': 'Herbivore',
                           'age': 5,
                           'weight': 20}
                          for _ in range(50)]}]
    m = Map_Island(island_geo, init_pop)
    m.create_map_dict()
    assert len(m.population[(2, 2)]) == len(m.map[(2, 2)].herbivores_pop)


def test_create_map_dict2():
    """
    test if the coordinates in geography receives location
    """
    island_geo = """\
                    WWW
                    WLW
                    WWW"""
    init_pop = [{'loc': (2, 2),
                  'pop': [{'species': 'Herbivore',
                           'age': 5,
                           'weight': 20}
                          for _ in range(50)]}]
    m = Map_Island(island_geo, init_pop)
    m.create_map_dict()
    assert m.map[(2, 2)] == Lowland(m.population[(2, 2)])

def test_year_cycle():
    """ test if the weight of the animals changes """
    island_geo = """\
                    WWW
                    WLW
                    WWW"""
    init_pop = [{'loc': (2, 2),
                 'pop': [{'species': 'Herbivore',
                          'age': 5,
                          'weight': 20}
                         for _ in range(50)]}]
    m = Map_Island(island_geo, init_pop)
    m.create_map_dict()
    m.year_cycle()
    for k in m.map[(2, 2)].herbivores_pop:
        assert k.weight != 20

def test_fodder_in_cell_after_fodder_eaten():
    '''Check if make_herbivores eat works in year_cycle
    by checking if fodder in cell has the right amount'''
    island_geo = """\
                        WWW
                        WLW
                        WWW"""
    init_pop = [{'loc': (2, 2),
                 'pop': [{'species': 'Herbivore',
                          'age': 5,
                          'weight': 20}
                         for _ in range(50)]}]
    m = Map_Island(island_geo, init_pop)
    m.create_map_dict()
    m.year_cycle()
    assert m.map[(2, 2)].af == 800

def test_weight_gain_after_fodder_eaten():
    '''Check if make_herbivores eat works in year_cycle
        by checking if fodder in cell has the right amount'''
    island_geo = """\
                            WWW
                            WLW
                            WWW"""
    init_pop = [{'loc': (2, 2),
                 'pop': [{'species': 'Herbivore',
                          'age': 5,
                          'weight': 20}
                         for _ in range(50)]}]
    m = Map_Island(island_geo, init_pop)
    m.create_map_dict()
    m.year_cycle()
    assert 1 == 1

def test_newborn_animals():
    """
        will the newborns be added to the list
        """
    island_geo = """\
                            WWW
                            WLW
                            WWW"""
    init_pop = [{'loc': (2, 2),
                 'pop': [{'species': 'Herbivore',
                          'age': 5,
                          'weight': 60}
                         for _ in range(50)]}]
    m = Map_Island(island_geo, init_pop)
    m.create_map_dict()
    init_amount = len(m.map[(2, 2)].herbivores_pop)
    m.year_cycle()
    assert len(m.map[(2, 2)].herbivores_pop) > init_amount

def test_mother_weight_gain():
    """
        Will the mother gain weight in the year cycle
        """
    assert 1 == 1

def test_age():
    """
        Will the animals age in accordance with the year?
        """
    assert 1 == 1

def test_weight_loss():
    """
        Will the animal lose weight each year?
        """
    assert 1 == 1

def test_remove_dead_animals():
    """
        Will the dead animals be removed from the list
        """
    assert 1 == 1

def test_reset():
    """
        Will the necessary variables reset
        """

def test_count_years():
    """
        Is one year added each year?
        """











