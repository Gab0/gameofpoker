#python script
from random import randint
import operator

names = ['Freddie', 'Suzanne', 'Wellington', 'Roberts', 'Spacely', 'John', 'Ruanito', 'Chavez', 'Wilson', 'Ford', 'Nikolai', 'Samara', 'Fernandita', 'Nikki', 'Andersen', 'Magda']



class player:

    def __init__(self, name = 'AI'):
        self.chips = 1500
        self.bet = 0

        if name == 'AI':
            x = randint(0, len(names)-1)
            self.name = names[x]
            del names[x]
            
        else:
            self.name = name
        
        self.dead = 0
        
        self.h1 = None
        self.h2 = None

        self.fold = 0

        order.append(self)


class game:

    def __init__(self):
        self.pot = None
        self.bet = None
        self.minimum = 20
        self.button = order[randint(0, len(order)-1)]
        self.deck = None

        self.f1 = None
        self.f2 = None
        self.f3 = None
        self.trn = None
        self.riv = None
        




order = []


south = player(name = raw_input('Your name, sir?'))
sp = south


west = player()
wp = west


north = player()
np = north

east = player()
ep = east



pkr = game()



print "Welcome to satanic poker table, "+sp.name+"."
print ""
print "You will be seated in a four-player NLHE tournament table."
raw_input("")
print "And will end victorious if you can beat the AI before they beat you. Have fun, and suffer."
raw_input("")
print ""
print np.name + " is in front of you, " + wp.name + " at your left, and " + ep.name + " at your right."
print ""
raw_input("")


print 

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



lastbet = 0




# function starts the round and deal the cards.
def deal():
    
    # deck generator. first char [0] stands for color, and second [1] for number.    
    pkr.deck = ['eA', 'pA', 'oA', 'cA', 'eK', 'pK', 'oK', 'cK', 'eQ', 'pQ', 'oQ', 'cQ', 'eJ', 'pJ', 'oJ', 'cJ', 'eT', 'pT', 'oT', 'cT', 'e9', 'p9', 'o9', 'c9', 'e8', 'p8', 'o8', 'c8', 'e7', 'p7', 'o7', 'c7', 'e6', 'p6', 'o6', 'c6', 'e5', 'p5', 'o5', 'c5', 'e4', 'p4', 'o4', 'c4', 'e3', 'p3', 'o3', 'c3', 'e2', 'p2', 'o2', 'c2']


    for i in range(0, len(order)):

        if order[i].dead == 0:
            order[i].h1 = dealcard()
            order[i].h2 = dealcard()


    

    reset_folds()


    global gamephase
    gamephase = "preflop"
    
    print "dealing..."

    print "you got " + card[sp.h1] + " and " + card[sp.h2] + "."
    print ""



def player_turn(player):
    if lastbet == player:
        nextphase()
    if player.chips <= 0:
        nexturn()

    if player.fold == 1:
        nexturn()



    
    if player == sp:
        
        strt = 0 
        action = 0
        print ""
        
        print "your turn... you got " + card[sp.h1] + " and " + card[sp.h2] + ".\n"
        print "also, you have " + str(sp.chips) + " chips.\n"
        print "The pot is at " +str(pkr.pot)+ " chips.\n"
        print "Current bet is "+str(pkr.bet)+" chips.\n"
        print "You have already bet "+str(sp.bet)+" chips this round.\n"
        action = raw_input("do?... [fold/check/pay/raise/bet/look table]")
        while not (action == "fold") and not(action =="check") and not (action=="pay") and not (action=="raise") and not (action=="bet") and not (action=="look table"):
            action = raw_input("do?... [fold/check/pay/raise/bet/look table]")


        else:
            
            options(action)
        print ""


    else:

  


        strt = 0 

        print player.name + "'s turn... he got " + str(player.chips) + " chips."
        print "thinking"

        if gamephase == "preflop":
            
            AI_preflop(player)

        elif gamephase == "flop":

            AI_flop(player)

        elif gamephase == "turn":

            AI_turn(player)

        elif gamephase == "river":

            AI_river(player)

        raw_input("")
        nexturn()

    

def jumporder():
    
    global order 
    x = order[-1]
    
    order[-1] = order[0]

    if len(order) > 2:
        
        for i in range(0, len(order)-2):
            order[i] = order[i+1]
        
        order[-2] = x

    else:

       order[1] = x




    




def nexturn():

    
    jumporder()

    #lastbet = pkr.button  
    player_turn(order[0])


  


def flop():

    pkr.f1 = dealcard()

    pkr.f2 = dealcard()

    pkr.f3 = dealcard()


    global lastbet


    print 'The dealer deals the flop....'
    print ""
    print "It's a " + card[pkr.f1] + ", a " + card[pkr.f2] + ", and a fucking " + card[pkr.f3] + "!!!"
    print ""
    raw_input("")

    global gamephase
    gamephase = "flop"
    global strt
    strt = 1
    
    while not order[0] == pkr.button:
        jumporder()

    jumporder()
    lastbet = pkr.button

    nexturn()   

