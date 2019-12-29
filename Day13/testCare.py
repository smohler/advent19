import INTCODE
import Care
from importlib import reload


#part 1
reload(Care)
cpu = INTCODE.computer()
data = open('pong.txt').read().split(',')
program = list(map(int, data))
Care.arcade(cpu, program)

#part2
reload(Care)
cpu = INTCODE.computer()
data = open('pong.txt').read().split(',')
program = list(map(int, data))
program[0]=2
Care.arcade(cpu,program)
