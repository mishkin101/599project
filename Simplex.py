import numpy as np

# TODO: Implelement natrix form of the simplex in standard form
class Simplex:


    #create all instance varibales from player stratgies/ distirbutions
    def __init__(
        self,
        players: list, 
        matrix: np.ndarray,
        coeffecients: list,
        constraints: [[int][int]], 
        optfunction: [[int][int]],
        optcoeff: np.ndarray,
        currvalues: np.ndarray,
        solutioncoeff: np.ndarray,
        basicmatrix: np.ndarray,
        nonbasicmatrix: np.ndarray, 
        basis:[int],
        gametype: str
        ):
            return
    
    def createContraints():
        return
    
    def toStandardForm():
        return
    
    def testFeasibility():
        return
    
    def getDual():
        return
    
    # TODO: call all above functions as subroutines in solve.
    def solve():
        return


