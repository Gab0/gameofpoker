#python script
from random import randint
import operator

names = ['Freddie', 'Suzanne', 'Wellington', 'Roberts', 'Spacely', 'John', 'Ruanito', 'Chavez', 'Wilson', 'Ford', 'Nikolai', 'Samara', 'Fernandita', 'Nikki', 'Andersen', 'Magda']

global ename
x = randint(0,len(names)-1)
ename = names[x]
del names[x]
global nname
x = randint(0,len(names)-1)
nname = names[x]
del names[x]
global wname
x = randint(0,len(names)-1)
wname = names[x]
del names[x]
global sname
sname = raw_input('Your name, sir?')


print "Welcome to satanic poker table."
print "You will be seated in a four-player NLHE tournament table."
raw_input("")
print "And will end victorious if you can beat the AI before they beat you. Have fun and suffer."
raw_input("")
print ""
print nname + " is in front of you, " + wname + " at your left, and " + ename + " at your right."
print ""
raw_input("")

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

bet = 0
chip = 0
minimum = 20


schips = 1500

nchips = 1500

wchips = 1500

echips = 1500

button = randint(1,4)

time = 0

pot = 0


deck="0"
sh1="0"
sh2="0"
eh1="0"
eh2="0"
nh1="0"
nh2="0"
nh2="0"



sbet=0
wbet=0
nbet=0
ebet=0

lastbet =0

ndead = 0
sdead = 0
edead = 0
wdead = 0


# function starts the round and deal the cards.
def deal():
    
    # deck generator. first char [0] stands for color, and second [1] for number.    
    global deck
    deck = ['eA', 'pA', 'oA', 'cA', 'eK', 'pK', 'oK', 'cK', 'eQ', 'pQ', 'oQ', 'cQ', 'eJ', 'pJ', 'oJ', 'cJ', 'eT', 'pT', 'oT', 'cT', 'e9', 'p9', 'o9', 'c9', 'e8', 'p8', 'o8', 'c8', 'e7', 'p7', 'o7', 'c7', 'e6', 'p6', 'o6', 'c6', 'e5', 'p5', 'o5', 'c5', 'e4', 'p4', 'o4', 'c4', 'e3', 'p3', 'o3', 'c3', 'e2', 'p2', 'o2', 'c2']

    if schips > 0:
        dealcard("sh1")
        dealcard("sh2")
        
    if nchips > 0:
        dealcard("nh1")
        dealcard("nh2")

    if echips > 0:
        dealcard("eh1")
        dealcard("eh2")

    if wchips > 0:
        dealcard("wh1")
        dealcard("wh2")

    

    global sfold
    sfold = 0
    global efold
    efold = 0
    global nfold
    nfold = 0
    global wfold
    wfold = 0



    global gamephase
    gamephase = "preflop"
    
    print "dealing..."

    print "you got " + card[sh1] + " and " + card[sh2] + "."
    print ""
    

    

def sturn():
    global sfold
    global strt
    global lastbet
    global schips
    
    if (lastbet == 1) and (strt==0):
            nextphase()

    if (sfold == 0) and (schips != 0):


        global pot
        global bet
        global sbet
        
  
        strt = 0 
        action = 0
        print ""
        
        print "your turn... you got " + card[sh1] + " and " + card[sh2] + ".\n"
        print "also, you have " + str(schips) + " chips.\n"
        print "The pot is at " +str(pot)+ " chips.\n"
        print "Current bet is "+str(bet)+" chips.\n"
        print "You have already bet "+str(sbet)+" chips this round.\n"
        action = raw_input("do?... [fold/check/pay/raise/bet/look table]")
        while not (action == "fold") and not(action =="check") and not (action=="pay") and not (action=="raise") and not (action=="bet") and not (action=="look table"):
            action = raw_input("do?... [fold/check/pay/raise/bet/look table]")


        else:
            
            options(action)
        print ""
    else:
        print ""
        wturn()


def eturn():
    global efold
    global strt
    global lastbet
    global echips

    global edead

    if (lastbet == 4) and (strt==0):
            nextphase()
#    elif (lastbet == 0) and (button == 4) and (strt == 0):
#            nextphase()
    if (efold == 0) and (echips != 0):

        global gamephase
        


        strt = 0 
        global minimum

        print ename + "'s turn... he got " + str(echips) + " chips."
        print "thinking"
        global pot
        global ebet
        
        
        global bet

        if gamephase == "preflop":
            
            AI_preflop("e")

        elif gamephase == "flop":

            AI_flop("e")

        elif gamephase == "turn":

            AI_turn("e")

        elif gamephase == "river":

            AI_river("e")

        raw_input("")
        sturn()

    else:
        sturn()
    
        
    
    

