#!/usr/bin/python

from Neuronal.neuronal import SynapseDimension
from Neuronal.neuronal import NetworkSize

import random
def genWeights(size=SynapseDimension):
    # size example = [(3,6),(5,3)]
    Weights = []
    mu = 0.7
    sigma = 1

    for I in range(len(size)):  # number of synaptic layers.
        Layer = []
        for K in range(size[I][0]):  # number of From instances.
            Layer.append([])
            for Z in range(size[I][1]):  # number of To instances.
                Layer[K].append(random.gauss(mu, sigma))
        Weights.append(Layer)

    return Weights


def genThresholds(MinValue, MaxValue, size=NetworkSize):
    # size example = [3, 5, 6]
    Thresholds = []
    mu = 7
    sigma = 2
    
    for I in range(len(size)):  # number of Neuronal layers.
        Layer = []
        for K in range(size[I]):  # size of layer.
            Layer.append(random.gauss(mu, sigma))
        Thresholds.append(Layer)

    return Thresholds

def genBias(sizeof, MinValue, MaxValue):
    BIAS = []

    for z in range(sizeof):
        BIAS.append(random.uniform(MinValue, MaxValue))
    
    return BIAS

def genName():
    
    n = random.randrange(0,1003008)
    return str(n) + '.brain'

def preheatNetwork(network):
    pass


