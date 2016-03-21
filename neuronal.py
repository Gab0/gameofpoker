#!/usr/bin/python

# import mlxtend.classifier import NeuralNetMLP
import random
from neuronalIO import load_brain, save_brain
import os

stdThresholdSize = [15, 23, 2]
stdWeightSize = [(15, 23), (23, 2)]


class neuron():

    def __init__(self, threshold):
        self.reset()
        self.Output = 0
        self.Threshold = threshold

    def process(self):
        SUM = 0
        for v in self.Input:
            SUM += v

        if SUM > self.Threshold:
            self.Output = SUM
        else:
            self.Output = 0

    def compare(self):
        R = 0
        ValidSize = 0
        for i in range(len(self.Input)):
            if not self.Input[i]:
                continue
            ValidSize += 1
            if self.Input[i] in self.Input[:i] + self.Input[i + 1:]:
                R += 1

        if ValidSize:
            self.Output += R / ValidSize

    def reset(self):
        self.Input = []


class synapse():

    def __init__(self, weight, From, To):
        self.weight = weight

        self.From = From
        self.To = To

    def connect(self):
        self.To.Input.append(self.From.Output * self.weight)


class NeuralNetwork():

    def __init__(self):
        self.ExpectedInputSize = 15

        Z = grabAbrain()
        self.Weights = Z[0]
        self.Thresholds = Z[1]

        self.Setup()

    def think(self, IN):
        # action.
        if not len(IN) == self.ExpectedInputSize:
            print("Wrong input size (%i != %i) on NeuralNetwork." %
                  (len(IN),self.ExpectedInputSize))
            exit()

        for I in range(len(IN)):
            self.Li[I].Input = IN
            self.Li[I].process()
            self.Li[I].compare()
            self.Li[I].reset()

        for I in range(len(self.Si1)):
            self.Si1[I].connect()

        for I in range(len(self.L1)):
            self.L1[I].process()
            self.L1[I].reset()
        for I in range(len(self.S1o)):
            self.S1o[I].connect()

        result = []
        for I in range(len(self.Lo)):
            self.Lo[I].process()
            self.Lo[I].reset()
            result.append(self.Lo[I].Output)

        return result

    def Setup(self):
        # As for the project is right now, with 11 inputs/23 hidden/2 outputs;
        # the Weights array is a [[[11*[23]],[[23*[2]]] array of
        # floats between 0 and 1.

        # the Thresholds array is [[*11*],[*23*],[*2*]]
        # setup.
        self.Li = []
        for I in range(self.ExpectedInputSize):
            self.Li.append(neuron(self.Thresholds[0][I]))

        self.L1 = []
        for I in range(23):
            self.L1.append(neuron(self.Thresholds[1][I]))

        self.Lo = []
        for I in range(2):
            self.Lo.append(neuron(self.Thresholds[2][I]))

        self.Si1 = self.setSynapses(self.Li, self.L1, 0, 1)

        self.S1o = self.setSynapses(self.L1, self.Lo, 1, 0)

    def setSynapses(self, layer_from, layer_to, Column, FIXED):
        S = []
        X = 1
        for F in range(len(layer_from)):
            for T in range(len(layer_to)):
                if not FIXED:
                    X = self.Weights[Column][F][T]
                S.append(synapse(X, layer_from[F], layer_to[T]))
        return S


def genWeights(size=stdWeightSize):
    # size example = [(3,6),(5,3)]
    Weights = []

    for I in range(len(size)):  # number of synaptic layers.
        Layer = []
        for K in range(size[I][0]):  # number of From instances.
            Layer.append([])
            for Z in range(size[I][1]):  # number of To instances.
                Layer[K].append(random.random())
        Weights.append(Layer)

    return Weights


def genThresholds(MaxValue, size=stdThresholdSize):
    # size example = [3, 5, 6]
    Thresholds = []

    for I in range(len(size)):  # number of Neuronal layers.
        Layer = []
        for K in range(size[I]):  # size of layer.
            Layer.append(random.randrange(MaxValue))
        Thresholds.append(Layer)

    return Thresholds


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
    return [W, T]


X = NeuralNetwork()
