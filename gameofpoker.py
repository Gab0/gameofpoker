#python script
from random import randint,randrange
import operator

import neuronal
from neuronalIO import *

names = ['Freddie', 'Suzanne', 'Wellington', 'Roberts', 'Spacely', 'John', 'Ruanito', 'Chavez', 'Wilson', 'Ford', 'Nikolai', 'Samara', 'Fernandita', 'Nikki', 'Andersen', 'Magda',
         'Rutherford', 'Dawkins', 'Rosenblatt', 'Elvis', 'Schapire', 'Freund', 'Grossberg', 'Collins', 'Patton', 'Albert', 'Klein', 'Hankel', 'Hilbert']

GAME = True
version = "v0.6"
class player:

    def __init__(self, name = 'zero'):
        self.chips = 1500
        self.bet = 0

        if name == 'zero':
            x = randint(0, len(names)-1)
            self.name = names[x]
            del names[x]
            
        else:
            self.name = name
        
        self.dead = 0
        
        self.HandCards = []
        self.h1 = None
        self.h2 = None

        self.fold = 0
        
        self.N = len(players)


    def getabrain(self):
        print('dificil')


    def paycheck(self):
        if (pkr.bet-self.bet) > self.chips:
            pkr.pot += self.chips
            self.chips=0
            print("")
            print(player.name+" goes ALL IN!")
            print("")
    
     
        elif pkr.bet > self.bet:
                self.chips -= (pkr.bet-self.bet)
                pkr.pot += (pkr.bet-self.bet)
            
                print("%s pays %i chips.\n" % (self.name, pkr.bet-self.bet))
                self.bet = pkr.bet

        elif pkr.bet == self.bet:
                print(self.name+" checks.\n")

    def raisebet(self, cash = None):
        if not cash: cash = pkr.minimum
        
        if self.chips > pkr.bet-self.bet+cash:
            
            pkr.bet += cash
            pkr.pot += (pkr.bet-self.bet)
            self.chips -=(pkr.bet - self.bet)
            self.bet = pkr.bet
            print("%s raises to %i chips." % (self.name,pkr.bet))
            print("")
            pkr.lastbet = self.N
            return 1
        elif self.chips <= pkr.bet-self.bet+cash:

            pkr.pot += self.chips
            pkr.bet += self.chips
            self.bet += self.chips
            self.chips = 0
            print("")
            print("%s raises to ALL IN! [%i chips]." % (self.name,pkr.bet))
            return 1
        else:
            return 0

    def Fold(self):
        self.fold=1

class AI_player(player):
    def __init__(self):
        player.__init__(self)

        
        Z = neuronal.grabAbrain()
        self.brain_Weights = Z[0] 
        self.brain_Thresholds = Z[1]
        
        

    def plays(self):
        
        strt = 0 

        print(self.name + "'s turn... he got " + str(self.chips) + " chips.")
        print("thinking")
        
        self.think()

        input("")
    def Card2int(self,card):
        CVT = {"e":0.2,"p":0.4,"o":0.6,"c":0.8,"T":10,"J":11,"Q":12,"K":13,"A":14}
        try:
            return CVT[card]
        except:
            return int(card)
        
        
    def think(self):
        Senses = [self.chips/pkr.buyin]

        for i in range(len(self.HandCards)):
            Senses.append(self.Card2int(self.HandCards[i][0]))
            Senses.append(self.Card2int(self.HandCards[i][1]))
        for i in range(len(pkr.TableCards)):
            Senses.append(self.Card2int(pkr.TableCards[i][0]))
            Senses.append(self.Card2int(pkr.TableCards[i][1]))
        while len(Senses) < 11:
            Senses.append(0)
        
        
        Brain = neuronal.think(Senses, Weights = self.brain_Weights,
                                       Thresholds = self.brain_Thresholds)
        print("[AI debug info] %i & %i" % (Brain[0],Brain[1]))
        if Brain[0] < 1200:
            self.Fold()
        if Brain[0] > Brain[1]:
            self.raisebet()
        else:
            self.paycheck()

        return
        
