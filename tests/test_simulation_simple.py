import unittest
from  biosim.Simulation import biosim

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

def test_init_pop():
    b = biosim()
    b.add_pop()
    assert 1 == 1











