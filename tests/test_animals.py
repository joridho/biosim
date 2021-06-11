# -*- encoding: utf-8 -*-

"""
"""


__author__ = 'Christianie Torres'
__email__ = 'christianie.torres@nmbu.no'

from biosim.Animals import Animal, Herbivore, Carnivore

class test_animals:
    alpha = 0.01  # Significance level

    """
    Tests for animal class

    """
    #@pytest.fixture
    def carnivore(self):
        return Carnivore()

    #@pytest.fixture
    def herbivore(self):
        return Herbivore()

    #@pytest.fixture
    def animals(self):
        """
        create animals of different type, age and weight to use in test of fitness
        """

        animals = [Herbivore(age=0, weight=5),
                   Herbivore(age=0, weight=1000),
                   Herbivore(age=100, weight=5),
                   Herbivore(age=100, weight=1000),
                   Herbivore(age=0, weight=5),
                   Carnivore(age=0, weight=5),
                   Carnivore(age=0, weight=1000),
                   Carnivore(age=100, weight=5),
                   Carnivore(age=100, weight=1000)]
        return animals

animals = [{'species': 'Herbivore', 'age': 0, 'weight': 5},
            {'species': 'Herbivore', 'age': 0, 'weight': 1000},
            {'species': 'Herbivore', 'age': 100, 'weight': 1000},
            {'species': 'Herbivore', 'age': 100, 'weight': 5},
            {'species': 'Herbivore', 'age': 0, 'weight': 5},
            {'species': 'Herbivore', 'age': 0, 'weight': 5},
            {'species': 'Herbivore', 'age': 0, 'weight': 1000},
            {'species': 'Herbivore', 'age': 100, 'weight': 5},
            {'species': 'Herbivore', 'age': 100, 'weight': 1000}]



# Tests for initial value:
def test_parameters_herb():
    """
    Checking if the correct parameters for herbivores is given
        It is given that the w_birth is 8.0 for herbivores
    """
    h = Herbivore({'age': 5, 'weight': 20})
    assert h.p['w_birth'] == 8.0

def test_parameters_carn():
    """
    Checking if the correct parameters for carnivores is given
    It is given that the w_birth is 6.0 for carnivores
    """
    h = Carnivore({'age': 10, 'weight': 40})
    assert h.p['w_birth'] == 6.0

def test_herbivore_age():
    """
    The herbivore shall be given an age when it is created
    It is given age = 5
    """
    h = Herbivore({'age': 5, 'weight': 20})
    assert h.age == 5

def test_carnivore_age():
    """
    The herbivore shall be given an age when it is created
    It is given age = 10
    """
    c = Carnivore({'age': 10, 'weight': 40})
    assert c.age == 10

def test_herbivore_weight():
    """
    The herbivore shall be given an weight when it is created
    It is given weight = 20
    """
    h = Herbivore({'age': 5, 'weight': 20})
    assert h.weight == 20

def test_carnivore_weight():
    """
    The carnivore shall be given an weight when it is created
    It is given weight = 40
    """
    c = Carnivore({'age': 10,'weight': 40})
    assert c.weight == 40

def test_herb_given_fitness():
    """
    When a herbivore is created the fitness is automatically updated
    """
    h = Herbivore({'age': 5, 'weight': 20})
    assert h.phi != None

def test_carn_given_fitness():
    """
    When a carnivore is created the fitness is automatically updated
    """
    c = Carnivore({'age': 10, 'weight': 40})
    assert c.phi != None



# Tests for aging function
def test_herbivore_aging():
    """
    A herbivore ages each year, and there are therefore created a function for it
    The herbivore has age = 0, each year it ages and the age should be year + 1
    """
    h = Herbivore({'age': 0, 'weight': 20})
    for year in range(10):
        h.aging()
        assert h.age == year + 1

def test_carnivore_aging():
    """
    A carnivore ages each year, and there are therefore created a function for it
    The carnivore has age = 0, each year it ages and the age should be year + 1
    """
    c = Carnivore({'age': 0, 'weight': 20})
    for year in range(10):
        c.aging()
        assert c.age == year + 1

