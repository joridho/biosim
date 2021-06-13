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


def test_neighbours_of_current_cells1():
    """

    """
    assert 1 == 1



def test_year_cycle_change_weight():
    """
    During a year the weight of the animals should change
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
    m.year_cycle()
    for k in m.map[(2, 2)].herbivores_pop:
        assert k.weight != 20

def test_fodder_in_cell_after_fodder_eaten():
    '''
    Check if make_herbivores eat works in year_cycle by checking if fodder in cell has the right
    amount. During the first year there should be enough fodder for all 50 animals
    '''
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
    assert m.map[(2, 2)].af == 800 - len(m.map[(2, 2)].herbivores_pop) * Herbivore.p['F']

def test_year_cycle_weight_change(mocker):
    '''
    During year_cycle they eat and gain weight, but later they lose weight again. In the first year
    thay gain F * beta, and later lose current weight * eta
    Since they all initially weigh 20, there will be no procreation, and therefor that will not
    affect the weight
    '''
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
    current_weight = []
    for k in m.map[(2, 2)].herbivores_pop:
        after_eating = Herbivore.p['beta'] * Herbivore.p['F']
        weight_loss = (k.weight + after_eating) * Herbivore.p['eta']
        current_weight.append(k.weight + after_eating - weight_loss)
    m.year_cycle()
    for k in range(len(m.map[(2, 2)].herbivores_pop)):
        assert m.map[(2, 2)].herbivores_pop[k].weight == current_weight[k]


def test_year_cycle_eating_carnivores():
    """

    """
    geogr = """\
                WWW
                WLW
                WWW"""

    ini_herbs = [{'loc': (2, 2),
                  'pop': [{'species': 'Herbivore',
                           'age': 5,
                           'weight': 20}
                          for _ in range(50)]}]
    ini_carns = [{'loc': (2, 2),
                  'pop': [{'species': 'Carnivore',
                           'age': 5,
                           'weight': 20}
                          for _ in range(20)]}]











def test_year_cycle_newborn_animals(mocker):
    """
    Checking the length of the initial population and comparing it to the length of the new
    population  after year_cycle. When there are this many animals the probability for birth is 1.
    The probability for death however is a lot smaller. Therefore the mocker gives a random value of
    1, so that no one will die, and the length of the list should be twice as long as the original
    """
    mocker.patch('random.random', return_value=1)
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
    assert len(m.map[(2, 2)].herbivores_pop) == init_amount * 2


def test_mother_weight_loss(mocker):
    """
    To test if the mother loses weight we have to check that the weight is less than
    initial_weight + weight gain after eating - yearly weight loss
    """
    mocker.patch('random.random', return_value=1)
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
    init_length = len(m.map[(2, 2)].herbivores_pop)
    current_weight = []
    for k in m.map[(2, 2)].herbivores_pop:
        after_eating = Herbivore.p['beta'] * Herbivore.p['F']
        weight_loss = (k.weight + after_eating) * Herbivore.p['eta']
        current_weight.append(k.weight + after_eating - weight_loss)
    m.year_cycle()
    for k in range(init_length):
        assert m.map[(2, 2)].herbivores_pop[k].weight < current_weight[k]


def test_age():
    """
    Will the animals age in accordance with the year?
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
    m.year_cycle()
    for k in m.map[(2, 2)].herbivores_pop:
        assert k.age == 6

def test_remove_dead_animals(mocker):
    """
    Will the dead animals be removed from the list. To test this we set a low random value, so that
    there will definitely be dead animals
    """
    mocker.patch('random.random', return_value=0.01)
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
    init_length = len(m.map[(2, 2)].herbivores_pop)
    m.year_cycle()
    assert len(m.map[(2, 2)].herbivores_pop) < init_length












