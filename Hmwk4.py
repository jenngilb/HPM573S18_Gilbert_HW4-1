from enum import Enum
import numpy as np
#numpy gives access to random number generators

class coinState:
    HEADS = 1
    TAILS = 0

class Game(Enum):
    #a) initialize, b) next flip, c) play, d) get reward
    #initialize id, coinstate, count tails = 0, count win = 0, total flips = 20, and flipNumber =1, set random number, set random seed)
    def __init__(self, id):
        self._status = coinState.HEADS
        self.headprob = headprob
        self.id = id
        self.countT = 0
        self.countWin = 0
        self.totalflips = 20
        self.flipNumber = 1
        self._rnd = np.random
        self._rnd.seed(id)

    def nextflip(self):
        if self._coinState = coinState.HEADS:
            if randomnumber > 0.5:
                self._coinState = coinState.HEADS
                #set status to heads
            elif randomnumber <0.5:
                self._coinState = coinState.TAILS
                countT = 1
            # set status to T and count the number of Tails

        elif self._coinState = coinState.Tails:
            if randomnumber < 0.5:
                self._coinState = Tails
                countT +=1
            elif randomnumber > 0.5:
                self.coinState = Heads
                if countT >= 2:
                    countWin +=1
            self.Coinstate = 0

        flipNumber += 1

    def play(self)
            for i in range (1, totalFlips+1):
                #have two statements - one that has a random number, and one that has a seed (self.nextflip) --> see hospital example
                self.playGame()
                if self._rnd.sample() < self._headprob:
                    self._coinState = coinState.TAILS
                    self._countWin = t+1
            t +=1

## see survival model for sample

    def get_reward(self):
        if self._coinState=coinState.HEADS
            self._reward = -250 + (countWin*100)
            return self._countWin
        else:
            return None

class cohort:
    def __init__(self,id, pop_size):
    self.players = [] #list of players
    n = 1

    for i in range(pop_size):
            #create the player
            player = Player(id*pop_size+i, headprob)
            # add the player to the cohort
            self._player.append(player)

    def simulate(self, n_time_steps):
        # simulate all patients
        for patient in self._patients:
            patient.simulate(n_time_steps)

            # get the survival time




##old code

#class cohort:

    #def __init__(self, prob):
        #self._rnd = np.random
        #self.prob = prob
        #self.results = []
        #self.dollars = 0

    #def get_dollar_value(self,results):
        #test for tails and heads and return dollar amount
        #self.dollars = 100
        #return self.dollars

    #def simulate(self, n_time_sims):

        #t = 0 #simulation time

        #while t <= n_time_sims:
            #if self.rnd.sample()<self.prob:
                #self.results.append(1)
            #else:
                #self.results.append(0)


            #increment time
        #t +=1

        #dollars = self.get_dollar_value(self.results)

