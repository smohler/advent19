from collections import defaultdict

def PaintBot(cpu, program, kmax = 5, debug = False):
    Color = {0:'Black', 1:'White'}
    Face = {complex(0,1): '^', complex(1,0):'>', complex(0,-1):'v', complex(-1,0):'<'}
    Turn = {0:complex(0,1), 1:complex(0,-1)}
    cpu.LoadProgram(program)
    pos = complex(0,0)
    step = complex(0,1)
    k = 0
    painted = defaultdict(list) 
    while k<kmax:
        panel = viewPanel(painted, pos)
        if debug: print('{}::Pos:{}\tInput:({},{})-->'.format(k,pos, panel, Color[panel]), end = '')
        if cpu.HALT == True: break
        paint = Color[cpu.RunProgram()]
        cpu.assignInput(panel)
        key = pos
        painted[key].append(paint)
        turn = Turn[cpu.RunProgram()]
        step = step*turn
        pos = pos + step
        if debug: print('\tOutput:({},{})\tPos{}     Face:{}'.format(paint, turn, pos, Face[step]))
        k += 1
    return len(painted.keys())

        
def viewPanel(history, pos):
    if not history[pos]: #New tiles are black 
        return 0
    if history[pos][-1] == 'Black':
        return 0
    if history[pos][-1] == 'White':
        return 1