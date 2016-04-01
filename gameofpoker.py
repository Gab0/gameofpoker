#!/bin/python

#######################################################################
#                                                                     #
# gameofpoker, a text-based poker simulator made to be fun (?)        #
# and to serve as a framework for development of exotic               #
# neural networks which will power the dumb intelligence of the       #
# computer players. For minimal playability, each player needs        #
# to be initialized (pre-trained) on its debut, please wait.          #
#                                                                     #
#######################################################################

from random import randint, randrange, choice
import operator
import sys
import time

from Neuronal import neuronal, utils


names = ['Freddie', 'Suzanne', 'Wellington', 'Roberts', 'Spacely',
         'John', 'Ruanito', 'Chavez', 'Wilson', 'Ford', 'Nikolai',
         'Samara', 'Fernandita', 'Nikki', 'Andersen', 'Magda',
         'Rutherford', 'Dawkins', 'Rosenblatt', 'Elvis', 'Schapire',
         'Freund', 'Grossberg', 'Collins', 'Patton', 'Albert',
         'Klein', 'Hankel', 'Hilbert']

GAME = True
version = "v0.7"


class player():

    def __init__(self, name='zero'):
        self.chips = 1500
        self.bet = 0
        self.Brain = 0

        if name == 'zero':
            x = randint(0, len(names) - 1)
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

    def paycheck(self):
        if (pkr.bet - self.bet) > self.chips:
            pkr.pot += self.chips
            self.chips = 0
            print("")
            print("%s goes ALL IN!" % self.name)
            print("")

        elif pkr.bet > self.bet:
            self.chips -= (pkr.bet - self.bet)
            pkr.pot += (pkr.bet - self.bet)

            print("%s pays %i chips.\n" % (self.name, pkr.bet - self.bet))
            self.bet = pkr.bet

        elif pkr.bet == self.bet:
            print(self.name + " checks.\n")

    def raisebet(self, cash=None):
        if not cash:
            cash = pkr.minimum

            if self.chips > pkr.bet - self.bet + cash:

                pkr.bet += cash
                pkr.pot += (pkr.bet - self.bet)
                self.chips -= (pkr.bet - self.bet)
                self.bet = pkr.bet
                print("%s raises to %i chips." % (self.name, pkr.bet))
                print("")
                pkr.lastbet = self.N
                return 1
        elif self.chips <= pkr.bet - self.bet + cash:

            pkr.pot += self.chips
            pkr.bet += self.chips
            self.bet += self.chips
            self.chips = 0
            print("")
            print("%s raises to ALL IN! [%i chips]." % (self.name, pkr.bet))
            pkr.lastbet = self.N
            return 1
        else:
            return 0

    def Fold(self):
        print("%s folds." % self.name)
        self.fold = 1
        # pkr.checkSurvival()