def test_update_fitness_when_aging_herb():
    """
    When a herbivore ages the fitness changes, since age is used to calculate fitness
    First the initial fitness is saved in init_phi, and compared with the new fitness after aging
    The initial fitness should ble slightly greater than the new fitness
    """
    h = Herbivore({'age': 5, 'weight': 35})
    init_phi = h.phi
    h.aging()
    assert h.phi < init_phi

def test_update_fitness_when_aging_carn():
    """
    When a carnivore ages the fitness changes, since age is used to calculate fitness
    First the initial fitness is saved in init_phi, and compared with the new fitness after aging
    The initial fitness should ble slightly greater than the new fitness
    """
    c = Carnivore({'age': 10, 'weight': 40})
    init_phi = c.phi
    c.aging()
    assert c.phi < init_phi



# Tests for birth_weight_function:
def test_birth_weight_function_herb():
    """
    When a new herbivore is born it needs to be given a weight
    The newborns weight is calculated with the birth_weight_function function
    To use this function the newborn has to be given a mother, which is h
    """
    h = Herbivore({'age': 5, 'weight': 20})
    newborn = Herbivore({'age': 0, 'weight': h.birth_weight_function()})
    assert newborn.weight != None

def test_birth_weight_function_carn():
    """
    When a new carnivore is born it needs to be given a weight
    The newborns weight is calculated with the birth_weight_function function
    To use this function the newborn has to be given a mother, which is c
    """
    c = Carnivore({'age': 10, 'weight': 40})
    newborn = Herbivore({'age': 0, 'weight': c.birth_weight_function()})
    assert newborn.weight != None



# Tests for weight_loss function:
def test_herbivore_weight_loss():
    '''
    The herbivore loses weight each year.
    The weight loss is equivalent to the initial weight times eta = 0.05
    '''
    h = Herbivore({'age': 5, 'weight': 20})
    initial_weight = h.weight
    eta = h.p['eta']
    h.weight_loss()
    assert h.weight == initial_weight - initial_weight * eta

def test_carnivore_weight_loss():
    '''
    The carnivore loses weight each year.
    The weight loss is equivalent to the initial weight times eta = 0.125
    '''
    c = Carnivore({'age': 10, 'weight': 40})
    initial_weight = c.weight
    eta = c.p['eta']
    c.weight_loss()
    assert c.weight == initial_weight - initial_weight * eta

def test_update_fitness_during_weight_loss_herb():
    """
    When the herbivore loses weight the fitness must be updates.
    It is updated in the weight_loss function.
    The initial fitness should be greater than the new fitness.
    """
    h = Herbivore({'age': 5, 'weight': 20})
    init_phi = h.phi
    h.weight_loss()
    assert h.phi < init_phi

def test_update_fitness_during_weight_loss_carn():
    """
    When the carnivore loses weight the fitness must be updates.
    It is updated in the weight_loss function.
    The initial fitness should be greater than the new fitness.
    """
    c = Carnivore({'age': 10, 'weight': 40})
    init_phi = c.phi
    c.weight_loss()
    assert c.phi < init_phi



# Tests for weight_gain function:
def test_weight_gain_herb():
    """
    When the herbivore eats it gains weight.
    Before it eats we save the initial weight in init_weight.
    We use the weight_gain function to calculate the new weight, where the input is the amount
    it eats. For convenience the amount it eats is the same as the appetite.
    """
    h = Herbivore({'age': 5, 'weight': 20})
    init_weight = h.weight
    beta = h.p['beta']
    F = h.p['F']
    new_weight = init_weight + beta * F  # for comparing with the weight given in the function
    h.weight_gain(consumption=F)
    assert h.weight == new_weight

def test_weight_gain_carn():
    """
    When the carnivore eats it gains weight.
    Before it eats we save the initial weight in init_weight.
    We use the weight_gain function to calculate the new weight, where the input is the amount
    it eats. For convenience the amount it eats is the same as the appetite.
    """
    c = Carnivore({'age': 10, 'weight': 40})
    init_weight = c.weight
    beta = c.p['beta']
    F = c.p['F']
    new_weight = init_weight + beta * F  # for comparing with the weight given in the function
    c.weight_gain(consumption=F)
    assert c.weight == new_weight