class Human_player(player):
    def __init__(self, name = 'zero'):
        player.__init__(self, name)
    

    def plays(self):
        
        strt = 0 
        action = 0
        print("")

        
        print("your turn... you got " + card[self.HandCards[0]] + " and " + card[self.HandCards[1]] + ".\n")
        print("also, you have " + str(self.chips) + " chips.\n")
        print("The pot is at " +str(pkr.pot)+ " chips.\n")
        print("Current bet is "+str(pkr.bet)+" chips.\n")
        print("You have already bet "+str(self.bet)+" chips this round.\n")
        self.options()
        print("")
        
    def options(self):
        Chk = "pay"
        if pkr.bet==self.bet: Chk = "check"
        Prompt = "do?... [fold/%s/raise/bet/look table]" % Chk
        action=0
  
        while not (action == "fold") and not(action =="check") and not (action=="pay") and not (action=="raise") and not (action=="bet") and not (action=="look table"):
            action = input(Prompt)
        else:
                      
            if action == "check":
                if pkr.bet <= self.bet:
                    print("You check.")
                    print("")
                else:
                    print("you can't check as there is a bet. fold or pay")
                    self.options()
                    return

            elif action == "pay":
                print("")
                self.paycheck()

            elif action == "fold":
                    self.Fold()
                    print("you fold.")
                    print("")

            elif action == "raise":
                    print("")
                    self.raisebet()

            elif action == "look table":
                    pkr.peektable()
                    self.options()
                    return

            elif action == "bet":
                    print("")
                    cash = "nada"
                    while not cash.isdigit():
                        cash = input("Put away the whisky... how many chips?")
                   
                    self.raisebet(cash=int(cash))
                    
        
class game:

    def __init__(self):
        self.pot = None
        self.bet = None
        self.minimum = 20
        self.button = NP
        self.deck = None


        self.TableCards = [] 
        self.f1 = None
        self.f2 = None
        self.f3 = None
        self.trn = None
        self.riv = None

        self.lastbet = None

        self.whoplays = 0

        self.buyin = 1500
        
        self.phase = 0
    def dealcard(self):
        x = randint(0,len(pkr.deck)-1)
        _card = self.deck[x]
        del self.deck[x]
        
        return _card


    def deal2table(self):
 
        self.TableCards.append(self.dealcard())
        print("Dealer puts a %s in the table." % self.TableCards[-1])
        
    def peektable(self):
        print('You peek at the table;')
        for Card in self.TableCards:
            print('.. %s.' %card[Card])

NP = 4

pkr = game()
players = []
players = [Human_player(name = input('Your name, sir?'))]
while len(players) < NP:
    players.append(AI_player())


print("Welcome to the satanic poker table %s, %s." % (version, players[0].name) )
print("")
print("You will be seated in a four-player NLHE tournament table.")
input("")
print("And will end victorious if you can beat the AI before they beat you. Have fun, and suffer.")
input("")
print("")
print("%s is in front of you, %s your left, and %s your right." % (players[1].name,players[2].name,players[3].name))
print("")
input("")


print() 

