#Sensor Boost (Intcode)
# get input data and convert it to integers
from INTCODE import computer
BOOSTER = computer('BOOST', clock_Mode = 'STEP', Print = True )
data = open('input.txt', 'r').read().strip().split(',')
prgm = list(map(int, data))
BOOSTER.LoadProgram(prgm, [1])
output = BOOSTER.RunProgram()
print(output)