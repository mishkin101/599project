## Notes
Nash Equilibrium no one wants to switch: (NOTHING ABOUT PAYOFF AMOUNT)
- curr players startegy is as good as any other 
- other players startegy does not depend on this option
dominate: all other stratgies for player

individual versus group incentives
PD: group and individual in conflict (joint payoffhighest when non-dominate stratgey is played)

## Mixed strategy Nash equlibirum:
- player payoff: expectation value : probability * outcome
Payoff(player 2 | strategy x) = Sum_x: P(player 1 marginal move x)((player 2 payoff strategy x ))
- do for all strategies -> solve for marginal probabilities for each player
    - this is the probability for player 1  at which player 2 is indifferent in his strategy (weak domination)
    - if pure: see if there does exist a nash equlibirum:

## Pure Strategy: given player picks one strategy:
- minmax function 
- probability distribution

Each player has selected a strategy such that no player has an incentive to switch to another strategy given the strategies being played by the other players.

# Simplex method:
it is like taking steps around intersections of the simplex shape, and testing each maximum point at a corner
1. Always a max function (multiply by -1 to transform)
2. <= ( multiply the functions that are not in <= form)
3. No non negative values (all variables must be >= 0)

### Process:
1. Check the above conditions
2. Set constraints to equalities and add slack for each
3. Put variables into tablaeu (row for optimizaiton (z- rest =0, constraint n,...,))
4. Pick most negative value from optimization function row -> pivot column (c)
5. Divide the current constraints (b col) by the pivot colum -> choose smallest indictor (the upperbound constraint for this variable) (r)
6. Divie correspondiong row of the indictor by the Pivot A(r,c)
7. Gaussian eliminaiton
8. stopping condition: No negative variable in last row

The inidicator value (constraint for a given variable) is the smallest a value can be given the others stay 0. 
meaning, we are checking the maximum "stretch" along an eigenvector? e.i eigenvalue for this basis**

Once we pick x(largest gain we can make from optimizaiton), pick max that x can be withough making corresponding slack var negative
in the tightest bound constraint.

[RHS - Slack] : remaining units -> c
c / x coffecient -> remaining units/cost of unit = total produced if we maximize over the pivot variable unit.
(0,0,0)-> (x,0,0)-> (y,0,0)-> interesction somwhere at simplex
- then, every element in the table is the rate of change of 


A basic variable can be classified to have a single 1 value in its column and the rest be all zeros
non-basic it means the optimal solution of that variable is zero. 

**slack** -- underitlization 

## Quantum Component:

The aim of this project was to allow players to also choose quantum strategies as well as classical strategies. 

The players are trying to determine their best outcome. They don't know what the 

