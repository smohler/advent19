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
            _,bang = D[angles[k]].pop(0)
            shotlist.append(bang)
            k = (k+1)%totalAngles
            shot = shot + 1
    back = lambda x: (x[1]+base[1],base[0]-x[0])
    return list(map(back,shotlist))


def OrderAsteroids(base, asteroids):
    angle = lambda x: math.atan2(x[1],x[0])
    shiftedAsteroids = sorted(shiftOrigin(base, asteroids), key = angle)
    thetas = list(map(angle, shiftedAsteroids))
    start = thetas.index(min(list(filter(lambda x: x>=0, thetas))))
    thetas = thetas[start:] + thetas[:start]
    shiftedAsteroids = shiftedAsteroids[start:] + shiftedAsteroids[:start]
    pairs = list(zip(thetas, shiftedAsteroids))
    return pairs, thetas

def reorder(targets):
    # reoder targets after rotation (a, (x,y))
    angle = lambda x: math.atan2(x[1][1],x[1][0])
    thetas = list(map(angle, targets))
    start = targets.index(min(list(filter(lambda x: x[0]>=0, targets))))
    thetas = thetas[start:] + thetas[:start]
    targets = targets[start:] + targets[:start]
    return targets

def BlastEm(asteroids, startingpoint = 0, debug = False):
    #compare (a, (x,y)) and (a,(u,v))
    sameAngle = lambda x, y: (x[0]-y[0])**2<1e-8 and x[1] != y[1]
    samePoint = lambda x, y: (x[0]-y[0])**2<1e-8 and x[1] == y[1]
    dist = lambda x: x[0]**2 + x[1]**2
    closer = lambda x, y: x if dist(x[1])<=dist(y[1]) else y
    rotation = lambda x,y: True if x[0]<0 and y[0]>=0 else False

    shotlist = []
    total = len(asteroids)
    k = startingpoint
    aim = asteroids[k]
    nextaim = asteroids[k+1]
    targets = asteroids
    point = 1
    message = "aim:{}  target:{}  k:{}  total:{}"
    while total > 0:
        
        if debug: 
            print(message.format(aim, nextaim, point, total))
        
        if rotation(aim, nextaim):
            if debug: print("Rotation")
            targets = reorder(targets)

        if total == 1: #last one!
            print('Shooting Last One:{}'.format(aim))
            targets = sorted(targets)
            shotlist = shotlist + targets
            total = 0

        elif sameAngle(aim, nextaim):
            print('Same Angles')
            #aim at the closest one
            aim = closer(aim, nextaim)
            point = (targets.index(nextaim) + 1)%total
            nextaim = targets[point]

        elif samePoint(aim, nextaim):
            print('Same Point!')
            point = (targets.index(nextaim) + 1)%total
            nextaim = targets[point]  
            shotlist.append(aim)
            targets.remove(aim)
            total = len(targets)         

        else: #blast em
            print('Shooting:{}'.format(aim))
            shotlist.append(aim)
            targets.remove(aim)
            total = len(targets)
            aim = nextaim
            point = (targets.index(aim) + 1)%total
            nextaim = targets[point]

        
    return shotlist

def TransformList(shotlist, base):
    getBack = lambda p: (p[1][1]+base[1], base[0]-p[1][0])
    Shotlist = list(map(getBack, shotlist))
    return Shotlist
   
def Solution(shotlist, index):
    ans = lambda x: x[0]*100 + x[1]
    winningShot = shotlist[index]
    return ans(winningShot)