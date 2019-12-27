from collections import defaultdict
from matplotlib import pyplot as plt
import numpy as np

def PaintBot(cpu, program, kmax = 50000, debug = False):
    Color = {0:'Black', 1:'White', 99: 0}
    Face = {complex(0,1): '^', complex(1,0):'>', complex(0,-1):'v', complex(-1,0):'<', complex(0,0):'Halt'}
    Turn = {0:complex(0,1), 1:complex(0,-1), None : 0}
    cpu.LoadProgram(program, 1)
    pos = key = complex(0,0)
    step = complex(0,1)
    k = 0
    painted = defaultdict(list) 
    while k<kmax: 
        if cpu.HALT == True:
            break
            
        panel = viewPanel(painted, pos)
        if k == 0: panel = 1
        cpu.assignInput(panel)    
           
        if debug: print('{}::Pos:{}\tInput:({},{})-->'.format(k,pos, panel, Color[panel]), end = '')
        paint = Color[cpu.RunProgram()]
        turn = Turn[cpu.RunProgram()]

        key = pos
        painted[key].append(paint)

        step = step*turn
        pos = pos + step  
        
        if debug: print('\tOutput:({},{})\tPos{}     Face:{}'.format(paint, turn, pos, Face[step]))
        
        k += 1
    plt.show()
    return len(painted.keys()), painted

        
def viewPanel(history, pos):
    if not history[pos]: #New tiles are black 
        return 0
    if history[pos][-1] == 'Black':
        return 0
    if history[pos][-1] == 'White':
        return 1

def visualizer(paintedPoints):
    plt.figure(facecolor='k')
    for point, color in paintedPoints.items():
        x = point.real
        y = point.imag
        if isinstance(color[-1], int): continue
        plt.scatter(x,y, color = color[-1].lower())
    ax = plt.gca()
    ax.set_facecolor('black')
    plt.show()

