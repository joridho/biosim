# -*- coding: utf-8 -*-

__author__ = 'Jorid Holmen'
__email__ = 'jorid.holmen@nmbu.no'

"""
Island with single lowland cell, first herbivores only
"""

__author__ = 'Hans Ekkehard Plesser, NMBU'


import textwrap
from biosim.Simulation import BioSim

geogr = """\
           WWW
           WLW
           WWW"""
#geogr = textwrap.dedent(geogr)

ini_herbs = [{'loc': (2, 2),
              'pop': [{'species': 'Herbivore',
                       'age': 5,
                       'weight': 20}
                      for _ in range(50)]}]

for seed in range(100, 103):
    sim = BioSim(island_map=geogr, ini_pop=ini_herbs, seed=seed,
                 img_dir='results', img_base=f'mono_ho_{seed:05d}', img_years=300)
    sim.simulate(301)







