import numpy as np
import skfuzzy as fuzz

def linearFunction(points, x, pending = True):
    if pending:
        if x<points['a']:
            return 0 
        elif ( x >= points['a'] and x < points['b']):
            return ( ( x - points['a'] ) / ( points['b'] - points['a'] ) )
        elif x >= points['b']:
            return 1
    else:
        if x<points['a']:
            return 1 
        elif x >= points['a'] and x <= points['b']:
            return ( points['b'] - x ) / ( points['b'] - points['a'] )
        elif x >= points['b']:
            return 0
pass

def triangleFunction(points, x):
    if x <= points['a']:
        return 0
    elif x >= points['a'] and x <= points['b']:
        return( x - points['a'] ) / ( points['b'] - points['a'] )
    elif x >= points['b'] and x <= points['c']:
        return ( points['c'] - x ) / ( points['c'] - points['b'] )
    elif x >= points['c']:
        return 0
    return values
pass

def trapezoidalFunction(points, x):
    if x <= points['a']:
        return 0
    elif x >= points['a'] and x <= points['b']:
        return ( x - points['a'] ) / ( points['b'] - points['a'] ) 
    elif x >= points['b'] and x <= points['c']:
        return 1
    elif x >= points['c'] and x <= points['d']:
        return ( points['d'] - x ) / ( points['d'] - points['c'] )
    elif x >= points['d']:
        return 0
pass

def generalizedBellFunction(generalizedBellData, xrange):
    return fuzz.gbellmf(xrange, generalizedBellData['width'],generalizedBellData['slope'],generalizedBellData['center'])
pass

def gaussianFunction(gaussianData, xrange):
    return fuzz.gaussmf(xrange, gaussianData['mean'], gaussianData['sigma'])