#card name content. 'e' stands for spades, 'p' for clubs, 'o' for diamonds, and 'c' for hearts...
card = {'eA': 'Ace of Spades', 'pA': 'Ace of Clubs', 'oA': 'Ace of Diamonds', 'cA': 'Ace of Hearts'}
cardz = {'eK': 'King of Spades', 'pK': 'King of Clubs', 'oK': 'King of Diamonds', 'cK': 'King of Hearts'}
card.update(cardz)
cardz = {'eQ': 'Queen of Spades', 'pQ': 'Queen of Clubs', 'oQ': 'Queen of Diamonds', 'cQ': 'Queen of Hearts'}
card.update(cardz)
cardz = {'eJ': 'Jack of Spades', 'pJ': 'Jack of Clubs', 'oJ': 'Jack of Diamonds', 'cJ': 'Jack of Hearts'}
card.update(cardz)
cardz = {'eT': 'Ten of Spades', 'pT': 'Ten of Clubs', 'oT': 'Ten of Diamonds', 'cT': 'Ten of Hearts'}
card.update(cardz)
cardz = {'e9': 'Nine of Spades', 'p9': 'Nine of Clubs', 'o9': 'Nine of Diamonds', 'c9': 'Nine of Hearts'}
card.update(cardz)
cardz = {'e8': 'Eight of Spades', 'p8': 'Eight of Clubs', 'o8': 'Eight of Diamonds', 'c8': 'Eight of Hearts'}
card.update(cardz)
cardz = {'e7': 'Seven of Spades', 'p7': 'Seven of Clubs', 'o7': 'Seven of Diamonds', 'c7': 'Seven of Hearts'}
card.update(cardz)
cardz = {'e6': 'Six of Spades', 'p6': 'Six of Clubs', 'o6': 'Six of Diamonds', 'c6': 'Six of Hearts'}
card.update(cardz)
cardz = {'e5': 'Five of Spades', 'p5': 'Five of Clubs', 'o5': 'Five of Diamonds', 'c5': 'Five of Hearts'}
card.update(cardz)
cardz = {'e4': 'Four of Spades', 'p4': 'Four of Clubs', 'o4': 'Four of Diamonds', 'c4': 'Four of Hearts'}
card.update(cardz)
cardz = {'e3': 'Three of Spades', 'p3': 'Three of Clubs', 'o3': 'Three of Diamonds', 'c3': 'Three of Hearts'}
card.update(cardz)
cardz = {'e2': 'Two of Spades', 'p2': 'Two of Clubs', 'o2': 'Two of Diamonds', 'c2': 'Two of Hearts'}
card.update(cardz)

time = 0

pot = 0

deck= None




# function starts the round and deal the cards.
def deal():
    
    # deck generator. first char [0] stands for color, and second [1] for number.    
    pkr.deck = ['eA', 'pA', 'oA', 'cA', 'eK', 'pK', 'oK', 'cK', 'eQ', 'pQ', 'oQ', 'cQ', 'eJ', 'pJ', 'oJ', 'cJ', 'eT', 'pT', 'oT', 'cT', 'e9', 'p9', 'o9', 'c9', 'e8', 'p8', 'o8', 'c8', 'e7', 'p7', 'o7', 'c7', 'e6', 'p6', 'o6', 'c6', 'e5', 'p5', 'o5', 'c5', 'e4', 'p4', 'o4', 'c4', 'e3', 'p3', 'o3', 'c3', 'e2', 'p2', 'o2', 'c2']


    for player in players:
        player.fold = 0
        if not player.dead:
            for x in range(2):
                player.HandCards.append(pkr.dealcard())
            

    pkr.gamephase = 0
    pkr.TableCards = []
    
    print("dealing...")

    print("you got %s and %s." % (card[players[0].HandCards[0]],card[players[0].HandCards[1]]))
    print("")



def player_turn(N):
    player = players[N]
    if player.chips > 0:
        if not player.fold:
            player.plays()


def nextplayer():
    pkr.whoplays += 1
    if pkr.whoplays >= len(players):
        pkr.whoplays = 0
 
   
def change_gamephase():
    outs = 0
    for p in players:
        outs += p.fold
        p.bet=0
        if not (p.dead) and (p.chips <= 0):      
            outs +=1


    if outs + 1 == len(players):
        print("")
        setprematureend()
        
    pkr.bet = 0
    pkr.lastbet = None
    
    phasenames = ['preflop','flop', 'turn', 'river']
    if not pkr.gamephase: x=3
    else: x=1
    pkr.gamephase +=1

    if pkr.gamephase >3:
        conclusion()
        return
    print('Dealer deals the %s....' % phasenames[pkr.gamephase])
    for z in range(x):
        print("")
        pkr.TableCards.append(pkr.dealcard())
        print("%s in da table!" % card[pkr.TableCards[-1]])
        print("")
    input("")
    

    pkr.start = 1

    pkr.whoplays = pkr.button


