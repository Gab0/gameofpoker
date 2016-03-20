#!/usr/bin/python

#import mlxtend.classifier import NeuralNetMLP
import random
from neuronalIO import *
import os

stdThresholdSize = [11, 23, 2]
stdWeightSize = [(11, 23), (23, 2)]


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


def genWeights(size=stdWeightSize):
    #size example = [(3,6),(5,3)]
    Weights = []

    for I in range(len(size)):#number of synaptic layers.
        Layer = []
        for K in range(size[I][0]):#number of From instances.
            Layer.append([])
            for Z in range(size[I][1]):#number of To instances.
                Layer[K].append(random.random())
        Weights.append(Layer)
        
    return Weights

def genThresholds(MaxValue, size=stdThresholdSize):
    #size example = [3, 5, 6]
    Thresholds = []

    for I in range(len(size)):#number of Neuronal layers.
        Layer = []
        for K in range(size[I]):#size of layer.
            Layer.append(random.randrange(MaxValue))
        Thresholds.append(Layer)

    return Thresholds


def think(IN, Weights = genWeights(),
              Thresholds = genThresholds(7)):
    #As for the project is right now, with 11 inputs/23 hidden/2 outputs;
    #the Weights array is a [[[11*[23]],[[23*[2]]] array of
    #floats between 0 and 1.

    #the Thresholds array is [[*11*],[*23*],[*2*]]
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

def grabAbrain():
    files = os.listdir('brain')
    files.append("R")

    K = random.choice(files)

    if K == "R":
        W = genWeights()
        T = genThresholds(7)
    else:
        FromFile = load_brain(K)
        W = FromFile[0]
        T = FromFile[1]
    return [W,T]

    
