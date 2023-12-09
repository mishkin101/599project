import numpy as np
import Player

# TODO: Implelement matrix form of the simplex in standard form
class Simplex:

    #Create all instance varibales from player strategies/ Distirbutions
    def __init__(
        self,
        players: [Player], 
        matrix: np.ndarray,
        coefficients: {str: np.ndarray},
        constraints: [[int][int]], 
        optfunction: [[int][int]],
        optcoeff: np.ndarray ,
        currvalues: np.ndarray,
        solutioncoeff: np.ndarray,
        basicmatrix: np.ndarray,
        nonbasicmatrix: np.ndarray, 
        basis_pos:[int],
        gametype: str,
        probabilities: [np.ndarray]
        ):
            self.players = [players]
            self.matrix = matrix
            self.coefficients = None
            self.constraints = None
            self.optfunction = None
            self.optoeff = None
            self.solutioncoeff = None
            self.basicmatrix = None
            self.nonbsicmatrix = None
            self.basis_pos = None
            self.gametype = gametype
            self.probabilities = None
            self.probabilities = None
            return
    
    # Minimizing over pure/mixed is the same
    # Maximizing over pure/mixed is different

    # Here, we can imagine a bayesian tree where the players are summing over the branches to find the expected value 
    # for their payoff | other player played strategy x > for all other players strategies
    #For all player_x strategies:
    #   Assume player_x chooses strategy i
    #   Marginal probability: p from distirbution
    #   Expected payoff | p_x played strategy x  <= player's best strategy
    def expectationVal(self):
        transposed_matrix = np.transpose(self.matrix)
        player1_payoffs = transposed_matrix.tolist()
        player1_probabilities = np.zeros(self.matrix.shape[0])
        self.probabilities.append(player1_probabilities)
        return 

    def get_pure_basis(self, n, pos):
        vector = np.zeros(n)
        vector[pos] = 1
        return vector
        
    def createContraints(self, ):


        return
    
    def toStandardForm():
        return
    
    #Todo:
    def testFeasibility():
        return
    
    def getDual():
        return
    
    # TODO: call all above functions as subroutines in solve.
    def solve(self):
        #transpose the a matrix
        mat = self.matrix.transpose()

        self.matrix

        return
    # set the Tablue Matrix to be the dual matrix form of MaxMin
    def maxmin_to_Dual(self):
        #constant to add to matrix
        k = np.random.randint(3,6)
        #---Setting Simplex Constraints---#
        #variables to optimize
        arr = np.zeros(self.matrix.shape[0])
        arr[0] = 1
        self.coefficients["expectation_player_1"] = arr
        #Minimize x such that x_i = prob_i_player_1/expectation_player_1
        self.coefficients["x"] = np.ones(self.matrix.shape[0])
        self.coefficients["probabilities"] = np.ones(self.matrix.shape[0])
        #Constraints
        #Assume positve bound on exp. player 1
        self.constraints["probabilities"] = (1, 1)
        self.constraints["x"] = (0, -1)
        #add optimization variables and constraints
        #prob_p1 * a_all_col >= v (the lowest bound on expectation_val_p1)
        self.basicmatrix = np.transpose(self.matrix)
        #add a constant to the matrix to ensure positivity
        k = 3
        #add constraint for v: 
        self.constraints[]

         
         return