def conclusion():
    print("")
    print("*** checking player's hands ***")
    input("")

    winner = []
    value = 0

    
    for player in players:
        if not player.fold:

            print(player.name+" got:")
            print("")
            for C in player.HandCards:
                print(card[C])

            print("")
            handvalue = checkhandvalue(player)


            print(comment)
            print("")

            if handvalue > value:
                winner = [player]
                value = handvalue
                
            elif handvalue == value:
                winner.append(i)
                
    print("")
    

    if len(winner) == 1:
        print(winner[0].name+" wins "+str(pkr.pot)+" chips.")
        winner[0].chips += pkr.pot

    elif len(winner) > 1:
        print("splitpot! " + str(pkr.pot/len(winner))+ " for each.")
        for i in range(0, len(winner)):
            print(winner[i].name)
            winner[i].chips += pkr.pot/len(winner)
         
            
    pkr.pot = 0


    print("")
    print("")
    input("")


    if players[0].chips <= 0:
        print("")
        print("Game Over.")
        while True:
            input("")
 

    
#function called when players raise the bet.



def setprematureend():
    print('Game ends now!')

    if pkr.gamephase == 0:
                for i in range(5): pkr.deal2table()
                conclusion()
    elif pkr.gamephase == 1:
                for i in range(2): pkr.deal2table()
                conclusion()
    elif pkr.gamephase == 2:
                pkr.deal2table()
                conclusion()
    elif pkr.gamephase == 3:
                conclusion()
    


#AI-related hand value speculation routines, one for each of the game phases

def checkhandpreflop(h, hh):

    
    handvalue = 0
    if (h[1] == "A") and (hh[1] == "A"):
        handvalue += 30
    elif (h[1] == "A") or (hh[1] == "A"):
        handvalue += 15
        
    if (h[1] == "K") and (hh[1] == "K"):
        handvalue += 28
    elif (h[1] == "K") or (hh[1] == "K"):
        handvalue += 14

    if (h[1] == "Q") and (hh[1] == "Q"):
        handvalue += 26        
    elif (h[1] == "Q") or (hh[1] == "Q"):
        handvalue += 12
        
    if (h[1] == "J") and (hh[1] == "J"):
        handvalue += 22        
    elif (h[1] == "J") or (hh[1] == "J"):
        handvalue += 10

    if (h[1] == "T") and (hh[1] == "T"):
        handvalue += 20        
    elif (h[1] == "T") or (hh[1] == "T"):
        handvalue += 8
    
    if (h[1] == "2") or (hh[1] == "2"):
        handvalue -= 4
    if (h[1] == "3") or (hh[1] == "3"):
        handvalue -= 3
    if (h[1] == "4") or (hh[1] == "4"):
        handvalue -= 1
                        
        
        


    if h[0] == hh[0]:#if got pair of same color
        handvalue += 40
    elif h[1] == hh[1]:#if got pair of same number
        handvalue +=30

    return handvalue