def test_updated_fitness_during_weight_gain_herb():
    """
    When the herbivore gains weight the fitness must be updates.
    It is updated in the weight_gain function.
    The initial fitness should be lower than the new fitness.
    """
    h = Herbivore({'age': 5, 'weight': 20})
    init_phi = h.phi
    h.weight_gain(consumption=h.p['F'])
    assert h.phi > init_phi

def test_updated_fitness_during_weight_gain_carn():
    """
    When the carnivore gains weight the fitness must be updates.
    It is updated in the weight_gain function.
    The initial fitness should be lower than the new fitness.
    """
    c = Carnivore({'age': 10, 'weight': 40})
    init_phi = c.phi
    c.weight_gain(consumption=c.p['F'])
    assert c.phi > init_phi


# Tests for fitness function:
def test_valid_fitness_carn():
    """
    The phi-value should be between 0 and zero.
    To test this we calculate the fitness for several herbivores
    """
    for age in range(0, 50):
        for weight in range(10,60):
            h = Herbivore({'age': age, 'weight': weight})
            assert 0 <= h.phi <= 1

def test_valid_fitness_carn():
    """
    The phi-value should be between 0 and zero.
    To test this we calculate the fitness for several carnivores
    """
    for age in range(0, 50):
        for weight in range(10,60):
            c = Carnivore({'age': age, 'weight': weight})
            assert 0 <= c.phi <= 1

def test_fitness_when_weight_is_zero():
    """
    When the weight = 0, the fitness should be zero
    """
    h = Herbivore({'age': 5, 'weight': 0})
    assert h.phi == 0



# Tests for birth_probability function:
def test_no_newborn_when_mother_weighs_too_little_herb():
    """
    If the mother weighs less than zeta * (w_birth + sigma_birth) the birth will not take place
    For herbivores: zeta * (w_birth * sigma_birth) = 3.5 * (8 - 1.5) = 22.75
    For the test we use weight = 20, since 20 < 22.75
    The input in birth_probability is how many herbivores in the cell.
    """
    h = Herbivore({'age': 5, 'weight': 20})
    assert h.birth_probability(n=3) == 0

def test_no_newborn_when_mother_weighs_too_little_carn():
    """
    If the mother weighs less than zeta * (w_birth + sigma_birth) the birth will not take place
    For carnivores: zeta * (w_birth * sigma_birth) = 3.5 * (6 - 1) = 17.5
    For the test we use weight = 15, since 15 < 17.5
    The input in birth_probability is how many carnivores in the cell.
    """
    c = Carnivore({'age': 10, 'weight': 15})
    assert c.birth_probability(n=3) == 0

def test_no_newborn_when_to_few_animals(): #too
    """
    This is a test that checks if the birth probability equals zero when there are too few animals
    a cell.
    """

    h = Herbivore({'species': 'Herbivore',
                       'age': 3,
                       'weight': 35})                      #weight=35, age=3
    assert h.birth_probability(n=1) == 0

def test_no_newborn_if_newborn_too_fat():
    """
    This is a test that checks if the birth probability equals zero when the newborn weighs more
    than the mother
    """
    # the newborn will weigh more than 15/3.5
    h = Herbivore({'species': 'Herbivore',
                       'age': 3,
                       'weight': 15})                          #weight=15, age=3
    assert h.birth_probability(n=3) == 0

def test_birth():
    'This is a test that checks if the Herbivore gives birth when it is supposed to'
    h = Herbivore({'species': 'Herbivore',
                       'age': 5,
                       'weight': 35})    #weight=35, age=3
    true = 0
    false = 0
    for _ in range(100):
        h.birth_probability(n=4)
        h.will_the_animal_give_birth(n=4)
        if h.birth == True:
            true += 1
        else:
            false +=1
    assert true == false  # bare en test for å sjekke hva som ikke fungerer

