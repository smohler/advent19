import MonitorStation as MS
from importlib import reload
testMsg = 'Test case {}.  Asserted{}\tOutput{}'

#example1
a = (3,4)
M = MS.makeMatrix('ex1.txt')
C = MS.coordinates(M)
B = MS.bestStation(C
s = B[-1][1][::-1]
print(testMsg.format(a==s, a, s))

#example2
a = (5,8)
M = MS.makeMatrix('ex2.txt')
C = MS.coordinates(M)
B = MS.bestStation(C)
s = B[-1][1][::-1]
print(testMsg.format(a==s, a, s))


#example3
a = (1,2)
M = MS.makeMatrix('ex3.txt')
C = MS.coordinates(M)
B = MS.bestStation(C)
s = B[-1][1][::-1]
print(testMsg.format(a==s, a, s))


#example4
a = (6,3)
M = MS.makeMatrix('ex4.txt')
C = MS.coordinates(M)
B = MS.bestStation(C)
s = B[-1][1][::-1]
print(testMsg.format(a==s, a, s))

#example5
a = (11,13)
M = MS.makeMatrix('ex5.txt')
C = MS.coordinates(M)
B = MS.bestStation(C)
s = B[-1][1][::-1]
print(testMsg.format(a==s, a, s))


#puzzlerun
msg = 'Part 1 Solution: Base: {}\tViewed:{}'
M = MS.makeMatrix('input.txt')
C = MS.coordinates(M)
B = MS.bestStation(C)
s = B[-1]
print(msg.format(s[0], s[1][::-1]))




#testshooting1
reload(MS)
M = MS.makeMatrix('ex6.txt')
Asteroids = MS.coordinates(M)
base = (3,8)
otherAsteroids = [x for x in Asteroids if x != base]
O,A = MS.OrderAsteroids(base, otherAsteroids)
SL = MS.BlastEm(O, debug = True)
sl = MS.TransformList(SL, base)

#testshooting2
reload(MS)
M = MS.makeMatrix('ex7.txt')
Asteroids = MS.coordinates(M)
base = (5,1)
otherAsteroids = [x for x in Asteroids if x != base]
O,A = MS.OrderAsteroids(base, otherAsteroids)
SL = MS.BlastEm(O, debug = True)
sl = MS.TransformList(SL, base)

#testshooting3
reload(MS)
M = MS.makeMatrix('ex8.txt')
Asteroids = MS.coordinates(M)
base = (1,8)
otherAsteroids = [x for x in Asteroids if x != base]
O,A = MS.OrderAsteroids(base, otherAsteroids)
SL = MS.BlastEm(O, debug = True)
sl = MS.TransformList(SL, base)

#testshooting4
reload(MS)
M = MS.makeMatrix('ex9.txt')
Asteroids = MS.coordinates(M)
base = (3,3)
otherAsteroids = [x for x in Asteroids if x != base]
C = MS.shiftOrigin(base, otherAsteroids)



#testshooting5
reload(MS)
M = MS.makeMatrix('ex5.txt')
Asteroids = MS.coordinates(M)
base = (13,11)
otherAsteroids = [x for x in Asteroids if x != base]
O,A = MS.OrderAsteroids(base, otherAsteroids)
SL = MS.BlastEm(O, debug = True)
sl = MS.TransformList(SL, base)

#puzzle part 2 solution 
import MonitorStation as MS
M = MS.makeMatrix('input.txt')
Asteroids = MS.coordinates(M)
stations = MS.allMonitors(Asteroids)
base = (11,19)
otherAsteroids = [x for x in Asteroids if x != base]
O, A = MS.OrderAsteroids(base, otherAsteroids)
SL = MS.BlastEm(O, debug = True)
sl = MS.TransformList(SL, base)
MS.Solution(sl, 199)

