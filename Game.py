#define a payoff matrix
#have a distribution of strategies that players choose from 
import numpy as np
import Player
import Quantum
import Simplex

# A Game between players. We focus on zero-sum and 2 player games for this implementation functionality.
# A game has:
# A list of players
# Resulting payout from moves between players for each round
# An associated type (constant payout, zero sum, ect)
# The results of the game
#

class Game:
    game_type = ["Zero-Sum", "Constant-Sum", "Cooperative", "Non-Cooperative"]

    def __init__(
        self, 
        players: [Player],
        #quantum : [results] , classical: [results]
        results: {(Player, Player): list},
        gametype: str, 
        rounds: int,
        player_player_matrices: {(Player, Player): np.ndarray},
        #Player and strategies
        player_payoffs: {Player: {}},
        #payoff for strategy against all other players
        strategy_values: {int: {Player: np.ndarray}}
    ):
        self.players = []
        results = []
        gametype = None
        rounds = None
        payoffs = 0
        player_payoffs = {}
        strategy_values = {}
        return
    
    #Choose a gametype from the Game class.
    def setGameType(self, game: str):
        self.game_type = Game.game_type[Game.game_type.index(str)]

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
    
    #Determine Best Strategies, i.e., the value of the game
    def calculate_Best_Plays(self, player1, player2):
        if self.game_type == "Zero-sum":
            game_value = Simplex(player1, player2, self.gametype)

        return game_value
    
    def getResults():
        return 
    
    def getPlayTime():
        return
    
    def countMoves():
        return
    
    def getGameType():
        return self.gametype
    