import Hmwk4 as Q1

PROB = 0.5
FLIPS = 20

# create a game
myGame = Q1.Game(headprob=PROB)

#simulate the game
myGame.simulate(FLIPS)


#print the dollar amount
print(myGame.self.reward())