def checkhandflop(h, hh, t, tt, ttt):
    handvalue = 0
    
    n = h[0]+hh[0]+t[0]+tt[0]+ttt[0]
    e=0
    p=0
    o=0
    c=0
    for i in range(len(n)):
        if n[i] == "e":
            e+=1
        elif n[i] == "p":
            p+=1
        elif n[i] == "o":
            o+=1
        elif n[i] == "c":
            c+=1

    if (c==3) or (p==3) or (o==3) or (c==3):
        handvalue+=15

    m = h[1]+hh[1]+t[1]+tt[1]+ttt[1]

    i2=0
    i3=0
    i4=0
    i5=0
    i6=0
    i7=0
    i8=0
    i9=0
    T=0
    J=0
    Q=0
    K=0
    A=0

    for i in range(len(m)):
        if m[i] == 'i2':
          i2+=1
        if m[i] == 'i3':
          i3+=1
        if m[i] == 'i4':
          i4+=1
        if m[i] == 'i5':
          i5+=1
        if m[i] == 'i6':
          i6+=1
        if m[i] == 'i7':
          i7+=1
        if m[i] == 'i8':
          i8+=1
        if m[i] == 'i9':
          i9+=1
        if m[i] == 'T':
          T+=1
        if m[i] == 'J':
          J+=1
        if m[i] == 'Q':
          Q+=1
        if m[i] == 'K':
          K+=1
        if m[i] == 'A':
          A+=1

    ms = str(i2)+str(i3)+str(i4)+str(i5)+str(i6)+str(i7)+str(i8)+str(i9)+str(T)+str(J)+str(Q)+str(K)+str(A)
    if "3" in ms:
            handvalue += 20
    if "2" in ms:
            handvalue += 10

    handvalue = randint(0, 15)
    return handvalue

        
def checkhandturn(h, hh, t, tt, ttt, tu):
    handvalue = 0
    
    n = h[0]+hh[0]+t[0]+tt[0]+ttt[0]+tu[0]
    e=0
    p=0
    o=0
    c=0
    for i in range(len(n)):
        if n[i] == "e":
            e+=1
        elif n[i] == "p":
            p+=1
        elif n[i] == "o":
            o+=1
        elif n[i] == "c":
            c+=1

    if (c==3) or (p==3) or (o==3) or (c==3):
        handvalue+=15

    m = h[1]+hh[1]+t[1]+tt[1]+ttt[1]+tu[1]

    i2=0
    i3=0
    i4=0
    i5=0
    i6=0
    i7=0
    i8=0
    i9=0
    T=0
    J=0
    Q=0
    K=0
    A=0

    for i in range(len(m)):
        if m[i] == 'i2':
          i2+=1
        if m[i] == 'i3':
          i3+=1
        if m[i] == 'i4':
          i4+=1
        if m[i] == 'i5':
          i5+=1
        if m[i] == 'i6':
          i6+=1
        if m[i] == 'i7':
          i7+=1
        if m[i] == 'i8':
          i8+=1
        if m[i] == 'i9':
          i9+=1
        if m[i] == 'T':
          T+=1
        if m[i] == 'J':
          J+=1
        if m[i] == 'Q':
          Q+=1
        if m[i] == 'K':
          K+=1
        if m[i] == 'A':
          A+=1

    ms = str(i2)+str(i3)+str(i4)+str(i5)+str(i6)+str(i7)+str(i8)+str(i9)+str(T)+str(J)+str(Q)+str(K)+str(A)
    if "3" in ms:
            handvalue += 20
    if "2" in ms:
            handvalue += 10

    handvalue = randint(0, 15)
    return handvalue


