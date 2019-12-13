# load data
import numpy as n
data = list(open('input.txt', 'r').read().strip().split('\n'))
WIRE1 = data[0].split(',')
WIRE2 = data[1].split(',')
exampleWire1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
exampleWire2 = ['U62','R66','U55','R34','D71','R55','D58','R83']
exampleWire3 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
exampleWire4 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
exampleWire5 = ['R8','U5','L5','D3']
exampleWire6 = ['U7','R6','D4','L4']

def Wire(Connections):
    #generate all points traced out from the connections
    direction = {'L':n.array([-1,0]), 'R':n.array([1,0]), 'U':n.array([0,1]), 'D':n.array([0,-1])}
    steps = len(Connections)
    path = n.array([0,0])
    point = n.array([0,0])
    total_distance = 0
    k = 0
    while k<steps:
        slope = direction[Connections[k][0]]
        distance = int(Connections[k][1:])
        total_distance = total_distance + distance
        #new position = direction*distance + old position
        for i in range(distance):
            add_point = slope*i + point
            path = n.vstack([path, add_point])
        point = slope*distance+ point
        k = k+1
    print('Length of Wire : {}'.format(total_distance))    
    return path[2:,:] #dont return [0,0]

p = Wire(WIRE1)
q = Wire(WIRE2)

def Intersections(wire1, wire2):
    #find all common points between the two wire paths
    wire1_points = set([tuple(x) for x in wire1])
    wire2_points = set([tuple(x) for x in wire2])
    return n.array([x for x in wire1_points & wire2_points])


Xs = Intersections(p,q) #taxi cab norm is sum of absolute values of points 


totalsteps = []
for i in range(len(Xs)):
    steps1 = n.where((p[:,0] == Xs[i][0]) & (p[:,1] == Xs[i][1]))[0] + 1
    steps2 = n.where((q[:,0] == Xs[i][0]) & (q[:,1] == Xs[i][1]))[0] + 1
    totalsteps.append(steps1 + steps2)
    message = 'Wire(1) Step = {}\t Wire(2) Steps = {}\t Total Steps = {}'
    print(message.format(steps1, steps2, steps1 + steps2))
print('Minimum Steps to Intersection Point is {}'.format(min(totalsteps)))   
