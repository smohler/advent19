#all the functions that help solve finding the optimal asteriod station...to be tested
import numpy as np
def turnMatrix(rawdata):
    data = open(rawdata, 'r').read().split('\n')
    Symbol = {'.':0, '#':1}
    Filter = lambda x: Symbol[x]
    matrix = np.matrix([(list(map(Filter, row))) for row in data]) 
    return matrix

def COM(matrix):
    mass = matrix.sum()
    indxs = matrix.nonzero()
    coord = (sum(indxs[0])/mass, sum(indxs[1])/mass)
    return coord

def coordinate(matrix):
    indxs = matrix.nonzero()
    coords = list(zip(indxs[0], indxs[1]))
    return coords




    