def checkhandriver(h, hh, t, tt, ttt, tu, riv):

    handvalue = 0
    
    n = h[0]+hh[0]+t[0]+tt[0]+ttt[0]+tu[0]+riv[0]
    e=0
    p=0
    o=0
    c=0
    for i in range(len(n)):
        if n[i] == "e":
            e+=1
        elif n[i] == "p":
            p+=1
        elif n[i] == "o":
            o+=1
        elif n[i] == "c":
            c+=1

    if (c==3) or (p==3) or (o==3) or (c==3):
        handvalue+=15

    m = h[1]+hh[1]+t[1]+tt[1]+ttt[1]+tu[1]+riv[1]

    i2=0
    i3=0
    i4=0
    i5=0
    i6=0
    i7=0
    i8=0
    i9=0
    T=0
    J=0
    Q=0
    K=0
    A=0

    for i in range(len(m)):
        if m[i] == 'i2':
          i2+=1
        if m[i] == 'i3':
          i3+=1
        if m[i] == 'i4':
          i4+=1
        if m[i] == 'i5':
          i5+=1
        if m[i] == 'i6':
          i6+=1
        if m[i] == 'i7':
          i7+=1
        if m[i] == 'i8':
          i8+=1
        if m[i] == 'i9':
          i9+=1
        if m[i] == 'T':
          T+=1
        if m[i] == 'J':
          J+=1
        if m[i] == 'Q':
          Q+=1
        if m[i] == 'K':
          K+=1
        if m[i] == 'A':
          A+=1

    ms = str(i2)+str(i3)+str(i4)+str(i5)+str(i6)+str(i7)+str(i8)+str(i9)+str(T)+str(J)+str(Q)+str(K)+str(A)
    if "3" in ms:
            handvalue += 20
    if "2" in ms:
            handvalue += 10

    handvalue = randint(0, 15)
    return handvalue

def prepare():
    pkr.pot = 0


    pkr.strt=1

    for player in players:
        if player.chips <= 0:
            player.dead = 1

def blind():

    pkr.whoplays = pkr.button
    print(pkr.button)

    nextplayer()
    pkr.button = pkr.whoplays


    print("")
    print(players[pkr.whoplays].name+" is the dealer.")
    print("")
    nextplayer()
    print(players[pkr.whoplays].name + " pays " + str(pkr.minimum/2) + " chips.")
    
    pkr.pot += pkr.minimum/2
    
    players[pkr.whoplays].chips -= pkr.minimum/2
    players[pkr.whoplays].bet = pkr.minimum/2

    nextplayer()

    print(players[pkr.whoplays].name + " pays " + str(pkr.minimum) + " chips.\n")
    
    pkr.pot += pkr.minimum
    pkr.bet = pkr.minimum
    
    players[pkr.whoplays].chips -= pkr.minimum
    players[pkr.whoplays].bet = pkr.minimum
    
    pkr.lastbet = pkr.whoplays
    input("")

    
    



def AI_preflop(player):
        h1 = player.h1
        h2 = player.h2
        pname = player.name
        foldz = player.fold
        pbet = player.bet



        handvalue = randrange(30)#checkhandpreflop(h1, h2)
        #if he will raise
        will = randint(0,15)
        
        if handvalue+will > 42:
            raisebet(player)

        #if he will check
        elif handvalue+will >= 7:
            paycheck(player)

        #if he will fold
        elif handvalue+will < 7:
            folds(player)

        elif bet > pbet:
            if handvalue+will > 20:
                paycheck(player)
            else:
                folds(player)

def AI_flop(player):

        h1 = player.h1
        h2 = player.h2
        pname = player.name
        foldz = player.fold
        pbet = player.bet
        


        handvalue = randrange(30)#checkhandflop(h1, h2, pkr.f1, pkr.f2, pkr.f3)
        #if he will raise
        will = randint(0,15)
        if handvalue+will > 38:
            raisebet(player)
            
        #if he will check
        elif handvalue+will >= 7:
            paycheck(player)
                
        #If he will fold
        elif handvalue+will < 7:
            folds(player)

        elif bet > pbet:
            if handvalue+will > 20:
                paycheck(player)
            else:
                folds(player)


def AI_turn(player):
        h1 = player.h1
        h2 = player.h2
        pname = player.name
        foldz = player.fold
        pbet = player.bet

        handvalue = randrange(30)#checkhandturn(h1, h2, pkr.f1, pkr.f2, pkr.f3, pkr.trn)
        #if he will raise
        will = randint(0,15)
        if handvalue+will > 38:
            raisebet(player)
            
        #if he will check
        elif handvalue+will >= 7:
            paycheck(player)
                
        #If he will fold
        elif handvalue+will < 7:
            folds(player)

        elif bet > pbet:
            if handvalue+will > 20:
                paycheck(player)
            else:
                folds(player)


            
