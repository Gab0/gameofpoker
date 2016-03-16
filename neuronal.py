#!/usr/bin/python

#import mlxtend.classifier import NeuralNetMLP
import random

class neuron():
    def __init__(self,threshold):
        self.Input = []
        self.Output = 0

        self.Threshold = threshold

    def process(self):
        SUM = 0
        for v in self.Input: SUM +=v
        
        if SUM > self.Threshold:
            self.Output = SUM
        else:
            self.Output = 0
    def compare(self):
        R=0
        ValidSize=0
        for i in range(len(self.Input)):
            if not self.Input[i]:
                continue
            ValidSize+=1
            if self.Input[i] in self.Input[:i]+self.Input[i+1:]:
                R+=1
                
        if ValidSize: self.Output += R/ValidSize
                
        
class synapse():
    def __init__(self,weight,From,To):
        self.weight = weight

        self.From = From
        self.To = To

    def connect(self):
        self.To.Input.append(self.From.Output * self.weight)

def setSynapses(layer_from,layer_to,FIXED):
    S = []
    X = 1
    for F in range(len(layer_from)):
        for T in range(len(layer_to)):
            if not FIXED:
                X=random.random()
            S.append(synapse(X,layer_from[F],layer_to[T]))    
    return S

def think(IN):
    #setup.
    Li = []
    for i in range(len(IN)): Li.append(neuron(random.randrange(3)))
    
    L1 = []
    for i in range(23): L1.append(neuron(random.randrange(3)))

    Lo = []
    for i in range(2): Lo.append(neuron(random.randrange(3)))

    
    Si1 = setSynapses(Li,L1,1)

    S1o = setSynapses(L1,Lo,0)


    #action.
    for I in range(len(IN)):
        Li[I].Input = IN
        Li[I].process()
        Li[I].compare()

    for I in range(len(Si1)):
        Si1[I].connect()

    for I in range(len(L1)):
        L1[I].process()

    for I in range(len(S1o)):
        S1o[I].connect()
        
    result = []
    for I in range(len(Lo)):
        Lo[I].process()
        result.append(Lo[I].Output)

    return result




#print(think([0,0,0,0,0,0,0,0,0,0,0]))