def nturn():
    global nfold
    global strt
    global lastbet
    global strt
    global ndead
    global nchips
    
    if (lastbet == 3) and (strt==0):
            nextphase()
#    elif (lastbet == 0) and (button == 3) and (strt == 0):
#            nextphase()
    if (nfold == 0) and (nchips != 0):

        global gamephase
       


        strt = 0     

        print nname + "'s turn... he got " + str(nchips) + " chips."
        print "their turn"
        global pot
        global nbet
        global bet
        
        global minimum
        
        if gamephase == "preflop":
            
            AI_preflop("n")

        elif gamephase == "flop":

            AI_flop("n")

        elif gamephase == "turn":

            AI_turn("n")

        elif gamephase == "river":

            AI_river("n")
            
        raw_input("")
        eturn()

    else:
        eturn()


def wturn():
    global wfold
    global strt
    global lastbet
    global strt
    global wdead
    global wchips
    
    if (lastbet == 2) and (strt==0):
            nextphase()
#    elif (lastbet == 0) and (button == 2) and (strt == 0):
#            nextphase()
    if (wfold == 0) and (wchips != 0):

        global gamephase



        strt = 0        

        print wname + "'s turn... he got " + str(wchips) + " chips."
        print "their turn"
        global pot
        global wbet
        global bet
        
        global minimum
        
        if gamephase == "preflop":

            AI_preflop("w")

        elif gamephase == "flop":

            AI_flop("w")

        elif gamephase == "turn":

            AI_turn("w")

        elif gamephase == "river":

            AI_river("w")
            
        raw_input("")
        nturn()

    else:
        nturn()

def flop():
    global deck
    global flp1
    global flp2
    global flp3
    dealcard("flp1")

    dealcard("flp2")

    dealcard("flp3")

    global bet
    bet = 0
    global wbet
    wbet = 0
    global nbet
    nbet = 0
    global ebet
    ebet = 0
    global sbet
    sbet = 0

    global lastbet


    print 'The dealer deals the flop....'
    print ""
    print "It's a " + card[flp1] + ", a " + card[flp2] + ", and a fucking " + card[flp3] + "!!!"
    print ""
    raw_input("")

    global gamephase
    gamephase = "flop"
    global strt
    strt = 1
    
    if button == 1:
        lastbet=2
        wturn()

    elif button == 2:
        lastbet=3
        nturn()

    elif button == 3:
        lastbet=4
        eturn()

    elif button == 4:
        lastbet=1
        sturn()


#draw the turn card and puts it in table, calls the player turn, of who is after the button.
def turn():
    global deck
    global trn
    dealcard("trn")
    global bet
    bet = 0
    global wbet
    wbet = 0
    global nbet
    nbet = 0
    global ebet
    ebet = 0
    global sbet
    sbet = 0

    global lastbet


    print "The dealer deals the turn..."
    print ""
    print "It's a "+card[trn]+"... kewl."
    print ""
    raw_input("")

    global gamephase
    gamephase = "turn"
    global strt
    strt = 1

    if button == 1:
        lastbet=2
        wturn()

    elif button == 2:
        lastbet=3
        nturn()
        
    elif button == 3:
        lastbet=4
        eturn()

    elif button == 4:
        lastbet=1
        sturn()


def river():
    global deck
    global riv
    dealcard("riv")

    global bet
    bet = 0
    global wbet
    wbet = 0
    global nbet
    nbet = 0
    global ebet
    ebet = 0
    global sbet
    sbet = 0

    global lastbet


    print "The dealer deals the river..."
    print ""
    print "It's a "+card[riv]+"... it's ok."
    print ""
    raw_input("")
    
    global gamephase
    gamephase = "river"
    global strt
    strt = 1

    if button == 1:
        lastbet=2
        wturn()

    elif button == 2:
        lastbet=3
        nturn()

    elif button == 3:
        lastbet=4
        eturn()

    elif button == 4:
        lastbet=1
        sturn()


