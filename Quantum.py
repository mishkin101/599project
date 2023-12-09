from qiskit import *
import numpy as np
from qiskit import IBMQ
from numpy import arcsin, sqrt, pi
from qiskit import QuantumRegister, ClassicalRegister 
from qiskit import QuantumCircuit
from qiskit_algorithms import AmplificationProblem
import heapq
from Player import Player
from qiskit.quantum_info import Statevector
from qiskit import circuit

class QuantumSuboutine:
    #Create a hermatian matrix that diag(encoded xa^T/B)
    # Estimate A's payoff from amplitdude estimation
    # Store the elements in a tree structure


    # Assume the sample dram ( payoff strategies) norm >=B and B>=1. This ensure the 
    # Estimating a single value uj can be done via amplitude estimation, finding the maximum can be achieved
    # Using the maximum-finding algorithm by D¨urr and Hoyer [DH96] and rejection sampling can
    #be done in O(√m) steps via amplitude amplification

    def __init__(self,
        matrix :np.ndarray,
        distribution: np.ndarray,
        sparsity: int,
        players: [Player],
        dist_heap: heapq
        ):
            self.matrix = np.ndarray,
            self.distribution = distribution
            self.spaesity = int
            self.players = [Player]
            self.dist_heap = None

    # Convert the matrix to a tree structure so that we can sample within O(log(n)) time and sample from all of a players stragies with
    # a probabilitiy that is bounded by a one-norm instead of a 2-norm. Sparsity here is important as the
    # algorithm is more likely to converge to a solution that is robust to outliers when the 1-norm. 
    # its valid to use a 1-norm since this is just dividing over a probability distributon that is classic-- we just get a different metric 
    # that represents the distace between the values and changes the probability of getting a mixed strategy from the players set of total 
    # strategies
    def matrix_row_to_maxheap(self, dist):
        row_list = (dist)
        # Use heapq to transform the list into a max heap
        self.dist_heap =heapq._heapify_max(row_list)

    
    def find_element_in_maxheap(self, move):
        heap_list = list(self.distribution)
        for node in heap_list:
            if node == move:
                return move
            
    def prepare_circuit(self):
        num = self.sparsity
        reg_q = QuantumRegister(num, name='r') # 4 qbits for register
        moves_q= QuantumRegister(num, name='t') # quibits for each possible vector of size t
        output_qubit = QuantumRegister(1, name='out') # 1 qbit for output
        cbits = ClassicalRegister(num+num, name='cbits') 
        qc = QuantumCircuit(reg_q, t_max_q, output_qubit, cbits)
        qc.initialize([1, -1]/np.sqrt(2), output_qubit)    
        qc.h(req_q)
        qc.barrier()  
        self.forward_qram_n(qc, reg_q,  moves_q, sample_list)
        clause = real # 3

    #need a way to map each of the states in the tree to a qubit. This is done
    # to prepare the uniform distribution we sample | j > from 
    def forward_qram_n(self, qc, register_qubits, data, n, matrix): 
        state_prep_circit = QuantumCircuit(2, 2) 
        for i, row in enumerate(list(self.distribution)):
            move_list = list(self.distribution)
            mask = format(move_list, f'0{n}b')
            mask_i = format(i, f'0{n}b')
            # Apply X gate to qubits where mask_i is '0'
            [state_prep_circit.x(register_qubits[j]) for j, bit in enumerate(mask_i) if bit == '0']
            # Apply MCX gate to qubits where mask is '1'
            [qc.append(circuit.library.MCXGate(n), register_qubits[0:n] + [data[j]]) for j, bit in enumerate(mask) if bit == '1']
            # Reverse the X gates applied in the first step
            [state_prep_circit.x(register_qubits[j]) for j, bit in enumerate(mask_i) if bit == '0']
            qc.barrier()

    #Define the oracle for J state at its specific node index
    def oracle_n(qc, good_state, clause_qbits, node_index, output):
        good_state_binary = format(good_state, f'0{node_index}b')[::-1]
        qc.append(circuit.library.MCXGate(n, ctrl_state=good_state_binary), clause_qbits[0:n] + [output])
    
    
    # Maximum-finding algorithm to find the maximum element from the players mixed stratetgy outcome.
    # Accept with probability e^(uj-u_max)
    # Reject the u_max choice with 1- e^(uj-u_max)
    # Sampling J from all the choices, [m], uniformly.
    # post-select for j, means we only want the samples that are possible given what player 1 played.
    def find_Max(self, good_state):
        oracle = QuantumCircuit(2, 2)
        oracle.cz(0, 1)
        oracle.measure([0, 1], [0, 1])
        oracle = QuantumCircuit(2)
        oracle.cz(0, 1)
        # define Grover's algorithm
        problem = AmplificationProblem(oracle, is_good_state=good_state)
        # so we have to decompose() the op to see it expanded into its component gates.)
        problem.grover_operator.decompose().draw(output='mpl')or, shots=1000)
        result = job.result()
        # Get the counts from the result
        counts = result.get_counts(circuit)
        return
    
    # Sampling J from all the choices, [m], uniformly. Prepare a stat that prepares all a player's mixed strategies with uniform probabilities.
    # prepare |J> from a state vector
    #  TODO: Gibbs sampling from a linear combination of t sparse outcomes
    def prepare_uniform_dist(self):
        probabilities = self.distribution
        # Number of qubits in the quantum state
        num_qubits = len(probabilities)
        # Create a quantum circuit with the specified number of qubits
        qc = QuantumCircuit(num_qubits)
        # Apply X gates to set the initial state to |1⟩
        qc.x(range(num_qubits))
        # Apply rotations to set the desired probabilities
        # Map probability to angle
        for i, prob in enumerate(probabilities):
            angle = 2 * prob * np.pi  
            qc.rx(angle, i)
        # Apply a uniform distirbution over the probabilities
        qc.h(range(num_qubits))


