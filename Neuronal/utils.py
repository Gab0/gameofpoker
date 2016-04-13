#!/usr/bin/python

import random
def genWeights(Inputs, size):
    # size example = [3, 5, 6]
    Weights = []
    mu = 0.7
    sigma = 1

    size = [Inputs] + size
    for I in range(len(size) - 1):  # number of synaptic layers.
        Layer = []
        for K in range(size[I]):  # number of From instances.
            Layer.append([])
            for Z in range(size[I + 1]):  # number of To instances.
                Layer[K].append(random.gauss(mu, sigma))
        Weights.append(Layer)

    return Weights


def genThresholds(size, MinValue, MaxValue):
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

def genBias(size, MinValue, MaxValue):
    BIAS = [0]
    size = len(size)
    for z in range(size):
        BIAS.append(random.uniform(MinValue, MaxValue))
    
    return BIAS

def genName():
    
    n = random.randrange(0,1003008)
    return str(n) + '.brain'

def preheatNetwork(network):
    pass