def conclusion():
    print ""
    print "*** checking player's hands ***"
    raw_input("")
    shand = 0
    nhand = 0
    whand = 0
    ehand = 0

    if sfold == 0:
        print sname+" got:"
        handvalue = checkhandvalue("s")
        shand = handvalue
        
        print comment
        print ""

    if wfold == 0:
        print wname+" got:"
        handvalue = checkhandvalue("w")
        whand = handvalue

        print comment
        print ""
    
    if nfold == 0:
        print nname+" got:"
        handvalue = checkhandvalue("n")
        nhand = handvalue

        print comment
        print ""

    if efold == 0:
        print ename+" got:"
        handvalue = checkhandvalue("e")
        ehand = handvalue

        print comment


    results={"w": whand, "n": nhand, "e": ehand, "s": shand}

    print ""
    
    winners = ""
    winners += max(results.iteritems(), key=operator.itemgetter(1))[0]

    global echips
    global schips
    global nchips
    global wchips

    if len(winners) == 1:
        if winners == "w":
            print wname+" wins "+str(pot)+" chips."

            wchips += pot

        elif winners == "e":
            print ename+" wins "+str(pot)+" chips."

            echips+=pot

        elif winners == "n":
            print nname+" wins "+str(pot)+" chips."

            nchips += pot

        elif winners == "s":
            print sname+" wins "+str(pot)+" chips."

            schips+=pot

    elif len(winners) > 1:
        print "splitpot! " + pot/len(winners) + " for each."
        for i in range(0, len(winners)-1):
            if winners[i] == "w":
                print wname

                wchips += pot/len(winners)

            elif winners[i] == "e":
                print ename

                echips += pot/len(winners)

            elif winners[i] == "n":
                print nname

                nchips += pot/len(winners)

            elif winners[i] == "s":
                print sname

                schips += pot/len(winners)





    print ""
    print ""
    raw_input("")


    if schips <= 0:
        print ""
        print "Game Over."
        while schips <= 0:
            raw_input("")
    blind()

    

    

    
#function called when players raise the bet. 's' stands for you, 'w' is the player on the left, 'n' in front, 'e' is on the right.
def raisebet(player):
    global lastbet
    global bet
    global pot
    global minimum
    

    
    if player == "e":
        
        global ebet
        global echips
        plastbet = 4
        pname = ename
        pbet = ebet

        pchips = echips

    elif player == "w":
        
        global wbet
        global wchips
        plastbet = 2
        pname = wname
        pbet = wbet

        pchips = wchips

    elif player == "n":
        
        global nbet
        global nchips
        plastbet = 3
        pname = nname
        pbet = nbet

        pchips = nchips
        
    elif player == "s":
        
        global sbet       
        global schips
        plastbet = 1
        pname = sname
        pbet = sbet

        pchips = schips

    if pchips > bet-pbet:
        
        lastbet = plastbet
        bet += minimum
        pot += (bet-pbet)
        pchips -=(bet-pbet)
        pbet=bet
        afteraise(player, pchips, pbet)
        print pname+" raises to "+str(bet)+" chips."
        print ""


    elif pchips <= bet-pbet:

        lastbet = plastbet
        pot += pchips
        bet += pchips
        pbet += pchips
        pchips = 0
        print ""
        print pname+" raises to ALL IN! ["+str(bet)+"]."
        afteraise(player, pchips, pbet)
    
    

        

def afteraise(player, pchips, pbet):
    global bet
    global pot
    global minimum

    if player == "w":
        global wchips
        global wbet
        wchips = pchips
        wbet = pbet

    elif player == "n":
        global nchips
        global nbet
        nchips = pchips
        nbet = pbet

    elif player == "e":
        global echips
        global ebet
        echips = pchips
        ebet = pbet

    elif player == "s":
        global schips
        global sbet
        schips = pchips
        sbet = pbet

       
def paycheck(player):
    global bet
    global pot

    
    if player == "w":
        global wbet
        global wchips
        pchips=wchips
        pbet=wbet
        pname=wname

    if player == "n":
        global nbet
        global nchips
        pchips=nchips
        pbet=nbet
        pname=nname

    if player == "e":
        global ebet
        global echips
        pchips=echips
        pbet=ebet
        pname=ename

    if player == "s":
        global sbet
        global schips
        pchips=schips
        pbet=sbet
        pname=sname

    if (bet-pbet) > pchips:

        pot += pchips
        pchips=0
        print ""
        print pname+" goes ALL IN!"
        print ""
        

        
    
    elif bet > pbet:
            pchips -= (bet-pbet)
            pot += (bet-pbet)
        
            print pname+" pays "+str(bet-pbet)+" chips.\n"
            pbet = bet

    elif bet == pbet:
            print pname+" checks.\n"

    afterpaycheck(player, pchips, pbet)

