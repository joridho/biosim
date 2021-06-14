import unittest
import pytest
from biosim.Simulation import BioSim
from biosim.Cell import Lowland
from biosim.Animals import Herbivore, Carnivore
import textwrap

'''
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)
'''

if __name__ == '__main__':
    unittest.main()

@pytest.fixture
def eg_sim():
    geogr = """\
               WWWWWWWWWWWWWWWWWWWWW
               WHHHHHLLLLWWLLLLLLLWW
               WHHHHHLLLLWWLLLLLLLWW
               WHHHHHLLLLWWLLLLLLLWW
               WWHHLLLLLLLWWLLLLLLLW
               WWHHLLLLLLLWWLLLLLLLW
               WWWWWWWWHWWWWLLLLLLLW
               WHHHHHLLLLWWLLLLLLLWW
               WHHHHHHHHHWWLLLLLLWWW
               WHHHHHDDDDDLLLLLLLWWW
               WHHHHHDDDDDLLLLLLLWWW
               WHHHHHDDDDDLLLLLLLWWW
               WHHHHHDDDDDWWLLLLLWWW
               WHHHHDDDDDDLLLLWWWWWW
               WWHHHHDDDDDDLWWWWWWWW
               WWHHHHDDDDDLLLWWWWWWW
               WHHHHHDDDDDLLLLLLLWWW
               WHHHHDDDDDDLLLLWWWWWW
               WWHHHHDDDDDLLLWWWWWWW
               WWWHHHHLLLLLLLWWWWWWW
               WWWHHHHHHWWWWWWWWWWWW
               WWWWWWWWWWWWWWWWWWWWW"""
    geogr = textwrap.dedent(geogr)

    ini_herbs = [{'loc': (2, 7),
                  'pop': [{'species': 'Herbivore',
                           'age': 5,
                           'weight': 20}
                          for _ in range(200)]}]
    ini_carns = [{'loc': (2, 7),
                  'pop': [{'species': 'Carnivore',
                           'age': 5,
                           'weight': 20}
                          for _ in range(50)]}]
    return BioSim(geogr, ini_herbs+ini_carns, seed=100, img_dir='results',
                  img_base=f'mono_hc_{100:05d}', img_years=300)

@pytest.fixture
def eg_sim2():
    geogr = """\
                WWW
                WLW
                WWW"""
    ini_herbs = [{'loc': (2, 2),
                  'pop': [{'species': 'Herbivore',
                           'age': 5,
                           'weight': 20}
                          for _ in range(50)]}]
    return BioSim(geogr, ini_herbs, seed=100, img_dir='results', img_base=f'mono_hc_{100:05d}',
                  img_years=300)

@pytest.fixture
def eg_sim3():
    geogr = """\
                WWW
                WLW
                WWW"""
    ini_herbs = [{'loc': (2, 2),
                  'pop': [{'species': 'Herbivore',
                           'age': 5,
                           'weight': 20}
                          for _ in range(200)]}]
    ini_carns = [{'loc': (2, 2),
                  'pop': [{'species': 'Carnivore',
                           'age': 5,
                           'weight': 20}
                          for _ in range(50)]}]
    return BioSim(geogr, ini_herbs+ini_carns, seed=100, img_dir='results',
                  img_base=f'mono_hc_{100:05d}', img_years=300)

def test_ini_year(eg_sim):
    """
    Test for checking that the number of years simulated is zero when nothing has been simulated
    """
    b = eg_sim
    assert b.num_years_simulated == 0

def test_num_animals1(eg_sim3):
    """
    Testing  that the initial population is 250
    """
    b = eg_sim3
    assert b.num_animals == 250

def test_num_animals(eg_sim2):
    """
    Testing that the initial population is 50
    """
    b = eg_sim2
    assert b.num_animals == 50

def test_num_animals_per_species(eg_sim3):
    """
    Testing if number of herbivores is 200 and number of carnivores is 50
    """
    b = eg_sim3
    num_per = b.num_animals_per_species
    assert [num_per["Herbivore"], num_per["Carnivore"]] == [200, 50]

def test_add_population(eg_sim2):
    """
    Checks if a population is added
    """
    b = eg_sim2
    ini_carns = [{'loc': (2, 2),
                  'pop': [{'species': 'Carnivore',
                           'age': 5,
                           'weight': 20}
                          for _ in range(20)]}]
    b.add_population(ini_carns)
    num_per = b.num_animals_per_species
    assert [num_per["Herbivore"], num_per["Carnivore"]] == [50, 20]




















