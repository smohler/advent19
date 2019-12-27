import INTCODE
import SpacePolice as SP
from importlib import reload
test = [3,100,104,1,104,0,3,100,104,0,104,0,3,100,104,1,104,0,3,100,104,1,104,0,3,100,104,0,104,1,3,100,104,1,104,0,3,100,104,1,104,0,99]
cpu = INTCODE.computer()
d, pts = SP.PaintBot(cpu, test, debug = True, kmax = 10)
print('Test is {}:\t Asserted {}:Output {}'.format(d==6, 6, d))

data = open('input.txt').read().split(',')
program = list(map(int, data))
d, pts = SP.PaintBot(cpu, program, debug = False, kmax =10000)
