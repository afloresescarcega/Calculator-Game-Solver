from itertools import combinations_with_replacement

class Solver:
    def __init__(self):
        self.operations_so_far = []

    def check(self, start, goal, operators=[]):
        if int(start) == int(goal):
            return True
        return False
    
    def solve(self, start, goal, operators=[], max_moves=10):
        for roll in combinations_with_replacement(operators, max_moves):
            if self.check(sum([int(x) for x in roll]), goal, roll):
                return roll
        return None
            
        
# create a main function to run the program
def main():
    # create a solver object
    solver = Solver()

    # get the start and goal
    start = input("Enter the start: ")
    goal = input("Enter the goal: ")

    # get the operators
    operators = input("Enter the operators: ")

    # solve the problem
    solver.solve(start, goal, operators)

# run the main function
if __name__ == "__main__":
    main()
