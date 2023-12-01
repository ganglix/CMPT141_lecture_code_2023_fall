# gambling problem
# a "fair" game: 50% chance losing 1 dollar, 50% winning 1 dollar
# quit gambling when my cash is 0 (bankrupt) or my cash reach upto ending_cash

# find what is the odd for me to go bankrupt
import random

def game(starting_cash, ending_cash):
    # return the outcome of playing the game
    cash = starting_cash
    while cash > 0 and cash < ending_cash:
        if random.random() > 0.5:   # 50% of chance
            cash += 1
        else:
            cash -= 1
    return cash

def game_simulation(n_sim, starting_cash, ending_cash):
    n_bankrupt = 0
    for i in range(n_sim):
        outcome = game(starting_cash, ending_cash)
        if outcome == 0:
            n_bankrupt += 1
    # calculate the odd of going bankrupt
    return n_bankrupt/n_sim    # probability

print("start with 10, only quit when 11")
print(game_simulation(10000, 10, 11))

print("start with 10, only quit when we get 20")
print(game_simulation(10000, 10, 20))

print("start with 10, only quit when we get 30")
print(game_simulation(10000, 10, 50))

print("start with 10, only quit when we get 30")
print(game_simulation(10000, 10, 100))

print("start with 10, only quit when we get 1000")
print(game_simulation(10000, 10, 1000))

