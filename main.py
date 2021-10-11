from itertools import combinations_with_replacement
from itertools import chain
from unittest import result
import sys

class Solver:
    def __init__(self):
        self.operations_so_far = []

    def check(self, start, goal, operators=[]):
        if int(start) == int(goal):
            return True
        return False

    def add(self, first, second):
        return first + second

    def multiply(self, first, second):
        return first * second

    def divide(self, first, second):
        return first / second

    def run_functions(self, start, list_to_check):
        result = start
        for i in range(0, len(list_to_check), 2):
            op = list_to_check[i]
            operand = list_to_check[i + 1]
            if op == '+':
                result = self.add(result, operand)
            elif op == '-':
                result = self.add(result, -operand)
            elif op == '*':
                result = self.multiply(result, operand)
            elif op == '/' and operand != 0:
                result = self.divide(result, operand)
        return result
    
    def solve(self, start, goal, operators=[], max_moves=10):
        for roll in combinations_with_replacement(operators*max_moves, max_moves):
            roll = tuple(x for x in roll if x != '/0')
            list_to_check = list(chain.from_iterable((x[0], int(x[1::])) for x in roll))
            if self.check(self.run_functions(start, list_to_check), goal, roll):
                return roll
        return None
            
        
# create a main function to run the program
def main():
    solver = Solver()
    # if has args, use them as start and goal
    if len(sys.argv) > 4:
        start = int(sys.argv[1])
        goal = int(sys.argv[2])
        max_moves = int(sys.argv[3])
        operators = sys.argv[4].split(' ')
        print(operators)
    
        # run solver
        result = solver.solve(start, goal, operators, max_moves=max_moves)
        # print result
        if result is not None:
            print(result)
        else:
            print('No solution found')
    else:
        start = int(input("Enter the start: "))
        goal = int(input("Enter the goal: "))
        operators = input("Enter the operators: ")
        max_moves = int(input("Enter the max amoun of movest: "))
        print(solver.solve(start, goal, operators.split(" "), max_moves=max_moves))

# run the main function
if __name__ == "__main__":
    main()
