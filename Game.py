#define a payoff matrix
#have a distribution of strategies that players choose from 
import numpy as np
import Player as Player
import Quantum as Quantum
import Simplex as Simplex
import time

# A Game between players. We focus on zero-sum and 2 player games for this implementation functionality.
# A game has:
# A list of players
# Resulting payout from moves between players for each round
# An associated type (constant payout, zero sum, ect)
# The results of the game
#

class Game:
    game_types = ["Zero-Sum", "Constant-Sum", "Cooperative", "Non-Cooperative"]

    def __init__(
        self, 
        players: [Player],
        #quantum : [results] , classical: [results]
        results: {(np.ndarray, np.ndarray): float},
        gametype: str, 
        rounds: int,
        player_player_matrices: {(Player, Player): np.ndarray},
        #Player and strategies
        player_payoffs: {Player: {}},
        #payoff for strategy against all other players
        strategy_values: {int: {Player: np.ndarray}}
    ):
        self.players = []
        self.results = []
        self.gametype = None,
        self.outcomes = {(): },
        self.player_payoffs = {}
        self.strategy_values = {}
        self.playtime = {(): float}
        return
    
    #Choose a gametype from the Game class.
    def setGameType(self, game: str):
        self.game_type = Game.game_types[Game.game_types.index(game)]

    #Create the players for the game
    def setPlayers(self, name, strategy_type, num_classical, num_quantum, num_distirbutions):
        new_player = Player(name, strategy_type, num_classical, num_quantum)
        new_player.generateDistributions(num_distirbutions)
        self.players.append[new_player]
    
    def getPlayer(self, name):
        i = 0
        while i != len(self.players):
            if self.players[i].getName(name) == name:
                return self.players[i]
        return "No Matching player found"

    # Create the payoff matrices between 2 players
    def set_payoff_matrix(self):
        if self.game_type == "Zero-sum":
            for player1 in self.players:
                for player2 in self.players:
                    if player1 != player2:
                        po_mat = self.generate_zero_sum_payoff_matrix(player1.get_total_strategies(), player1.get_total_strategies())
                        self.player_player_matrices[(player1, player2)] = po_mat
                        self.player_player_matrices[(player2, player1)] = -np.transpose(po_mat)
    
    # Generate a random zero-sum payoff matrix
    @staticmethod
    def generate_zero_sum_payoff_matrix(num_strat, num_strat2, payoff_range):
        matrix = np.random.randint(payoff_range[0], payoff_range[1], size=(num_strat, num_strat2), dtype=int)
        return matrix

    # Return the Payoff Matrix
    def getPayoffMatrix(self, player1, player2):
        return self.player_player_matrices[(player1,player2)]
    
    # Determine Best Strategies, i.e., the value of the game
    # This follows from the Min/Max theorem for Nash equlibriums
    def calculate_Best_Plays(self, player1, player2):
        if self.game_type == "Zero-Sum":
            best_player_strategies = Simplex(player1, player2, self.gametype)
            best_player_strategies.solve()
        return player1.get_optimal_strategies(), player2.get_optimal_strategies
    
    # Get the total time taken to find the optimal solution given a set of strating strategies
    # Each round tests two different starting strategies and their convergence time
    def play_Rounds(self, player1, player2, pure=False, total_strategies = 1, quantum = False):
        #determing if they start from pure or mixed strategies for this game.
        player1.generate_Distributions(total_strategies, pure)
        player2.generate_Distributions(total_strategies, pure)
        game_solver = Simplex(player1, player2, self.game_type)
        #Each round has a different starting strategy. Testing to see which neighborhoods lead to faster convergence.
        # The entire optimization happens within simplex.solve()
        for round in range(self.rounds):
            # Draw from their existing mixed strategies
            player1.set_current_strategy(np.random.randint(1, total_strategies))
            player2.set_current_strategy(np.random.randint(1, total_strategies))
            # Use optimizer to find the equlibrium
            time_to_play_round, result = self.timeGame(game_solver.solve(player1.get_current_strategy(), player2.get_current_strategy()))
            self.results[(player1.get_current_strategy(), player2.get_current_strategy())] = result
            self.playtime[(player1.get_current_strategy(), player2.get_current_strategy())] = time_to_play_round
    
    #Solve for the total time taken to play the game.
    # Used to calculate the runtime for quantum versus classical games, and different size matrices
    def getPlayTime(self):
        return self.playtime
    
    def timeGame(self, func):
        start_time = time.time()
        result = func()
        end_time = time.time()
        execution_time = end_time - start_time
        return execution_time, result

    def getGameType(self):
        return self.gametype
    
    def setRounds(self, inti):
        self.rounds = inti