#draw the turn card and puts it in table, calls the player turn, of who is after the button.
def turn():
    global deck
    global trn
    pkr.trn = dealcard()

    global lastbet


    print "The dealer deals the turn..."
    print ""
    print "It's a "+card[pkr.trn]+"... kewl."
    print ""
    raw_input("")

    global gamephase
    gamephase = "turn"
    global strt
    strt = 1

    while not order[0] == pkr.button:
        jumporder()

    jumporder()
    lastbet = pkr.button

    nexturn()




def river():

    pkr.riv = dealcard()

    global lastbet


    print "The dealer deals the river..."
    print ""
    print "It's a "+card[pkr.riv]+"... it's ok."
    print ""
    raw_input("")
    
    global gamephase
    gamephase = "river"
    global strt
    strt = 1

    while not order[0] == pkr.button:
        jumporder()

    jumporder()
    lastbet = pkr.button


    nexturn()

def conclusion():
    print ""
    print "*** checking player's hands ***"
    raw_input("")

    winner = []
    value = 0

    
    for i in range(0, len(order)):
        if order[i].fold == 0:

            print order[i].name+" got:"
            print ""
            print card[order[i].h1]
            print card[order[i].h2]
            print ""
            handvalue = checkhandvalue(order[i])


            print comment
            print ""

            if handvalue > value:
                winner = [i]
                value = handvalue
                
            elif handvalue == value:
                winner.append(i)
                
            
         
           


    print ""
    

    if len(winner) == 1:

        print order[winner[0]].name+" wins "+str(pkr.pot)+" chips."
        order[winner[0]].chips += pkr.pot




    elif len(winner) > 1:
        print "splitpot! " + str(pkr.pot/len(winner))+ " for each."
        for i in range(0, len(winner)):
            print order[winner[i]].name
            order[winner[i]].chips += pkr.pot/len(winner)

            
            
    pkr.pot = 0


    print ""
    print ""
    raw_input("")


    if sp.chips <= 0:
        print ""
        print "Game Over."
        while schips <= 0:
            raw_input("")
    blind()

    

    

    
#function called when players raise the bet. 's' stands for you, 'w' is the player on the left, 'n' in front, 'e' is on the right.
def raisebet(player):
    global lastbet

 

    plastbet = 4
    pname = player.name
    pbet = player.bet

    pchips = player.chips


    if pchips > pkr.bet-pbet:
        
        lastbet = plastbet
        pkr.bet += pkr.minimum
        pkr.pot += (pkr.bet-pbet)
        pchips -=(pkr.bet-pbet)
        pbet = pkr.bet
        print pname+" raises to "+str(pkr.bet)+" chips."
        print ""


    elif pchips <= pkr.bet-pbet:

        lastbet = plastbet
        pkr.pot += pchips
        pkr.bet += pchips
        pbet += pchips
        pchips = 0
        print ""
        print pname+" raises to ALL IN! ["+str(pkr.bet)+"]."

    
    
    player.chips = pchips
    player.bet = pbet
    lastbet = player
        
       
def paycheck(player):


    pchips=player.chips
    pbet=player.bet
    pname=player.name


    if (pkr.bet-player.bet) > player.chips:

        pkr.pot += pplayer.chips
        player.chips=0
        print ""
        print player.name+" goes ALL IN!"
        print ""
        

        
    
    elif pkr.bet > pbet:
            pchips -= (pkr.bet-pbet)
            pkr.pot += (pkr.bet-pbet)
        
            print pname+" pays "+str(pkr.bet-pbet)+" chips.\n"
            pbet = pkr.bet

    elif pkr.bet == pbet:
            print pname+" checks.\n"


    player.chips = pchips
    player.bet = pbet


def nextphase():
    outs = 0
    for i in range(len(order)):

        outs += order[i].fold
        
        if order[i].chips <= 0:
            outs +=1


    if outs + 1 == len(order):
        print ""
        setprematureend()

        
    pkr.bet = 0
    for i in range(len(order)):
        order[i].bet = 0

    
    if gamephase == "preflop":
                flop()
    elif gamephase == "flop":
                turn()
    elif gamephase == "turn":
                river()
    elif gamephase == "river":
                conclusion()

def setprematureend():


    if gamephase == "preflop":
                dealcard("flp1")
                dealcard("flp2")
                dealcard("flp3")
                print ""
                print "Dealer deals the flop: "+card[flp1]+", "+card[flp2]+" and "+card[flp3]+"."
                raw_input("")
                dealcard("trn")
                print ""
                print "Dealer deals the turn: "+card[trn]+"."
                raw_input("")
                dealcard("riv")
                print ""
                print "Dealer deals the river: "+card[riv]+"."
                raw_input("")
                conclusion()
    elif gamephase == "flop":
                dealcard("trn")
                print ""
                print "Dealer deals the turn: "+card[trn]+"."
                raw_input("")
                dealcard("riv")
                print ""
                print "Dealer deals the river: "+card[riv]+"."
                raw_input("")
                conclusion()
    elif gamephase == "turn":
                dealcard("riv")
                print ""
                print "Dealer deals the river: "+card[riv]+"."
                raw_input("")
                conclusion()
    elif gamephase == "river":
                conclusion()
    


