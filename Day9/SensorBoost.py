#Sensor Boost (Intcode)
# get input data and convert it to integers
from INTCODE import computer
Intcode = computer('BOOST')
data = open('input.txt', 'r').read().strip().split(',')
prgm = list(map(int, data))
prgm = Intcode.assignMemory(prgm)
prgm = Intcode.assignInput(prgm, [1])
Intcode.RunProgram(prgm)
