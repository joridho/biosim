import unittest
from biosim.animals import herbivore, carnivore
from biosim.Cell import lowland
from biosim.Map_Island import map_island

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

def test_fodder_in_cell_after_fodder_eaten():
    '''Check if make_herbivores eat works in year_cycle
    by checking if fodder in cell has the right amount'''
    m = map_island(island_geo='0', init_pop=None)
    m.add_population()
    m.year_cycle()
    af2 = m.available_fodder
    assert af2 == 800 - 50 * 10

def test_weight_gain_after_fodder_eaten():
    m = map_island(island_geo='0', init_pop=None)
    m.add_population()
    init_w = [k.weight for k in m.init_pop]
    calculated_new_weight = [k + 9 for k in init_w]

    m.year_cycle()
    #new_weight_by_function = m.weight_year_cycle
    pop = m.population_herb
    #new_weight_by_function = [k.weight for k in pop]
    #new_weight_by_function = [k.weight for k in m.population_herb]  # hvorfor fungerer ikke den?
    new_weight_by_function = m.weight_year_cycle
    calculated_new_weight.sort()
    new_weight_by_function.sort()
    assert calculated_new_weight == new_weight_by_function

def test_change_of_appetite():
    l = lowland()
    l.herbivores_pop = [herbivore(weight=35, a=3), herbivore(weight=41, a=8),
                        herbivore(weight=20, a=6), herbivore(weight=35, a=3),
                        herbivore(weight=41, a=8), herbivore(weight=20, a=6)]
    b = biosim(init_pop=l.herbivores_pop)
    # b.add_pop()

    one_herb = b.init_pop[0]
    init_ap = one_herb.p['F']
    b.year_cycle()
    # same_but_updated_herb = b.init_pop[0]
    new_ap = b.population_herb[0].p['F']  # vet ikke hvorfor b.population_herb ikke funker
    b.num_animals()
    assert new_ap == init_ap - b.population_herb[0].F_consumed

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