def test_herbivore_birth_weight_loss():
    ' This is a test that checks if the Mother looses the right amount of weight after giving birth'
    h = Herbivore({'species': 'Herbivore',
                       'age': 3,
                       'weight': 15})   #Bare å endre alder og vekt hvis du føler for det
    current_weight = h.weight
    h.birth_weight_loss(newborn_birth_weight=8)
    assert h.weight == current_weight - h.p['zeta'] * 8


def test_death():
    '''
    This is a test that checks if the Herbivore dies when it is supposed to'
    '''
    h = Herbivore({'species': 'Herbivore',
                       'age': 3,
                       'weight': 10})
    for _ in range(100):
        h.death_probability()
        if h.will_the_animal_die() == True:
            assert h.d < h.p
        else:
            assert h.d >= h.p

def test_consumption():
    h = Herbivore(properties={'species': 'Herbivore', 'weight': 35, 'age': 5})
    h.eat_fodder(F_cell=800)
    assert h.F_consumption == 10#h.p['F']

def  test_consumption_not_enough_fodder():
    h = Herbivore(properties={'species': 'Herbivore', 'weight': 35, 'age': 5})
    h.eat_fodder(F_cell=7)
    assert h.F_consumption == h.F_consumption

def test_herbivore_eat_fodder():
    h = Herbivore(properties={'species': 'Herbivore', 'weight': 35, 'age': 5})
    current_weight = h.weight
    h.eat_fodder(F_cell = h.p['F']) 
    assert h.weight == current_weight + h.p['beta'] * h.F_consumption

def test_herbivore_gains_weight_after_eat_fodder():
    h = Herbivore(properties={'species': 'Herbivore', 'weight': 35, 'age': 5})
    current_weight = h.weight
    h.eat_fodder(F_cell = 6)
    assert h.weight == current_weight + h.p['beta'] * h.F_consumption

def test_weight_gain_after_eating():
    h = Herbivore(properties={'species': 'Herbivore', 'weight': 35, 'age': 5})
    h.eat_fodder(F_cell = 800)
    assert h.weight == 35 + h.p['beta'] * h.F_consumption


def test_if_carnivore_gains_correct_weight():
    carn = Carnivore({'species': 'Herbivore',
                       'age': 3,
                       'weight': 15})
    w = carn.weight
    herb = Herbivore({'species': 'Herbivore',
                       'age': 3,
                       'weight': 15})
    carn.weight_gain_after_eating_herb(herb)
    assert carn.weight == w + herb.weight * carn.p['beta']

def test_carnivore_updated_fitness():
    carn = Carnivore({'species': 'Carnivore',
                       'age': 5,
                       'weight': 70})
    f1 = carn.phi
    herb = Herbivore({'species': 'Herbivore',
                       'age': 2,
                       'weight': 35})
    carn.weight_gain_after_eating_herb(herb)
    assert f1 != carn.phi

def test_prob_kill():
    herb = Herbivore({'species': 'Herbivore',
                       'age': 3,
                       'weight': 15})
    carn = Carnivore({'species': 'Carnivore',
                       'age': 3,
                       'weight': 15})
    for _ in range(100):
        if carn.probability_kill_herbivore(herb) == True:
        #if carn.prob_kill == True:
            assert carn.r < carn.prob_kill
        else:
            assert carn.r >= carn.prob_kill

def test_prob_kill_not_work1():
    herb = Herbivore({'species': 'Herbivore',
                       'age': 3,
                       'weight': 35})
    carn = Carnivore({'species': 'Carnivore',
                       'age': 1,
                       'weight': 8})
    # have calculated that the herbivore has greater fitness than the carnivore
    carn.probability_kill_herbivore(herb)
    assert carn.prob_kill == 0

def test_prob_kill_not_work2():
    herb = Herbivore({'species': 'Herbivore',
                       'age': 3,
                       'weight': 35})
    carn = Carnivore({'species': 'Carnivore',
                       'age': 4,
                       'weight': 60})
    carn.probability_kill_herbivore(herb)
    assert carn.prob_kill == (carn.phi - herb.phi) / carn.p['DeltaPhiMax']

def test_to_much_fitness():
    h = Herbivore(properties={'species': 'Carnivore', 'weight': 29, 'age': 5})
    assert h.phi == 0.8698915249774015
