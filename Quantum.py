from qiskit import *
import numpy as np

class QuantumSuboutine:
    # Implement gobbs sampling
    # Have a block endocded unitary
    # Have a payoff matrix that we query form

    # Create a hermatian matrix that diag(encoded xa^T/B)
    # Estimate A's payoff from amplitdude estimation
    # Store the elements in a tree structure


    # Assume the sample dram ( payoff strategies) norm >=B and B>=1. This ensure the 
    # Estimating a single value uj can be done via amplitude estimation, finding the maximum can be achieved
    # Using the maximum-finding algorithm by D¨urr and Hoyer [DH96] and rejection sampling can
    #be done in O(√m) steps via amplitude amplification

    '''
    Then there is a quantum circuit U˜, which is an (a+ 2)-qubit block-encoding of P(A), and which consists of d applications of U and U†,
      (and in case (i) a single application of controlled-U±1)and O((a + 1)d) other one- and two-qubit gates.'''

    def __init__(self,
        matrix :np.ndarray
    ):
        self.matrix = np.ndarray
    
    # Convert the matrix to a tree structure so that we can sample within O(log(n)) time and sample from all of a players stragies with
    # a probabilitiy that is bounded by a one-norm instead of a 2-norm. Sparsity here is important as the
    # algorithm is more likely to converge to a solution that is robust to outliers when the 1-norm. 
    # its valid to use a 1-norm since this is just dividing over a probability distributon that is classic-- we just get a different metric taht represents
    # the distace between the values
    def tree_structure(self, A_vector):
        return 

    # Use amplitdude estimation to approximate the 
    def estimate_payoff():
        return
    
    #maximum-finding algorithm
    def findMax():
        return

    #ampltidude estimation
    def rejection_Sampling():
        return
    


    def __init__():
        return

