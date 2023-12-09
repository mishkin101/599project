## Overview:
The aim of this project was to allow players to also choose quantum strategies as well as classical strategies. 

In solving the expected payout for a given strategy, the player's do not know what the other will play when we assume they draw at the same time. By playing many times, they can essentially recover their "density" matrix. Instead of using the simplex method to sample, we want to see if we can effeciently recover the best strategies the player should choose using Gibb's Sampling with the quantum component. 

Our goal is to compare the results using the Gibbs Sampling method rather than the simplex algorithm, which produces a probabilty vector, P(t), and Q(t). In the classical strategy, the simplex is converted from the primal-dual problem using the Maxmin functions to correctly setup the constraints. Upon getting the probabilites, they are fed-in again until the difference are within an e-approximate bound from the last draw. 

The type of game is always a **zero-sum** game, and players are choosing competitve strategies (hence, the minmax functions). Given these assumptions, we are always gauranteed to find a bound. 


## Quantum Subroutine Set-up 
1. pick 2 starting random vectors.
2. Amplitude estimation to find the max 
3. If this is a feasilible solution, accept it with rejection sampling test

**Assumptions**
 Assume the sample drawn from ( payoff strategies) norm >=B and B>=1.
 - Estimating a single value uj can be done via amplitude estimation. Given we have a heap, we have query (x^T)A, where x is a sparse vector up to some weight t wich accesses a certain neighborhood of the distirbution. Therefore, we obtain a way to query for the max elements player 2 can recieve, given player 1's strategy.
 - amplitude amplification to find the max
 - rejection sampling can done via amplitude amplification as well

**Matrix to Heap**
Convert the matrix to a tree structure so that we can sample within O(log(n)) time and sample from all of a players stragies with
a probabilitiy that is bounded by a one-norm instead of a 2-norm. Sparsity here is important as the algorithm is more likely to converge to a solution that is robust to outliers when the 1-norm. Its valid to use a 1-norm since this is just dividing over a probability distributon that is classic-- we just get a different metric that represents the distace between the values and changes the probability of getting a mixed strategy from the players set of total strategies.

**Find the Maximum Payoff for player 2 from Player 1's Strategy**
The rejectiom sampling portion will find the maximum element from the players mixed stratetgy outcome. We Accept with probability the element u_j from player 2's possible payoffs with proability e^(uj-u_max). We must consider sampling from all of players 2 choices, [m], uniformly and post-select for j-- meaning, we want to see how likely it is that this distrbution we have from player 1's choice will produce the max payoff for player 2.


## Algorithim
- Set strategy distirbutons for players -- can be pure or mixed
- Call game.playRounds to test various comibations of starting strategies and the time taken to solve for the nash equilibirum given this starting set
- Return all the round with the ending strategies for both players and the expected values at the equilbrium as well as the time to solve each round
- Test with both the quantum solver and the simplex solver using the dual version of the simplex method


## Notes
Nash Equilibrium occuers when no one wants to switch their strategy.
- curr players startegy is as good as any other 
- other players startegy does not depend on this option
dominate: all other stratgies for this player

Individual versus Group Incentives
joint payoffhighest when non-dominate stratgey is played

## Mixed strategy Nash equlibirum:
- player payoff: expectation value : probability * outcome
Payoff(player 2 | strategy x) = Sum_x: P(player 1 marginal move x)((player 2 payoff strategy x ))
- do for all strategies -> solve for marginal probabilities for each player
    - this is the probability for player 1  at which player 2 is indifferent in his strategy (weak domination)

Esentially, pure strategies are a specific subcase of a mixed strategy. Given any of the pure strategy vectors are in the mixed strategy distirbution, then this is a specific case of the mixed stratgey. Another obervation I had (but no tested here) is that I believe any mixed strategy payoff will never be better than any pure strategy which is included in its distirbution, since the mixed distribution is over all of the pure strategies. 

In our game, we assume that both players draw from a mixed distribution.

## Pure Strategy: given player picks one strategy:
- Minmax function. There is an equivalent condition such that in a "bayes" interpretation", given the other player picks a pure strategy is equivalent to selecting a mixed on. 

Each player has selected a strategy such that no player has an incentive to switch to another strategy given the strategies being played by the other players.

# Simplex method Implementation:
it is like taking steps around intersections of the simplex shape, and testing each maximum point at a corner
1. Always a max function (multiply by -1 to transform)
2. <= ( multiply the functions that are not in <= form)
3. No non negative values (all variables must be >= 0)

### Simplex Process:
1. Check the above conditions
2. Set constraints to equalities and add slack for each
3. Put variables into tablaeu (row for optimizaiton (z- rest =0, constraint n,...,))
4. Pick most negative value from optimization function row -> pivot column (c)
5. Divide the current constraints (b col) by the pivot colum -> choose smallest indictor (the upperbound constraint for this variable) (r)
6. Divie correspondiong row of the indictor by the Pivot A(r,c)
7. Gaussian eliminaiton
8. stopping condition: No negative variable in last row

The inidicator value (constraint for a given variable) is the smallest a value can be given the others stay 0. Meaning,we are checking the maximum "stretch" along an eigenvector? (eigenvalue for this basis)

Once we pick x(largest gain we can make from optimizaiton), pick max that x can be withough making corresponding slack var negative
in the tightest bound constraint.

[Right hand side - Slack] : remaining units -> c

c / x coffecient -> (remaining units/cost of unit) = total produced (or in the support) if we maximize over the pivot variable unit.

(0,0,0)-> (x,0,0)-> (y,0,0)-> interesction somwhere at simplex edges
- Then, every element in the table is the rate of change. Essentially, this is like finding partial derivatives.


A basic variable can be classified to have a single 1 value in its column and the rest be all zeros
non-basic it means the optimal solution of that variable is zero. 

** Slack ** -- Underitlization 