class AI_player(player):

    def __init__(self):
        player.__init__(self)

        self.Brain = neuronal.NeuralNetwork(name=self.name)

    def plays(self):

        strt = 0

        print(self.name + "'s turn... he got " + str(self.chips) + " chips.")
        print("thinking")

        self.think()

        WaitInput()

    def Card2int(self, card):
        CVT = {"e": 0.2, "p": 0.4, "o": 0.6, "c": 0.8,
               "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
        try:
            return CVT[card]
        except:
            return int(card)

    def think(self):
        Senses = [(self.chips / (pkr.bet + 1)) / 10]

        for i in range(len(self.HandCards)):
            Senses.append(self.HandCards[i][0])
            Senses.append(self.Card2int(self.HandCards[i][1]))
        for i in range(len(pkr.TableCards)):
            Senses.append(pkr.TableCards[i][0])
            Senses.append(self.Card2int(pkr.TableCards[i][1]))
        while len(Senses) < 15:
            Senses.append(0)

        Brain = self.Brain.think(Senses)
        print("[AI debug info] VChips = %i" % Senses[0])
        print("[AI debug info] %i & %i" % (Brain[0], Brain[1]))
        
        if not Brain[0] + Brain[1]:
            self.Fold()
        elif Brain[0] + Brain[1] == 2:
            self.raisebet()
        else:
            self.paycheck()

        return


class Human_player(player):

    def __init__(self, name='zero'):
        player.__init__(self, name)

    def plays(self):

        strt = 0
        action = 0
        print("")

        print("your turn... you got %s and %s.\n" %
              (card[self.HandCards[0]], card[self.HandCards[1]]))
        print("also, you have " + str(self.chips) + " chips.\n")
        print("The pot is at " + str(pkr.pot) + " chips.\n")
        print("Current bet is " + str(pkr.bet) + " chips.\n")
        print("You have already bet %i chips this round.\n" % self.bet)
        self.options()
        print("")

    def options(self):
        Chk = "pay"
        if pkr.bet == self.bet:
            Chk = "check"
        Prompt = "do?... [fold/%s/raise/bet/look table]" % Chk
        action = 0
        Valid = ['fold', 'check', 'pay', 'raise', 'bet', 'look table']
        while not action in Valid:
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
        self.roundcount = 0

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

    def NewGame(self):
        self.__init__()

        global players
        players = []
        
        if not Automatic:
            players = [Human_player(name=input('Your name, sir?'))]
        while len(players) < NP:
            players.append(AI_player())
        
    def dealcard(self):
        x = randint(0, len(pkr.deck) - 1)
        _card = self.deck[x]
        del self.deck[x]

        return _card

    def deal2table(self):

        self.TableCards.append(self.dealcard())
        print("Dealer puts a %s in the table." % self.TableCards[-1])

    def peektable(self):
        print('You peek at the table;')
        for Card in self.TableCards:
            print('.. %s.' % card[Card])

    def gameloop(self):
        self.roundcount += 1
        prepare()
        deal()
        blind()
        while pkr.gamephase < 4:
            nextplayer()

            if pkr.lastbet == self.whoplays:
                change_gamephase()
            else:
                player_turn(self.whoplays)
                if not self.checkSurvival():
                    return
                
    def checkSurvival(self):

        Survivors = []
        for P in players:

            if not P.dead and not P.fold:
                Survivors.append(P)
        if len(Survivors) == 1:
            ## debug stuff:
            # print("*** checking survivors: True ***")
            # print(Survivors)
            # for P in players:
            #    print("player %s debug: Fold=%i;Dead=%i;Chips=%i" %
            #          (P.name,P.fold,P.dead,P.chips))
            endgame(Survivors)
            return 0
        else:
            return 1

def WaitInput():
    if Automatic:
        return
    else:
        input("")
NP = 4

Automatic = 0
if len(sys.argv) > 1:
    if not sys.argv[1] == '--automatic' and not sys.argv[1] == '-a':
        Automatic = 1
        
pkr = game()
pkr.NewGame()


if not Automatic:
    print("Welcome to the satanic poker table %s, %s." %
          (version, players[0].name))
    print("")
    print("You will be seated in a four-player NLHE tournament table.")
    WaitInput()
    print("And will end victorious if you can beat the AI before" +
          " they beat you. Have fun, and suffer.")
    WaitInput()
    print("")
    print("%s is in front of you, %s your left, and %s your right." %
          (players[1].name, players[2].name, players[3].name))
    print("")
    WaitInput()


print()

# card name content. 'e' stands for spades, 'p' for clubs, 'o' for
# diamonds, and 'c' for hearts...
ColorNames = {'e': 'Spades', 'p': 'Clubs',
              'o': 'Diamonds', 'c': 'Hearts'}
NumberNames = {'A': 'Ace', '2': 'Two', '3': 'Three', '4': 'Four',
               '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight',
               '9': 'Nine', 'T': 'Ten', 'J': 'Jack', 'Q': 'Queen',
               'K': 'King'}

card = {'eA': 'Ace of Spades', 'pA': 'Ace of Clubs',
        'oA': 'Ace of Diamonds', 'cA': 'Ace of Hearts',
        'eK': 'King of Spades', 'pK': 'King of Clubs',
        'oK': 'King of Diamonds', 'cK': 'King of Hearts',
        'eQ': 'Queen of Spades', 'pQ': 'Queen of Clubs',
        'oQ': 'Queen of Diamonds', 'cQ': 'Queen of Hearts',
        'eJ': 'Jack of Spades', 'pJ': 'Jack of Clubs',
        'oJ': 'Jack of Diamonds', 'cJ': 'Jack of Hearts',
        'eT': 'Ten of Spades', 'pT': 'Ten of Clubs',
        'oT': 'Ten of Diamonds', 'cT': 'Ten of Hearts',
        'e9': 'Nine of Spades', 'p9': 'Nine of Clubs',
        'o9': 'Nine of Diamonds', 'c9': 'Nine of Hearts',
        'e8': 'Eight of Spades', 'p8': 'Eight of Clubs',
        'o8': 'Eight of Diamonds', 'c8': 'Eight of Hearts',
        'e7': 'Seven of Spades', 'p7': 'Seven of Clubs',
        'o7': 'Seven of Diamonds', 'c7': 'Seven of Hearts',
        'e6': 'Six of Spades', 'p6': 'Six of Clubs',
        'o6': 'Six of Diamonds', 'c6': 'Six of Hearts',
        'e5': 'Five of Spades', 'p5': 'Five of Clubs',
        'o5': 'Five of Diamonds', 'c5': 'Five of Hearts',
        'e4': 'Four of Spades', 'p4': 'Four of Clubs',
        'o4': 'Four of Diamonds', 'c4': 'Four of Hearts',
        'e3': 'Three of Spades', 'p3': 'Three of Clubs',
        'o3': 'Three of Diamonds', 'c3': 'Three of Hearts',
        'e2': 'Two of Spades', 'p2': 'Two of Clubs',
        'o2': 'Two of Diamonds', 'c2': 'Two of Hearts'}

pot = 0

deck = None

def prepare():
    pkr.pot = 0

    print("* Starting round %i. *" % pkr.roundcount)
    print("")
    pkr.strt = 1

    pkr.startingRoundChips = []
    
        
    for player in players:
        pkr.startingRoundChips.append(player.chips)
        if player.chips <= 0:
            player.dead = 1

# function starts the round and deal the cards.
def deal():

    # deck generator. first char stands for color, and second for number.
    pkr.deck = ['eA', 'pA', 'oA', 'cA', 'eK', 'pK', 'oK', 'cK', 'eQ', 'pQ',
                'oQ', 'cQ', 'eJ', 'pJ', 'oJ', 'cJ', 'eT', 'pT', 'oT', 'cT',
                'e9', 'p9', 'o9', 'c9', 'e8', 'p8', 'o8', 'c8', 'e7', 'p7',
                'o7', 'c7', 'e6', 'p6', 'o6', 'c6', 'e5', 'p5', 'o5', 'c5',
                'e4', 'p4', 'o4', 'c4', 'e3', 'p3', 'o3', 'c3', 'e2', 'p2',
                'o2', 'c2']

    for player in players:
        player.fold = 0
        if not player.dead:
            print("dealing cards to %s" % player.name)
            for x in range(2):
                player.HandCards.append(pkr.dealcard())
                print(player.HandCards[x])

    pkr.gamephase = 0
    pkr.TableCards = []

    print("dealing...")
    if not Automatic:
        print("you got %s and %s." %
              (card[players[0].HandCards[0]], card[players[0].HandCards[1]]))
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
    if players[pkr.whoplays].dead:
        nextplayer()

def change_gamephase():
    survivors = []
    for p in players:
        p.bet = 0
    pkr.bet = 0
    pkr.lastbet = pkr.button

    phasenames = ['preflop', 'flop', 'turn', 'river']
    if not pkr.gamephase:
        x = 3
    else:
        x = 1
    pkr.gamephase += 1

    if pkr.gamephase > 3:
        conclusion()
        return
    print('Dealer deals the %s....' % phasenames[pkr.gamephase])
    for z in range(x):
        print("")
        pkr.TableCards.append(pkr.dealcard())
        print("%s in da table!" % card[pkr.TableCards[-1]])
        print("")
    WaitInput()

    pkr.start = 1

    pkr.whoplays = pkr.button
    nextplayer()

def conclusion():
    print("")
    print("*** checking player's hands ***")
    WaitInput()

    winner = []
    value = 0

    for player in players:
        if not player.fold and not player.dead:

            print(player.name + " got:")
            print("")
            for C in player.HandCards:
                print(card[C])

            print("")
            handvalue = checkhandvalue(player)
            try:
                handvalue = checkhandvalue(player)
            except:
                print("Where are the fucking cards?")
                print ("deck: %i cards" % len(pkr.deck))
                for P in players:
                    print ("%s; dead? %i" %  (P.name,P.dead))
                    for C in P.HandCards:
                        print(card[C])
                exit()
            print(comment)
            print("")

            if handvalue > value:
                winner = [player]
                value = handvalue

            elif handvalue == value:
                winner.append(player)
    endgame(winner)

def endgame(winner):
    print("")

    if len(winner) == 1:
        print(winner[0].name + " wins " + str(pkr.pot) + " chips.")
        winner[0].chips += pkr.pot

    elif len(winner) > 1:
        print("splitpot! " + str(pkr.pot / len(winner)) + " for each.")
        for i in range(0, len(winner)):
            print(winner[i].name)
            winner[i].chips += pkr.pot / len(winner)

    for p in range(len(players)):
        if players[p].Brain:
            players[p].Brain.feedback(players[p].chips-pkr.startingRoundChips[p], 0)
            
    pkr.pot = 0
    pkr.TableCards = []
    for player in players:
        player.HandCards = []

    print("")
    print("")
    WaitInput()

    if not Automatic and players[0].chips <= 0:
        print("")
        print("Game Over. You lose at round %i." % pkr.roundcount)
        while True:
            WaitInput()
    Go = []
    for player in players:
        player.fold = 0
        if not player.dead and not player.chips < 0:
            Go.append(player)

    if len(Go) == 1:
        print("")
        for P in players:
            if P.Brain:
                if P in Go:
                    P.Brain.finalFeedback(1)
                else:
                    P.Brain.finalFeedback(0)
        print("Game Over. %s wins at round %i." % (Go[0].name,
                                                   pkr.roundcount))
        time.sleep(10)
        pkr.NewGame()
        

def setprematureend():
    print('Game ends now!')

    if pkr.gamephase == 0:
        for i in range(5):
            pkr.deal2table()
        conclusion()
    elif pkr.gamephase == 1:
        for i in range(2):
            pkr.deal2table()
        conclusion()
    elif pkr.gamephase == 2:
        pkr.deal2table()
        conclusion()
    elif pkr.gamephase == 3:
        conclusion()


# AI-related hand value speculation routines, one for each of the game phases

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

    if h[0] == hh[0]:  # if got pair of same color
        handvalue += 40
    elif h[1] == hh[1]:  # if got pair of same number
        handvalue += 30

    return handvalue


def checkhandflop(h, hh, t, tt, ttt):
    handvalue = 0

    n = h[0] + hh[0] + t[0] + tt[0] + ttt[0]
    e = 0
    p = 0
    o = 0
    c = 0
    for i in range(len(n)):
        if n[i] == "e":
            e += 1
        elif n[i] == "p":
            p += 1
        elif n[i] == "o":
            o += 1
        elif n[i] == "c":
            c += 1

    if (c == 3) or (p == 3) or (o == 3) or (c == 3):
        handvalue += 15

    m = h[1] + hh[1] + t[1] + tt[1] + ttt[1]

    i2 = 0
    i3 = 0
    i4 = 0
    i5 = 0
    i6 = 0
    i7 = 0
    i8 = 0
    i9 = 0
    T = 0
    J = 0
    Q = 0
    K = 0
    A = 0

    for i in range(len(m)):
        if m[i] == 'i2':
            i2 += 1
        if m[i] == 'i3':
            i3 += 1
        if m[i] == 'i4':
            i4 += 1
        if m[i] == 'i5':
            i5 += 1
        if m[i] == 'i6':
            i6 += 1
        if m[i] == 'i7':
            i7 += 1
        if m[i] == 'i8':
            i8 += 1
        if m[i] == 'i9':
            i9 += 1
        if m[i] == 'T':
            T += 1
        if m[i] == 'J':
            J += 1
        if m[i] == 'Q':
            Q += 1
        if m[i] == 'K':
            K += 1
        if m[i] == 'A':
            A += 1

    ms = str(i2) + str(i3) + str(i4) + str(i5) + str(i6) + str(i7) + \
        str(i8) + str(i9) + str(T) + str(J) + str(Q) + str(K) + str(A)
    if "3" in ms:
        handvalue += 20
    if "2" in ms:
        handvalue += 10

    handvalue = randint(0, 15)
    return handvalue


def checkhandturn(h, hh, t, tt, ttt, tu):
    handvalue = 0

    n = h[0] + hh[0] + t[0] + tt[0] + ttt[0] + tu[0]
    e = 0
    p = 0
    o = 0
    c = 0
    for i in range(len(n)):
        if n[i] == "e":
            e += 1
        elif n[i] == "p":
            p += 1
        elif n[i] == "o":
            o += 1
        elif n[i] == "c":
            c += 1

    if (c == 3) or (p == 3) or (o == 3) or (c == 3):
        handvalue += 15

    m = h[1] + hh[1] + t[1] + tt[1] + ttt[1] + tu[1]

    i2 = 0
    i3 = 0
    i4 = 0
    i5 = 0
    i6 = 0
    i7 = 0
    i8 = 0
    i9 = 0
    T = 0
    J = 0
    Q = 0
    K = 0
    A = 0

    for i in range(len(m)):
        if m[i] == 'i2':
            i2 += 1
        if m[i] == 'i3':
            i3 += 1
        if m[i] == 'i4':
            i4 += 1
        if m[i] == 'i5':
            i5 += 1
        if m[i] == 'i6':
            i6 += 1
        if m[i] == 'i7':
            i7 += 1
        if m[i] == 'i8':
            i8 += 1
        if m[i] == 'i9':
            i9 += 1
        if m[i] == 'T':
            T += 1
        if m[i] == 'J':
            J += 1
        if m[i] == 'Q':
            Q += 1
        if m[i] == 'K':
            K += 1
        if m[i] == 'A':
            A += 1

    ms = str(i2) + str(i3) + str(i4) + str(i5) + str(i6) + str(i7) + \
        str(i8) + str(i9) + str(T) + str(J) + str(Q) + str(K) + str(A)
    if "3" in ms:
        handvalue += 20
    if "2" in ms:
        handvalue += 10

    handvalue = randint(0, 15)
    return handvalue


def checkhandriver(h, hh, t, tt, ttt, tu, riv):

    handvalue = 0

    n = h[0] + hh[0] + t[0] + tt[0] + ttt[0] + tu[0] + riv[0]
    e = 0
    p = 0
    o = 0
    c = 0
    for i in range(len(n)):
        if n[i] == "e":
            e += 1
        elif n[i] == "p":
            p += 1
        elif n[i] == "o":
            o += 1
        elif n[i] == "c":
            c += 1

    if (c == 3) or (p == 3) or (o == 3) or (c == 3):
        handvalue += 15

    m = h[1] + hh[1] + t[1] + tt[1] + ttt[1] + tu[1] + riv[1]

    i2 = 0
    i3 = 0
    i4 = 0
    i5 = 0
    i6 = 0
    i7 = 0
    i8 = 0
    i9 = 0
    T = 0
    J = 0
    Q = 0
    K = 0
    A = 0

    for i in range(len(m)):
        if m[i] == 'i2':
            i2 += 1
        if m[i] == 'i3':
            i3 += 1
        if m[i] == 'i4':
            i4 += 1
        if m[i] == 'i5':
            i5 += 1
        if m[i] == 'i6':
            i6 += 1
        if m[i] == 'i7':
            i7 += 1
        if m[i] == 'i8':
            i8 += 1
        if m[i] == 'i9':
            i9 += 1
        if m[i] == 'T':
            T += 1
        if m[i] == 'J':
            J += 1
        if m[i] == 'Q':
            Q += 1
        if m[i] == 'K':
            K += 1
        if m[i] == 'A':
            A += 1

    ms = str(i2) + str(i3) + str(i4) + str(i5) + str(i6) + str(i7) + \
        str(i8) + str(i9) + str(T) + str(J) + str(Q) + str(K) + str(A)
    if "3" in ms:
        handvalue += 20
    if "2" in ms:
        handvalue += 10

    handvalue = randint(0, 15)
    return handvalue

def blind():

    pkr.whoplays = pkr.button
    print(pkr.button)

    nextplayer()
    pkr.button = pkr.whoplays

    print("")
    print(players[pkr.whoplays].name + " is the dealer.")
    print("")
    nextplayer()
    print(players[pkr.whoplays].name + " pays " +
          str(pkr.minimum / 2) + " chips.")

    pkr.pot += pkr.minimum / 2

    players[pkr.whoplays].chips -= pkr.minimum / 2
    players[pkr.whoplays].bet = pkr.minimum / 2

    nextplayer()

    print(players[pkr.whoplays].name + " pays " +
          str(pkr.minimum) + " chips.\n")

    pkr.pot += pkr.minimum
    pkr.bet = pkr.minimum

    players[pkr.whoplays].chips -= pkr.minimum
    players[pkr.whoplays].bet = pkr.minimum

    pkr.lastbet = pkr.whoplays
    WaitInput()

def folds(player):

    print(player.name + " folds.")
    player.fold = 1


def checkhandvalue(player):
    global comment
    comment = "Nothing."

    a = player.HandCards[0]
    b = player.HandCards[1]
    pname = player.name

    handvalue = 0

    GOTflush = 0
    GOTsequence = 0
    GOTstraightflush = 0

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

    pos2 = 0

    poscard = {0: 'A', 1: 'K', 2: 'Q', 3: 'J', 4: 'T', 5: '9',
               6: '8', 7: '7', 8: '6', 9: '5', 10: '4', 11: '3', 12: '2'}
    antiposcard = dict((value, key) for key, value in poscard.items())

    if antiposcard[a[1]] <= antiposcard[b[1]]:
        hc = a
        lc = b
    else:
        hc = b
        lc = a

    xit = str(n2) + str(n3) + str(n4) + str(n5) + str(n6) + str(n7) + \
        str(n8) + str(n9) + str(T) + str(J) + str(Q) + str(K) + str(A)
    xit = xit[::-1]

    NumberSequence = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T',
                      'J', 'Q', 'K', 'A']

    # check for sequences on cardpool.
    for N in range(len(NumberSequence) - 5):
        CandidateSequence = ""
        for x in range(5):
            CandidateSequence += NumberSequence[N + x]

        if containsAll(unumbers, CandidateSequence):
            GOTsequence = "%s%s" % (NumberSequence[N], NumberSequence[N+5])


    # check for flushs on cardpool.
    Color = {0: "c", 1: "p", 2: "s", 3: "o"}
    Carray = [c,p,s,o]
    for i in range(len(Carray)):
        if Carray[i] > 4:
            GOTflush = Color[i]

    # check for straight flush on cardpool.
    if GOTflush and GOTsequence:
        SFRequiredCards = []
        for C in range(NumberSequence.index(GOTsequence[0]),
                       NumberSequence.index(GOTsequence[1])):
            SFRequiredCards.append("%s%s" % (GOTflush,NumberSequence[C]))

        if set(SFRequiredCards).issubset(set(cardpool)):
            GOTstraightflush = GOTflush+GOTsequence


    if GOTstraightflush:
        comment = "Straight flush! %s to %s, of %s." % (NumberNames[GOTsequence[0]],
                                                        NumberNames[GOTsequence[1]],
                                                        ColorNames[GOTflush])
        handvalue = 1800 + NumberSequence.index(GOTsequence[0]) * 10

    elif "4" in xit:

        pos = xit.index('4')
        comment = "Quartet of " + poscard[pos] + "'s."

        handvalue = 1600
        deuce = 13 - pos
        handvalue += deuce

    elif ("3" in xit) and ("2"in xit):
        pos = xit.index('3')
        pos2 = xit.index('2')

        comment = "full house... " + \
            poscard[pos] + " 's, and " + poscard[pos2] + " 's."
        handvalue = 800
        deuce = 80 - 2 * pos
        handvalue += deuce
        deuce = 13 - pos2
        handvalue += deuce

    elif GOTflush:
        comment = "Flush of %s" % ColorNames[GOTflush]
        handvalue += 1000

    elif GOTsequence:
        comment = "Sequence... %s to %s" % (NumberNames[GOTsequence[0]],
                                            NumberNames[GOTsequence[1]])
        handvalue = 510 + NumberSequence.index(GOTsequence[0]) * 10


    elif "3" in xit:
        pos = xit.index('3')

        comment = "Trio"
        handvalue = 400
        deuce = 13 - pos
        handvalue += deuce

    elif "2" in xit:

        pos = xit.index('2')

        if "2" in xit[pos + 1:12]:
            pos2 = xit[pos + 1:12].index('2') + pos + 1

            handvalue = 360
            deuce = -13 * pos
            handvalue += deuce

            comment = "Two pairs... " + \
                poscard[pos] + "'s and " + poscard[pos2] + "'s ."

            if (pos != antiposcard[hc[1]]) and (pos2 != antiposcard[hc[1]]):
                comment += "Kicker: " + hc[1]
                handvalue += 13 - antiposcard[hc[1]]

            elif (pos != antiposcard[lc[1]]) and (pos2 != antiposcard[lc[1]]):
                comment += "Kicker: " + lc[1]
                handvalue += 13 - antiposcard[lc[1]]

        else:

            handvalue = 180
            deuce = -13 * pos
            handvalue += deuce

            comment = "Pair of " + poscard[pos] + "'s."

            if pos != antiposcard[hc[1]]:
                comment += " Kicker: " + hc[1]
                handvalue += 13 - antiposcard[hc[1]]

            elif pos != antiposcard[lc[1]]:
                comment += " Kicker: " + lc[1]
                handvalue += 13 - antiposcard[lc[1]]

    else:

        handvalue = 13 - antiposcard[hc[1]]
        comment = "High Card " + hc[1]

    return handvalue


def containsAll(str, set):
    return 0 not in [c in str for c in set]

while True:
    pkr.gameloop()
