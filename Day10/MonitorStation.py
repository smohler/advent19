#all the functions that help solve finding the optimal asteriod station...to be tested
import numpy as np
from numpy import linalg as LA
import math
import itertools as IT
def makeMatrix(rawdata):
    data = open(rawdata, 'r').read().split('\n')
    Symbol = {'.':0, '#':1}
    Filter = lambda x: Symbol[x]
    matrix = np.matrix([(list(map(Filter, row))) for row in data]) 
    return matrix

def coordinates(matrix):
    indxs = matrix.nonzero()
    coords = list(zip(indxs[0], indxs[1]))
    return coords

def shiftOrigin(base, coordinates):
    points = coordinates
    points = [(base[0]-point[0], point[1]-base[1]) for point in points]
    points.remove((0,0))
    return points

def rankStation(coordinates):
    # assumes coordinates have been shifted
    angle = lambda x: math.atan2(x[1],x[0])
    dist = lambda x: abs(x[1]) + abs(x[0])
    allAngles = list(map(angle, coordinates))
    allDists = list(map(dist, coordinates))
    points = zip(allAngles, allDists, coordinates)
    Dict = {}
    for angle, dist, coord in points:
        key = angle
        Dict.setdefault(key,[]).append((dist, coord))
        Dict[key] = sorted(Dict[key])
    return len(Dict), Dict

def bestStation(coordinates):
    stations = []
    for coord in coordinates:
        base = coord
        others = shiftOrigin(base, coordinates)
        uniques, _  = rankStation(others)
        stations.append((uniques, base))
    return sorted(stations)

def dictBlast(totalAngles, dictionary, coordinates, base):
    D = dictionary
    totalAsteroids = len(coordinates)
    angles = sorted(D.keys())
    start = angles.index(min(list(filter(lambda x: x>=0, angles))))
    angles = angles[start:] + angles[:start]
    k = 0; shot = 0
    shotlist = []
    while shot<totalAsteroids:
        if not D[angles[k]]:# there are not values for this key
            k = (k+1)%totalAngles
        else:
            bang = D[angles[k]].pop(0)
            shotlist.append(bang[1])
            k = (k+1)%totalAngles
            shot = shot + 1
    back = lambda x: (x[1]+base[1], base[1]-x[0])
    return list(map(back, shotlist))