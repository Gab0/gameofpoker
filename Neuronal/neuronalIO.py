#!/usr/bin/python
import json

class BrainValues():
    def __init__(self):
        self.WeightsValues = None
        self.ThresholdsValues = None
        self.BiasValues = None
        self.Score = None
        
    def ApplyValues(self, Network):
        Network.Weights = self.WeightsValues
        Network.Thresholds = self.ThresholdsValues
        Network.Bias = self.BiasValues
        Network.Score = self.Score

LogFile = open('brain.log', 'a+')

def load_brain(filename):
    Fo = open(filename, 'r')

    Weights = 0
    Thresholds = 0
    Bias = 0
    read = Fo.read()
    read = read.split('&')
    Skeleton = BrainValues()
    
    for fragment in read:
        R = json.loads(fragment[3:])#, parse_float, parse_int)
        if "THR" in fragment:
            Skeleton.ThresholdsValues = R
        if "WGH" in fragment:
            Skeleton.WeightsValues = R
        if "BIS" in fragment:
            Skeleton.BiasValues = R
        if "SCR" in fragment:
            Skeleton.Score = R
            
    if not Skeleton.BiasValues:
        Skeleton.BiasValues = genBias(2, 0, 2)
    try:
        return Skeleton
    except UnboundLocalError:
        print ("Outdated brain file.")
        exit()
        
def save_brain(Network):
    Fo = open('brain/%s.brain' % Network.name, 'w+')

    Fo.write('SCR')
    Fo.write(json.dumps(Network.Score))
    Fo.write("&THR")
    # print(json.dumps(Thresholds))
    Fo.write(json.dumps(Network.Thresholds))
    Fo.write('&WGH')
    Fo.write(json.dumps(Network.Weights))
    Fo.write('&BIS')
    Fo.write(json.dumps(Network.Bias))
    Fo.close()


def log(text):
    LogFile.write("%s\n" % text)
 
def test_brain(filename):
    pass
    
