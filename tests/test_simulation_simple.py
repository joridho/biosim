import unittest
from biosim.Simulation import BioSim
from biosim.Cell import Lowland
from biosim.Animals import Herbivore, Carnivore

'''
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)
'''

if __name__ == '__main__':
    unittest.main()

def test_init_pop():
    'Check if add_pop works'
    b = biosim(init_pop=None)
    b.add_pop()
    assert len(b.init_pop) == 50

#def test_year_cycle():
 #   'Check if add_pop works in test_year_cycle'
  #  b = biosim(init_pop=None)
   # assert len(b.year_cycle()) == 50
    #assert len(l.nyliste) == 50
   #assert len(b.eat) == 50


def test_fodder_in_cell_after_fodder_eaten():
    '''Check if make_herbivores eat works in year_cycle
    by checking if fodder in cell has the right amount'''
    b = biosim(init_pop=None)
    b.add_pop()
    b.year_cycle()
    af2 = b.available_fodder
    assert af2 == 800 - 50 * 10

def test_weight_gain_after_fodder_eaten():
    b = biosim(init_pop=None)
    b.add_pop()
    init_w = [k.weight for k in b.init_pop]
    calculated_new_weight = [k + 9 for k in init_w]

    b.year_cycle()
    new_weight_by_function = b.weight_year_cycle
    #new_weight_by_function2 = [k.weight for k in b.population_herb]  # hvorfor fungerer ikke den?
    calculated_new_weight.sort()
    new_weight_by_function.sort()
    #assert new_weight_by_function == new_weight_by_function2

    assert new_weight_by_function == calculated_new_weight

def test_change_of_appetite():
    l = Lowland()
    l.herbivores_pop = [Herbivore(weight=35, a=3), Herbivore(weight=41, a=8),
                        Herbivore(weight=20, a=6), Herbivore(weight=35, a=3),
                        Herbivore(weight=41, a=8), Herbivore(weight=20, a=6)]
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
