def afterpaycheck(player, pchips, pbet):
    if player == "n":
        global nchips
        global nbet
        nchips = pchips
        nbet = pbet

    if player == "w":
        global wchips
        global wbet
        wchips = pchips
        wbet = pbet

    if player == "e":
        global echips
        global ebet
        echips = pchips
        ebet = pbet

    if player == "s":
        global schips
        global sbet
        schips = pchips
        sbet = pbet
        
def nextphase():

    if ((sfold == 1) or (schips <= 0)) and ((nfold == 1) or (nchips <= 0)) and ((wfold == 1) or (wchips <= 0)):
        print ""
        setprematureend()
    if ((efold == 1) or (echips <= 0)) and ((nfold == 1) or (nchips <= 0)) and ((wfold == 1) or (wchips <= 0)):
        print ""
        setprematureend()
    if ((sfold == 1) or (schips <= 0)) and ((efold == 1) or (echips <= 0)) and ((wfold == 1) or (wchips <= 0)):
        print ""
        setprematureend()
    if ((efold == 1) or (echips <= 0)) and ((nfold == 1) or (nchips <= 0)) and ((sfold == 1) or (schips <= 0)):
        print ""
        setprematureend()

        
    global gamephase
    
    if gamephase == "preflop":
                flop()
    elif gamephase == "flop":
                turn()
    elif gamephase == "turn":
                river()
    elif gamephase == "river":
                conclusion()

def setprematureend():

    global gamephase
    
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
        global schips
        global pot
        global bet
        global sbet
        
        if action == "check":
            if bet <= sbet:
                print "You check."
                print ""
                wturn()
            else:
                print "you can't check as there is a bet. fold or pay"
                action = 0
                while not (action == "fold") and not(action =="check") and not (action=="pay") and not (action=="raise") and not (action=="bet") and not (action=="look table"):
                    action = raw_input("do?... [fold/check/pay/raise/bet/look table]")
                else:
                    options(action)



        elif action == "pay":
            print ""
            paycheck("s")
            
            
            wturn()


        elif action == "fold":
                global sfold
                sfold = 1
                print "you fold"
                print ""
                wturn()

        elif action == "raise":
                print ""
                raisebet("s")
                wturn()

        elif action == "look table":
                if gamephase == "preflop":
                    print "There is nothing to look."

                elif gamephase == "flop":
                    print "The flop is: "+card[flp1]+", "+card[flp2]+" and "+card[flp3]+"."

                elif gamephase == "turn":
                    print "Flop and turn: "+card[flp1]+", "+card[flp2]+", "+card[flp3]+" and "+card[trn]+"."

                elif gamephase == "river":
                    print "Five cards on table: "+card[flp1]+", "+card[flp2]+", "+card[flp3]+", "+card[trn]+" and "

                sturn()

        elif action == "bet":
                print ""
                cash = raw_input("Put away the whisky... how many chips?")
                while cash.isdigit() is not True:
                    cash = raw_input("Put away the whisky... how many chips?")


                freebet("s", cash)

                wturn()



def freebet(player, cash):
    global lastbet
    global bet
    global pot
    if player == "s":
        global schips
        global sbet

        cash = int(cash)
        
        if bet-sbet+cash < schips:
            schips -= bet-sbet+cash
            pot += bet-sbet+cash
            sbet = cash+bet
            bet = sbet
            print ""
            print sname+" bets "+str(bet-sbet+cash)+" chips!"
            print ""

        else:

            bet = sbet + schips
            schips = 0
            sbet = bet
            print ""
            print sname+" goes ALL IN!"
            print ""

        lastbet = 1
            
            
        
            
            
    

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
    global bet
    global pot
    global schips
    global nchips
    global wchips
    global echips
    global lastbet
    global minimum
    global sbet
    global nbet
    global wbet
    global ebet
    pot = 0

    global button
    if button == 4:
        button = 1
    else:
        button +=1

    global strt
    strt=1

    bet = minimum

    deal()
    
    if button == 1:
        print ""
        print sname+" is the dealer."
        print ""
        print wname + " pays " + str(minimum/2) + " chips."
        
        pot += minimum/2
        
        wchips -= minimum/2
        wbet = minimum/2

        print nname + " pays " + str(minimum) + " chips.\n"
        
        pot += minimum
        
        nchips -= minimum
        nbet = minimum
        lastbet=4
        raw_input("")

        eturn()

    elif button ==2:
        print ""
        print wname+" is the dealer."
        print ""
        
        print nname + " pays " + str(minimum/2) + " chips."
        
        pot += minimum/2
        
        nchips -= minimum/2
        nbet = minimum/2

        print ename + " pays " + str(minimum) + " chips.\n"
        
        pot += minimum
        
        echips -= minimum
        ebet = minimum
        lastbet=1
        raw_input("")
        
        sturn()

    elif button ==3:
        print ""
        print nname+" is the dealer."
        print ""
        
        print ename + " pays " + str(minimum/2) + " chips."
        
        pot += minimum/2
        
        echips -= minimum/2
        ebet = minimum/2

        print sname + " pays " + str(minimum) + " chips.\n"
        
        pot += minimum
        
        schips -= minimum
        sbet = minimum
        lastbet=2
        raw_input("")
        
        wturn()

    elif button ==4:
        print ""
        print ename+" is the dealer."
        print ""
        
        print sname + " pays " + str(minimum/2) + " chips."
        
        pot += minimum/2
        
        schips -= minimum/2
        sbet = minimum/2

        print wname + " pays " + str(minimum) + " chips.\n"
        
        pot += minimum
        
        wchips -= minimum
        wbet = minimum
        lastbet=3
        raw_input("")

        nturn()