def AI_river(player):
        h1 = player.h1
        h2 = player.h2
        pname = player.name
        foldz = player.fold
        pbet = player.bet

        handvalue = randrange(30)#checkhandriver(h1, h2, pkr.f1, pkr.f2, pkr.f3, pkr.trn, pkr.riv)
        #if he will raise
        will = randint(0,15)
        if handvalue+will > 38:
            raisebet(player)
            
        #if he will check
        elif handvalue+will >= 7:
            paycheck(player)
                
        #If he will fold
        elif handvalue+will < 7:
            folds(player)

        elif bet > pbet:
            if handvalue+will > 20:
                paycheck(player)
            else:
                folds(player)


def folds(player):
    

            print(player.name+" folds.")
            player.fold = 1


def checkhandvalue(player):
        global comment
        comment = "Nothing."

        a = player.HandCards[0]
        b = player.HandCards[1]
        pname = player.name


        handvalue = 0

        cardpool = player.HandCards + pkr.TableCards

        game = ""
        colors = ""
        numbers = ""
        for card in cardpool:
            game += card
            colors += card[0]
            numbers += card[1]
        
        
        s = 0
        p = 0
        o = 0
        c = 0
        n2 = 0
        n3 = 0
        n4 = 0
        n5 = 0
        n6 = 0
        n7 = 0
        n8 = 0
        n9 = 0
        T = 0
        J = 0
        Q = 0
        K = 0
        A = 0

        colors = ''.join(sorted(colors))
        numbers = ''.join(sorted(numbers))
        unumbers = ''.join(sorted("".join(set(numbers))))

        

        for i in range(len(game)):
                        if game[i] == "s":
                            s += 1
                        elif game[i] == "p":
                            p += 1
                        elif game[i] == "o":
                            o += 1
                        elif game[i] == "c":
                            c += 1
                        elif game[i] == "2":
                            n2 += 1
                        elif game[i] == "3":
                            n3 += 1
                        elif game[i] == "4":
                            n4 += 1
                        elif game[i] == "5":
                            n5 += 1
                        elif game[i] == "6":
                            n6 += 1
                        elif game[i] == "7":
                            n7 += 1
                        elif game[i] == "8":
                            n8 += 1
                        elif game[i] == "9":
                            n9 += 1
                        elif game[i] == "T":
                            T += 1
                        elif game[i] == "J":
                            J += 1
                        elif game[i] == "Q":
                            Q += 1
                        elif game[i] == "K":
                            K += 1
                        elif game[i] == "A":
                            A += 1
                            
                       


        
        pos2 =0

        poscard={0: 'A', 1: 'K', 2: 'Q', 3: 'J', 4: 'T', 5: '9', 6: '8', 7: '7', 8: '6', 9: '5', 10: '4', 11: '3', 12: '2'}
        antiposcard=dict((value,key) for key,value in poscard.items())

        
        if antiposcard[a[1]] <= antiposcard[b[1]]:
            hc = a
            lc = b
        else:   
            hc = b
            lc = a




                            
        
            
        xit = str(n2)+str(n3)+str(n4)+str(n5)+str(n6)+str(n7)+str(n8)+str(n9)+str(T)+str(J)+str(Q)+str(K)+str(A)
        xit = xit[::-1]
        if "4" in xit:

            pos=xit.index('4')
            comment = "Quartet of "+poscard[pos]+"'s."

            handvalue = 1600
            deuce = 13 - pos
            handvalue += deuce
            
        elif ("3" in xit) and ("2"in xit):
            pos=xit.index('3')
            pos2=xit.index('2')
           
            comment = "full house... "+poscard[pos]+" 's, and "+poscard[pos2]+" 's."
            handvalue=800
            deuce = 80-2*pos
            handvalue += deuce
            deuce = 13-pos2
            handvalue += deuce
            

        elif (c > 4) or (p > 4) or (s > 4) or (o > 4):
            
            comment = "Flush!"
            handvalue += 1000
            
        elif containsAll(unumbers, 'TJQKA') == 1:
            
            comment = "Sequence... Ten to Ace"
            handvalue =600

        elif containsAll(unumbers, "9TJQK") == 1:
            
            comment = "Sequence... Nine to Kings"
            handvalue =590
        elif containsAll(unumbers, "89TJQ") == 1:
            
            comment = "Sequence... Eight to Queens"
            handvalue =580
        elif containsAll(unumbers, "789TJ") == 1:
            
            comment = "Sequence... Seven to Jack"
            handvalue =570
        elif containsAll(unumbers, "6789T") == 1:
            
            comment = "Sequence... Six to Ten"
            handvalue =560
        elif containsAll(unumbers, "56789") == 1:
            
            comment = "Sequence... Five to Nine"
            handvalue =550
        elif containsAll(unumbers, "45678") == 1:
            
            comment = "Sequence Four to Eight"
            handvalue =540
        elif containsAll(unumbers, "34567") == 1:
            
            comment = "Sequence... Three to Seven"
            handvalue =530
        elif containsAll(unumbers, "23456") == 1:
           
            comment = "Sequence... Two to Six"
            handvalue =520
        elif containsAll(unumbers, "A2345") == 1:
            
            comment = "Sequence... A to Five"
            handvalue =510
        
        elif "3" in xit:
            pos=xit.index('3')
            
            comment = "Trio"
            handvalue = 400
            deuce = 13-pos
            handvalue+=deuce
            
        elif "2" in xit:
            
            pos=xit.index('2')
            
            if "2" in xit[pos+1:12]:
               pos2=xit[pos+1:12].index('2')+pos+1
               
               handvalue = 360
               deuce = -13*pos
               handvalue += deuce
               
               comment = "Two pairs... "+poscard[pos]+"'s and "+poscard[pos2]+"'s ."

               if (pos != antiposcard[hc[1]]) and (pos2 != antiposcard[hc[1]]):
                   comment += "Kicker: "+hc[1]
                   handvalue += 13-antiposcard[hc[1]]

               elif (pos != antiposcard[lc[1]]) and (pos2 != antiposcard[lc[1]]):
                   comment += "Kicker: "+lc[1]
                   handvalue += 13-antiposcard[lc[1]]
               
            else:
               
               handvalue=180
               deuce=-13*pos
               handvalue += deuce
                
               
               comment = "Pair of "+poscard[pos]+"'s."

               if pos != antiposcard[hc[1]]:
                   comment += " Kicker: "+hc[1]
                   handvalue += 13-antiposcard[hc[1]]

               elif pos != antiposcard[lc[1]]:
                   comment += " Kicker: "+lc[1]
                   handvalue += 13-antiposcard[lc[1]]

        else:

            handvalue = 13-antiposcard[hc[1]]
            comment = "High Card "+hc[1]


               
        return handvalue

def containsAll(str, set):
    
    return 0 not in [c in str for c in set]


def premature(player):
    if player == "w":
       global wchips 
       wchips += pot
       pname = wname

    if player == "e":
       global echips 
       echips += pot
       pname = ename

    if player == "n":
       global nchips 
       nchips += pot
       pname = nname

    if player == "s":
       global schips 
       schips += pot
       pname = sname
   


        
    print("")
    print(pname+" wins "+pot+" chips.")
    print("")

    blind()

def gameloop():
    prepare()
    deal()
    blind()
    while pkr.gamephase<4:
        nextplayer()
        
        if pkr.lastbet == pkr.whoplays:
            change_gamephase()
        else:
            player_turn(pkr.whoplays)
while GAME == True:               
    gameloop()
