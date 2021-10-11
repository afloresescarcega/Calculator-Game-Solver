import unittest
from main import Solver


class TestMain(unittest.TestCase):
    def setUp(self):
        self.solver = Solver()

    def test_simpleAddition(self):
        self.assertEqual(self.solver.solve(0, 5, ["2", "3"], 2), ("2", "3"))

    def test_simpleAddition2(self):
        self.assertEqual(self.solver.solve(0, 2, ["1", "1"], 2), ("1", "1"))
    
    def test_simpleCannotSolve(self):
        self.assertEqual(self.solver.solve(0, 5, ["2"], 1), None)

    def test_mediumSimpleAddition(self):
        self.assertEqual(self.solver.solve(0, 8, ["2", "3"], 3), ("2", "3", "3"))
        


if __name__ == '__main__':
    unittest.main()