def AI_preflop(player):
        if player == "w":
            h1 = wh1
            h2 = wh2
            pname = wname
            foldz = wfold
            pbet = wbet

        elif player == "n":
            h1 = nh1
            h2 = nh2
            pname = nname
            foldz = nfold
            pbet = nbet

        elif player == "e":
            h1 = eh1
            h2 = eh2
            pname = ename
            foldz = efold
            pbet = ebet

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
        if player == "w":
            h1 = wh1
            h2 = wh2
            pname = wname
            foldz = wfold
            pbet = wbet

        elif player == "n":
            h1 = nh1
            h2 = nh2
            pname = nname
            foldz = nfold
            pbet = nbet

        elif player == "e":
            h1 = eh1
            h2 = eh2
            pname = ename
            foldz = efold
            pbet = ebet

        handvalue = checkhandflop(wh1, wh2, flp1, flp2, flp3)
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
        if player == "w":
            h1 = wh1
            h2 = wh2
            pname = wname
            foldz = wfold
            pbet = nbet

        elif player == "n":
            h1 = nh1
            h2 = nh2
            pname = nname
            foldz = nfold
            pbet = wbet

        elif player == "e":
            h1 = eh1
            h2 = eh2
            pname = ename
            foldz = efold
            pbet = ebet

        handvalue = checkhandturn(wh1, wh2, flp1, flp2, flp3, trn)
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
        if player == "w":
            h1 = wh1
            h2 = wh2
            pname = wname
            foldz = wfold
            pbet = wbet

        elif player == "n":
            h1 = nh1
            h2 = nh2
            pname = nname
            foldz = nfold
            pbet = nbet

        elif player == "e":
            h1 = eh1
            h2 = eh2
            pname = ename
            foldz = efold
            pbet = ebet

        handvalue = checkhandriver(wh1, wh2, flp1, flp2, flp3, trn, riv)
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
    
        if player == "w":
            global wfold
            print wname+" folds."
            wfold = 1

        elif player == "n":
            global nfold
            print nname+" folds."
            nfold = 1

        elif player == "e":
            global efold
            print ename+" folds."
            efold = 1

        elif player == "s":
            global sfold
            print sname+" folds."
            sfold = 1
            
def checkhandvalue(player):
        global comment
        comment = "Nothing."
        if player == "s":
                global sh2
                global sh1
                a = sh1
                b = sh2
                pname =sname
        elif player == "e":
                global eh1
                global eh2
                a = eh1
                b = eh2
                pname=ename
        elif player == "w":
                global wh1
                global wh2
                a = wh1
                b = wh2
                pname=wname
        elif player == "n":
                global nh1
                global nh2
                a = nh1
                b = nh2
                pname=nname

        handvalue = 0
        
        game = a+b+flp1+flp2+flp3+trn+riv
        colors = a[0]+b[0]+flp1[0]+flp2[0]+flp3[0]+trn[0]+riv[0]
        numbers = a[1]+b[1]+flp1[1]+flp2[1]+flp3[1]+trn[1]+riv[1]
        
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


def dealcard(target):
    global deck


    exec("x = randint(0,len(deck)-1)") in globals()
    exec(target+" = deck[x]") in globals()
    del deck[x]



               
    
blind()
