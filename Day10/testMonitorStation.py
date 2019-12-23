import MonitorStation as MS
from importlib import reload
testMsg = 'Test case {}.  Asserted{}\tOutput{}'

#example1
a = (3,4)
M = MS.makeMatrix('ex1.txt')
C = MS.coordinates(M)
B = MS.bestStation(C)
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
print(msg.format(s[1][::-1], s[0]))

#part 2 testing
M = MS.makeMatrix('ex6.txt')
C = MS.coordinates(M)
base = (3,8)
sC = MS.shiftOrigin(base, C)
uniques,D = MS.rankStation(sC)
MS.dictBlast(uniques, D, sC)
