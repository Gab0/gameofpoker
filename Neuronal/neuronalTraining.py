#!/usr/bin/python
import random
import copy

def Card2int(card):
    CVT = {"e": 0.2, "p": 0.4, "o": 0.6, "c": 0.8,
           "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    try:
        return CVT[card]
    except:
        return int(card)

def progressBar(percent):
    bV = percent / 100 * 30
    bV = round(bV)

    HASH = bV * "#"
    VOID = (30 - bV) * " "

    bar = "[%s%s] %f%%" % (HASH, VOID, round(percent))
    print(bar)
        
def PreHeat(network, MaxRun, retries=166):
    Debug = 0
    
    DECK = ['eA', 'pA', 'oA', 'cA', 'eK', 'pK', 'oK', 'cK', 'eQ', 'pQ',
            'oQ', 'cQ', 'eJ', 'pJ', 'oJ', 'cJ', 'eT', 'pT', 'oT', 'cT',
            'e9', 'p9', 'o9', 'c9', 'e8', 'p8', 'o8', 'c8', 'e7', 'p7',
            'o7', 'c7', 'e6', 'p6', 'o6', 'c6', 'e5', 'p5', 'o5', 'c5',
            'e4', 'p4', 'o4', 'c4', 'e3', 'p3', 'o3', 'c3', 'e2', 'p2',
            'o2', 'c2']

    Phasenames = {0: "preflop", 1: "flop", 2: "turn", 3: "river"}
    RUNLENGHT = 40
    for R in range(MaxRun):
        RET = retries
        for GamePhase in range(4):
            if Debug:
                print("Training for %s of run %i;" %\
                      (Phasenames[GamePhase], R + 1))
            Again = 1
            while Again:
                if RET < 0:
                    print("Failed")
                    return 0
                Fold = 0
                Raise = 0
                Check = 0

                for K in range(RUNLENGHT):
                    uDECK = copy.deepcopy(DECK)
                    # print('>---%i' % len(uDECK))

                    CardPool = []
                    for I in range(2 + GamePhase):
                        x = random.randrange(0, len(uDECK))
                        CardPool.append(uDECK.pop(x))

                    Senses = [random.randint(55, 80) / 10]
                    for card in CardPool:
                        Senses.append(card[0])
                        Senses.append(Card2int(card[1]))

                    while len(Senses) < 15:
                        Senses.append(0)

                    Z = network.think(Senses)
                    Z = Z[0] + Z[1]
                    if Z > 1:
                        Raise += 1
                    elif Z == 1:
                        Check += 1
                    else:
                        Fold += 1

                X = RUNLENGHT // 4

                if not Raise > X and\
                   not Check > X * 2.6 and\
                   not Fold  > X * 1.9:
                    Again = 0

                else:
                    Again = 1

                    G = [Raise, Check, Fold]
                    FeedBack = -max(G)
                    if max(G) == RUNLENGHT:
                        FeedBack -= 400
                        RET -= 20
                    if max(G) < RUNLENGHT // 1.5:
                        FeedBack += 600
                    elif max(G) < RUNLENGHT/2:
                        FeedBack += 800

                    modifyOutput = 0

                       
                    if not Raise and not Fold:
                        modifyOutput = -2
                    elif not Raise:
                        modifyOutput = 1
                    elif not Fold:
                        modifyOutput = -1

                    elif Check > X * 1.2:
                        modifyOutput = -2
                    elif Fold < X // 5 and Fold < Raise:
                        modifyOutput = -1
                    elif Raise < X // 5 and Raise < Fold:
                        modifyOutput = 1
                    elif Check < X // 5:
                        modifyOutput = 2

                    RET -= 1
                    if Debug:
                        print ("(%i %i %i) (%i) GOING AGAIN [%i]; %i %i %i" % \
                              (X, X*1.3, X,
                               RET, modifyOutput, Raise, Check, Fold))
                    network.feedback(FeedBack, modifyOutput)
            RET += 85
            
            if Debug:
                print("Partial finish. %i %i %i" % (Raise, Check, Fold))
            else:
                progressBar((GamePhase+1 + 4*R)  / (MaxRun*4) * 100)
    if Debug:            
        print("PreHeat concluded.")
            
    return 1
