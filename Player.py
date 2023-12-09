import numpy as np


# A player has a:
# Name
# number of Classical Strategies 
# Number of Quanntum Strategies
# A list of probability distbrutions for their strategies
# Their Strategy Type 
# A list of winnings
# A list of losses

class Player:
  game_theory_strategies = ["Dominant Strategy", "Weak Dominant", "Maximax Strategy", "Minimax Strategy", "Cooperative Strategy", "Non-cooperative Strategy", "Mixed Strategy"]
  
  #REQUIRED: Name and Strategy Type
  def __init__(
    self,
    name: str, 
    distributions: {int: int},
    #strategy number, payoff amount
    classical_strategies: int, 
    quantum_strategies: int,
    strategy_type: str,
    optimal_strategies: [],
    curren_strategy: np.ndarray
    ):
        self.name = name
        self.distirbutions = {}
        self.classical_strategies = classical_strategies
        self.strategy_type = strategy_type
        self.winnings = []
        self.losses = []
        self.quantum_strategies = quantum_strategies
        self.optimal_strategies = []
        self.current_strategy = None

  # Generate a sample from the Dirichlet distribution with varied probabilities for 
  # Both the classical and quantum strategies
  # Or generate a pure distirbution
  def generate_Distributions(self, num_distributions, pure=False):

    if (self.quantum_strategies == 0 or  self.quantum_strategies == 0):
      raise Exception ("The player has no strategies currently. Please create some based on the game.")

    if self.distirbutions:
      currkey = self.distirbutions.keys()[-1] + 1
    else:
       currkey = 1
    i = 0
    while i <= num_distributions:
      if pure:
         vec = np.zeros(self.quantum_strategies + self.classical_strategies, size=1)
         random_index = np.random.randint(n)
         vec[random_index] = 1
         self.distirbutions[currkey]
      else:
         self.distirbutions[currkey] = np.random.dirichlet(np.random.rand(self.quantum_strategies + self.classical_strategies), size=1)
      i+=1
      currkey+=1

  # Add an optimal distirbuton if finding mixed strategy from result of a game.
  def set_optimal_strategies(self, dist: np.ndarray):
    if self.distirbutions:
      currkey = self.distirbutions.keys()[-1] + 1
    else:
       currkey = 1
    self.distirbutions[currkey] = dist
    self.optimal_strategies.append[currkey]
  
  def clear_winnings(self):
     self.winnings = []

  def set_winnings(self, payout):
     self.winnings.append(payout)
     
  def get_winnings(self):
     return np.ndarray(self.winnings)
  
  def clear_losses(self):
     self.losses = []
     
  def set_losses(self, loss):
     self.winnings.append(loss)

  def get_losses(self):
     return np.ndarray(self.losses)
  
  def update_strategy_classical(self, val):
     self.classical_strategies[val] += val

  def update_strategy_quantum(self, val):
     self.quantum_strategies += val

  def clear_strategy_classical(self):
     self.classical_strategies = 0
  
  def clear_strategies_quantum(self):
     self.quantum_strategies = 0
  
  def clear_distributions(self):
     self.distirbutions = {}

  def update_strategy_type(self, int):
     self.strategy_type = Player.game_theory_strategies[int]
  
  def get_total_strategies(self):
     return self.quantum_strategies + self.classical_strategies

  def get_Name(self):
     return self.name
  
  def get_optimal_strategies(self):
     return [self.distirbutions[strategy] for strategy in self.optimal_strategies]
  
  def set_current_strategy(self, val):
     self.current_strategy = self.distirbutions[val]
   
  def get_current_strategy(self):
     return self.current_strategy