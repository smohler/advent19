import keyboard
import tkinter as gui
import time
def arcade(cpu, program):
    cpu.LoadProgram(program)
    running = True
    score = horz_x = ball_x = 0
    screen = gui.Tk()
    screen.title('Score:{}'.format(score))
    sgn = lambda x: -1 if x<0 else 1 if x>0 else 0
    while running:
        cpu.assignInput(sgn(ball_x - horz_x))
        x, y, tile = update(cpu)
        #track ball
        if tile == 3: horz_x = x 
        #track horizontal panel
        if tile == 4: ball_x = x
        
        #update screen
        if (x,y) == (-1,0): score = tile; screen.title('Score = {}'.format(score))
        else: draw(x,y,tile,screen)

        #time.sleep(0.005)
        #exit loop 
        if keyboard.is_pressed('q'): break
        if cpu.HALT == True: running = False; break 

        screen.update_idletasks()
        screen.update() 
    return score

def update(cpu):
    x = cpu.RunProgram()
    y = cpu.RunProgram()
    tile = cpu.RunProgram()
    return x, y, tile


def draw(x,y,tile,screen):
    tiles = {0:'empty', 1:'wall', 2:'block', 3:'horz', 4:'ball', None:'gameover'}
    if tiles[tile] == 'empty': txt =  ' '
    if tiles[tile] == 'wall': txt = '_' 
    if tiles[tile] == 'block': txt = '_'
    if tiles[tile] == 'horz': txt = '_'
    if tiles[tile] == 'ball': txt = '_'
    if tiles[tile] == 'gameover': txt = ' '
    if x==99: x = 0
    gui.Label(screen, text=txt).grid(row=y,column=x)