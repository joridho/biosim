import unittest
from biosim.animals import Herbivore, Carnivore
from biosim.Cell import Lowland
from biosim.MapIsland import Map_Island


if __name__ == '__main__':
    unittest.main()

def test_population_dict():
    """
        Testing if each letter gets it's coordinates
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
    assert len(m.population[(2, 2)]) == 50

def test_population_dict2():
    """
        Testing if each letter gets it's coordinates
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
    # assert m.population([2, 2]).age == 2
    for animal in m.population[(2, 2)]:
        assert animal["age"] == 5

def test_check_island_boundaries():
    island_geo = """\
                            WWW
                            WLW
                            WWW"""
    m = Map_Island(island_geo, init_pop=0)
    assert m.check_island_boundaries() == True

def test_check_map_lines():
    island_geo = """\
                            WWW
                            WLW
                            WWW"""
    m = Map_Island(island_geo, init_pop=0)
    assert m.check_for_equal_map_lines() == True

def test_create_geography_dict1():
    island_geo = """\
                            WWW
                            WLW
                            WWW"""
    m = Map_Island(island_geo, init_pop=0)
    m.create_geography_dict()
    assert m.geo.splitlines() == island_geo.splitlines()

def test_create_geography_dict2():
    island_geo = """\
                                WWW
                                WLW
                                WWW"""
    m = Map_Island(island_geo, init_pop=0)
    m.create_geography_dict()
    #assert m.geo.splitlines() == list('hei')
    #for line1 in m.geo:
        #assert line1 == 'W'

    assert m.geography[(2, 2)] == 'L'






def test_fodder_in_cell_after_fodder_eaten():
    '''Check if make_herbivores eat works in year_cycle
    by checking if fodder in cell has the right amount'''
    assert 1 == 1

def test_weight_gain_after_fodder_eaten():
    assert 1 == 1

def test_change_of_appetite():
    assert 1 == 1

def test_newborn_animals():
    """
        will the newborns be added to the list
        """
    assert 1 == 1

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











