#all the functions that help solve finding the optimal asteriod station...to be tested
import numpy as np
from numpy import linalg as LA
import math
import itertools as IT
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

def Colinear(o,u,v):
    #the triangle inequality for vectors (o,u,v)
    #o: origin point
    #u: arbitrary point, v:arbitrary point
    ox = o[0]; oy = o[1]
    ux = u[0]; uy = u[1]
    vx = v[0]; vy = v[1]
    A = ox*(uy - vy) + ux*(vy - oy) + vx*(oy - uy)
    return 1*(A == 0)

def TotalColinears(origin, otherpoints):
    combs = list(IT.combinations(otherpoints, 2))
    return [Colinear(origin, comb[0], comb[1]) for comb in combs]

def TotalTriangle(otherpoints):
    combs = list(IT.combinations(otherpoints, 2))
    return [TriangleCheck(comb[0], comb[1]) for comb in combs]

def TriangleCheck(p1, p2):
    #use the triangle inequality to determine if two points are on a line relative to the origin
    norm = lambda x: math.sqrt(x[0]**2 + x[1]**2)
    vadd = lambda x, y: (x[0] + y[0], x[1] + y[1])
    return norm(vadd(p1, p2)) == norm(p1) + norm(p2)

def shiftOrigin(origin, otherpoints):
    shiftedPoints = [(point[0] - origin[0], point[1] - origin[1]) for point in otherpoints]
    return shiftedPoints

def allMonitors(coordinates):
    allAsteroids = coordinates
    Colinears = []
    for anAsteroid in allAsteroids:
        otherAsteroids = [x for x in allAsteroids if x != anAsteroid]
        shiftedAsteroids = shiftOrigin(anAsteroid, otherAsteroids)
        T = TotalTriangle(shiftedAsteroids)
        Colinears.append(sum(T))
    zeros = [i for i, p  in enumerate(Colinears) if p == min(Colinears)]
    bestAsteroids = [allAsteroids[i] for i in zeros]
    #reverse entries to match problem set up. 
    flip = lambda x: x[::-1]
    bestAsteroids = list(map(flip, bestAsteroids))
    return (bestAsteroids, len(Colinears) - min(Colinears))

#best canditates are ones that at least have no colinear points.