#function containing player options at his turn
    
def options(action):


        
        if action == "check":
            if pkr.bet <= sp.bet:
                print "You check."
                print ""
                nexturn()
            else:
                print "you can't check as there is a bet. fold or pay"
                action = 0
                while not (action == "fold") and not(action =="check") and not (action=="pay") and not (action=="raise") and not (action=="bet") and not (action=="look table"):
                    action = raw_input("do?... [fold/check/pay/raise/bet/look table]")
                else:
                    options(action)



        elif action == "pay":
            print ""
            paycheck(sp)
            
            
            nexturn()


        elif action == "fold":
                sp.fold = 1
                print "you fold."
                print ""
                nexturn()

        elif action == "raise":
                print ""
                raisebet(sp)
                nexturn()

        elif action == "look table":
                if gamephase == "preflop":
                    print "There is nothing to look."

                elif gamephase == "flop":
                    print "The flop is: "+card[pkr.f1]+", "+card[pkr.f2]+" and "+card[pkr.f3]+"."

                elif gamephase == "turn":
                    print "Flop and turn: "+card[pkr.f1]+", "+card[pkr.f2]+" and "+card[pkr.f3]+card[pkr.trn]+"."

                elif gamephase == "river":
                    print "Five cards on table: "+card[pkr.f1]+", "+card[pkr.f2]+", "+card[pkr.f3]+card[pkr.trn]+" and "+card[pkr.riv]+"."

                nexturn()

        elif action == "bet":
                print ""
                cash = raw_input("Put away the whisky... how many chips?")
                while cash.isdigit() is not True:
                    cash = raw_input("Put away the whisky... how many chips?")

                
                freebet(sp, cash)
                
                nexturn()



def freebet(player, cash):
    global lastbet


    cash = int(cash)

    if pkr.bet - player.bet + cash < player.chips:
        player.chips -= pkr.bet-player.bet+cash
        pkr.pot += pkr.bet - player.bet+  cash
        player.bet = cash+bet
        pkr.bet = player.bet
        print ""
        print player.name+" bets "+str(pkr.bet-player.bet+cash)+" chips!"
        print ""

    else:

        pkr.bet = player.bet + player.chips
        player.chips = 0
        player.bet = pkr.bet
        print ""
        print player.name+" goes ALL IN!"
        print ""

    lastbet = player
            
            
        
            
            
    

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




def blind():

    pkr.pot = 0

    

    global strt
    strt=1



    for i in range(len(order)-1):
        if order[i].chips <= 0:
            order[i].dead = 1
            del order[i]



    deal()
    
    while not order[0] == pkr.button:
        jumporder()




    jumporder()
    pkr.button = order[0]


    print ""
    print order[0].name+" is the dealer."
    print ""
    jumporder()
    print order[0].name + " pays " + str(pkr.minimum/2) + " chips."
    
    pkr.pot += pkr.minimum/2
    
    order[0].chips -= pkr.minimum/2
    order[0].bet = pkr.minimum/2

    jumporder()

    print order[0].name + " pays " + str(pkr.minimum) + " chips.\n"
    
    pkr.pot += pkr.minimum
    pkr.bet = pkr.minimum
    
    order[0].chips -= pkr.minimum
    order[0].bet = pkr.minimum
    
    lastbet= order[0]
    raw_input("")

    
    nexturn()



def AI_preflop(player):
        h1 = player.h1
        h2 = player.h2
        pname = player.name
        foldz = player.fold
        pbet = player.bet



        handvalue = checkhandpreflop(h1, h2)
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
        


        handvalue = checkhandflop(h1, h2, pkr.f1, pkr.f2, pkr.f3)
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

        handvalue = checkhandturn(h1, h2, pkr.f1, pkr.f2, pkr.f3, pkr.trn)
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

        handvalue = checkhandriver(h1, h2, pkr.f1, pkr.f2, pkr.f3, pkr.trn, pkr.riv)
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
    

            print player.name+" folds."
            player.fold = 1


def checkhandvalue(player):
        global comment
        comment = "Nothing."

        a = player.h1
        b = player.h2
        pname = player.name


        handvalue = 0
        
        game = a+b+pkr.f1+pkr.f2+pkr.f3+pkr.trn+pkr.riv
        colors = a[0]+b[0]+pkr.f1[0]+pkr.f2[0]+pkr.f3[0]+pkr.trn[0]+pkr.riv[0]
        numbers = a[1]+b[1]+pkr.f1[1]+pkr.f2[1]+pkr.f3[1]+pkr.trn[1]+pkr.riv[1]
        
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
        antiposcard=dict((value,key) for key,value in poscard.iteritems())

        
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
        


        
    print ""
    print pname+" wins "+pot+" chips."
    print ""

    blind()


def dealcard():
    x = randint(0,len(pkr.deck)-1)
    _card = pkr.deck[x]
    del pkr.deck[x]
    
    return _card

def reset_folds():

    for i in range(len(order)-1):
        order[i].fold = 0


               
    
blind()
