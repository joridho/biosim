import unittest
from  biosim.Simulation import biosim
from biosim.Cell import lowland

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
    af2 = b.af_bio
    assert af2 == 800 - 50 * 10

def test_weight_gain_after_fodder_eaten():
    b = biosim(init_pop=None)
    b.add_pop()
    init_w = []
    # b pop for ikke oppdatert seg
    for k in range(len(b.init_pop)):
        init_w.append(b.init_pop[k].weight)

    b.year_cycle()
    newlist = [k for k in b.weight_year_cycle]

    assert newlist == init_w

    #for k in range(len(b.weight_year_cycle)):
        #assert newlist[k] == init_w[k] + b.init_pop[k].p['beta']*init_w[k]













