import unittest
from main import Solver


class TestMain(unittest.TestCase):
    def setUp(self):
        self.solver = Solver()

    def test_simpleAddition(self):
        self.assertEqual(self.solver.solve(0, 5, ["+2", "+3"], 2), ("+2", "+3"))

    def test_simpleAddition_startingAtOne(self):
        self.assertEqual(self.solver.solve(1, 6, ["+2", "+3"], 2), ("+2", "+3"))

    def test_simpleAddition_trickWithZero(self):
        self.assertEqual(self.solver.solve(0, 5, ["+0", "+2", "+3"], 2), ("+2", "+3"))

    def test_simpleSubtraction(self):
        self.assertEqual(self.solver.solve(0, 3, ["-1", "+4"], 2), ("-1", "+4"))

    def test_simpleAddition2(self):
        self.assertEqual(self.solver.solve(0, 2, ["+1", "+1"], 2), ("+1", "+1"))
    
    def test_simpleCannotSolve(self):
        self.assertEqual(self.solver.solve(0, 5, ["+2"], 1), None)

    def test_simpleCannotSolve_notEnoughMoves(self):
        self.assertEqual(self.solver.solve(0, 8, ["+2", "+3"], 1), None)

    def test_mediumSimpleAddition(self):
        self.assertEqual(self.solver.solve(0, 8, ["+2", "+3"], 3), ("+2", "+3", "+3"))

    def test_simpleMultiplication(self):
        self.assertEqual(self.solver.solve(0, 6, ["+2", "*3"], 2), ("+2", "*3"))

    def test_simpleMultiplication_trickWithZero(self):
        self.assertEqual(self.solver.solve(0, 6, ["*0", "+2", "*3"], 2), ("+2", "*3"))

    def test_simpleDivide(self):
        self.assertEqual(self.solver.solve(10, 2, ["/5"], 1), ("/5",))

    def test_simpleDivide_divideWithZero(self):
        self.assertEqual(self.solver.solve(10, 2, ["/0","/5"], 2), ("/5",))

    def test_simpleDivide_divideZero(self):
        self.assertEqual(self.solver.solve(1, 1, ["/1","-1"], 2), ("/1", "/1"))

    def test_needsRepition(self):
        self.assertEqual(self.solver.solve(0, 20, ["*4","+4"], 3), ('+4', '*4', '+4'))

if __name__ == '__main__':
    unittest.main()
