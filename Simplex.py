import numpy as np
from Player import Player
from Game import Game

# TODO: Implelement matrix form of the simplex in standard form
class Simplex:

    #Create all instance varibales from player strategies/ Distirbutions
    def __init__(
        self,
        players: [Player], 
        matrix: np.ndarray,
        #coeffecient_list: (value, -1/1)
        #val: the bound value
        #-1: lower bound
        #+1: upperbound
        constraints: {():()}, 
        optfunction: np.ndarray,
        solutioncoeff: np.ndarray,
        basicmatrix: np.ndarray,
        nonbasicmatrix: np.ndarray, 
        gametype: str,
        probabilities: [np.ndarray],
        coefficients: {str: np.ndarray}
        ):
            self.players = [players]
            self.matrix = matrix
            self.coefficients = {}
            self.constraints = {}
            self.optfunction = None
            self.solutioncoeff = {Player: []}
            self.basicmatrix = None
            self.nonbasicmatrix = None
            self.tableau = None
            self.gametype = gametype
            self.probabilities = None
            self.cumulativetime =0
            return
    
    #Update the strategies for players
    def update_Player_Strategies(self, dist = None):
            if dist:
                for strategies in dist:
                    strat_1 = np.zeros(self.matrix.shape[0])
                    strat_2 = np.zeros(self.matrix.shape[1])
                    strat_1[strategies[0]] = 1
                    strat_2[strategies[1]] = 1
                    self.solutioncoeff[self.players[0]].append(strat_1)
                    self.solutioncoeff[self.players[1]].append(strat_2)
                    return
            for cur_player in self.players:
                for opt_strategy in self.solutioncoeff[cur_player]:
                    cur_player.set_optimal_strategies(opt_strategy)

    # Check if there is a pure strategy solution
    # The saddlepoints of the game given by the row, column
    def checkPureStrategies(self, r, c):
        # Find the minimum value in each row and its corresponding column index
        min_row_values = np.min(self.matrix, axis=1)
        min_row_indices = np.argmin(self.matrix, axis=1)

        # Find the maximum value in each column and its corresponding row index
        max_col_values = np.max(self.matrix, axis=0)
        max_col_indices = np.argmax(self.matrix, axis=0)

        # Check if the minimum value in each row is also the maximum value in its column
        saddle_points = [(i, j) for i, (min_val, min_idx) in enumerate(zip(min_row_values, min_row_indices))
        for j, (max_val, max_idx) in enumerate(zip(max_col_values, max_col_indices))
        if min_val == max_val and min_idx == max_idx]

        self.update_Player_Strategies(saddle_points)

        return True if len(saddle_points) != 0 else None
        
    def createContraints(self, coeffecients, val, bound_type):
        self.constraints[(coeffecients)] = (val, bound_type)

    def createRHS(self):
        #add one to add a row for the optimization function
        rhs = np.ones(self.matrix.shape[0]+1)
        i= 0
        for constraint in self.constraints.keys():
            bound = self.constraints[constraint][1]
            rhs[i] = bound
            i+=1
        self.coefficients["rhs"] = rhs

    # Check for all conditions for Simplex form
    # TODO: Handle slack variables if needed later
    def toStandardForm(self):
        self.nonbasicmatrix = np.transpose(self.matrix)
        self.coefficients["x"] = np.transpose(self.matrix).tolist()
        self.createContraints()
        self.createRHS()
        self.tableau = np.transpose(self.matrix)
    
    #check the last row has negatives
    def testOptimal(self):
        return np.all(self.tableau[-1, :-1] < 0)
    
    def getIndicator(self, pivot):
        return np.argmin(np.min(self.tableau[:, -1] // pivot))
    
    def GaussianStep(self, r, c):
        pivot_element =self.tableau[r,c]
        matrix = np.full(self.tableau.shape, self.toStandardForm[r]) // pivot_element
        #zero out the pivot row
        matrix[r, :] = 0
        pivot_col = self.tableau[:,c]
        #make the column a basis column in the matrix 
        pivot_mult = np.array(pivot_col)
        matrix = matrix * pivot_mult[:, np.newaxis]
        self.tableau - matrix
        
    #Check that the values for the variables are all >=0
    def checkFeasible(self):
        return np.all(self.tableau[:, -1]) > 0

 
    # TODO: Call all above functions as subroutines in solve.
    def solve(self, dual_flag= False, strategy1 = None, strategy2 = None):
        if strategy1 and strategy2:
            return np.dot(np.transpose(strategy1), np.dot(self.matrix, strategy2))
        if self.checkPureStrategies():
            self.update_Player_Strategies()
        self.create_tableau(dual_flag)
        while self.testOptimal():
            #Get maximum pivot 
            pivot_row = np.max(self.tableau[-1, self.tableau[-1] < 0], axis=1)
            #get the indicator
            pivot_col = self.getIndicator(pivot_row)
            self.GaussianStep(pivot_row, pivot_col)

        if self.checkFeasible():
            if dual_flag:
                # Optimal mixed strategy is x_i*v, since we found 1/v
                self.solutioncoeff[self.players[0]].append(self.tableau[-1, :] // self.tableau[-1, -1])
                self.solutioncoeff[self.players[1]].append(self.tableau[:, -1] // self.tableau[-1, -1])
                self.update_Player_Strategies()
        else:
            return "This game has no minmax strategy "


    # Minimizing over pure/mixed is the same
    # Maximizing over pure/mixed is different

    # Here, we can imagine a bayesian tree where the players are summing over the branches to find the expected value 
    # for their payoff | other player played strategy x > for all other players strategies
    #For all player_x strategies:
    #   Assume player_x chooses strategy i
    #   Marginal probability: p from distirbution
    #   Expected payoff | p_x played strategy x  <= player's best strategy
    
    # Set the Tablue Matrix to be the dual matrix form of MaxMin (for player 1)
    def maxmin_to_Dual(self):
        #---Setting Simplex Constraints---#

        #Variables to optimize
        #Minimize x such that x_i = prob_i_player_1/expectation_player_1
        #prob_p1 * a_all_col >= v (the lowest bound on expectation_val_p1)
        # z=0= a1 *x1 + ... a2*xn -> -a1*x1 - ... -an *xn = 0
        self.coefficients["optimization"] = - np.ones(self.matrix.shape[0])
        self.coefficients["x"] = np.transpose(self.matrix).tolist()

        #Constraints: Set all upperbounds
        #By assumption, everything in simplex has >= 0.
        # for dual for zero-sum player game, assume the upperbound is 1
        for constraint in self.coefficients["x"]:
            self.createContraints(constraint, 1, -1)

        #Create the right-hand side:
        self.createRHS()
        # for the dual, we assume that the optimizaiton funciton is 0.
        self.coefficients["rhs"][-1] = 0

         #constant to add to matrix
        k = np.random.randint(3,6)
        self.tableau = np.transpose(self.matrix) + k 
        
    
    # Create the matrix to solve
    #TODO: Implement slack matrix logic
    def create_tableau(self, flag_dual):
        if(flag_dual):
            self.maxmin_to_Dual()
        # We have slack variables to add
        else:
            #tableua is adjusted for slack variable
            self.toStandardForm()
        #add the optimizaton coeffecients row
        self.tableau = np.vstack([self.tableau, self.coefficients["optimization"]])
        #add the right-hand side
        self.tableau =np.hstack([self.tableau,self.coefficients["rhs"]])

