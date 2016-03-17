#!/usr/bin/python
import json

def load_brain(filename):
    Fo = open(filename, 'r')

    read = Fo.read()
    read = read.split('&')
    for fragment in read:
        R = json.loads(fragment[3:])#, parse_float, parse_int)
        if "THR" in fragment:
            Thresholds = R
        if "WGH" in fragment:
            Weights = R

    return [Weights,Thresholds]

def save_brain(filename, Weights, Thresholds):
    Fo = open(filename, 'w+')

    Fo.write("THR")
    print(json.dumps(Thresholds))
    Fo.write(json.dumps(Thresholds))
    Fo.write('&WGH')
    Fo.write(json.dumps(Weights))

    Fo.close()



    
    
