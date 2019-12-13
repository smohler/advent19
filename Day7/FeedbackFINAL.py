# --- Day 7: Amplification Circuit (Feedback Loop) ---

# get input data and convert it to integers
data = open('input.txt', 'r').read().strip().split(',')
prgm = tuple(map(int, data))

#Examples

example1 = (3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5)
ans1 = 139629729
phase1 = [9,8,7,6,5]


example2 = (3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,\
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,\
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10)
ans2 = 18216
phase2 = [9,7,8,5,6]


def Amplifier(PRGM, PRGMINPUT, STEP = 0, log = False, initializing = True):
    """
    returns (PRGM, LASTOUTPUT, STEP, HALTCODE)
    if HALTCODE == 0 awaiting more input else program has halted 
    """
    prgmSize = len(PRGM)
    optcodes = {1:'ADD', 2:'MULT', 3:'INPUT', 4:'OUTPUT',5:'JMPTRU', 6:'JMPFLSE', 7:'LESSTHN', 8:'EQUALS', 99:'HALT'}
    modedefs = {0: 'P', 1: 'I'}
    if log: message = 'INSTRUCTION:{0:20} OPTCODE:{1:6}({2:6}, {3:6})    PARAMETERS:({4}, {5})\tSTORE:{6:4}\tSTEP:{7:4}'
    if log: print('INPUT TO PROGRAM :{}'.format(PRGMINPUT))
    while STEP < prgmSize:
        READ = str(PRGM[STEP])
        optint = int(READ[-2:])
        OPTCODE = optcodes[optint]

        #determine the PARAMETER MODES
        if len(READ) <= 2:
            MODE2 = 'P'
            MODE1 = 'P'
        if len(READ) == 3:
            MODE2 = 'P'
            MODE1 = 'L'
        if len(READ) == 4:
            MODE2 = modedefs[int(READ[0])]
            MODE1 = modedefs[int(READ[1])]

        if OPTCODE == 'ADD': 
            INSTRUCTION = str(PRGM[STEP:STEP+4])
            if MODE1 == 'P': 
                VAL1 = PRGM[PRGM[STEP+1]]  
            else: 
                VAL1 = PRGM[STEP+1]

            if MODE2 == 'P': 
                VAL2 = PRGM[PRGM[STEP+2]]
            else: 
                VAL2 = PRGM[STEP+2]
            STOR = PRGM[STEP+3]
            PRGM[STOR] = VAL1+VAL2
            if log: print(message.format(INSTRUCTION, OPTCODE,VAL1, VAL2, MODE1, MODE2, STOR, STEP))  
            STEP = STEP + 4
            
            
        if OPTCODE == 'MULT':
            INSTRUCTION = str(PRGM[STEP:STEP+4])
            if MODE1 == 'P': 
                VAL1 = PRGM[PRGM[STEP+1]]
            else: 
                VAL1 = PRGM[STEP+1]

            if MODE2 == 'P': 
                VAL2 = PRGM[PRGM[STEP+2]]
            else: 
                VAL2 = PRGM[STEP+2]

            STOR = PRGM[STEP+3]
            PRGM[STOR] = VAL1*VAL2
            if log: print(message.format(INSTRUCTION, OPTCODE,VAL1, VAL2, MODE1, MODE2, STOR, STEP)) 
            STEP = STEP + 4
             

        if OPTCODE == 'INPUT':
            INSTRUCTION = str(PRGM[STEP:STEP+2])
            if log:
                #VAL = int(input('User Input: '))
                VAL = PRGMINPUT
            else:
                VAL = PRGMINPUT
            STOR = PRGM[STEP+1]
            if log: print(message.format(INSTRUCTION, OPTCODE,VAL, 'NA', "P", "NA", STOR, STEP))  
            PRGM[STOR] = VAL
            STEP = STEP + 2
            HALTCODE = 0
            if initializing: return PRGM, None, STEP, HALTCODE
            
        if OPTCODE == 'OUTPUT':
            INSTRUCTION = str(PRGM[STEP:STEP+2])
            if MODE1 == 'P':
                VAL = PRGM[PRGM[STEP+1]]
                #store output at end of program
            else:
                VAL = PRGM[STEP+1]
                #store output at end of program

            if log: print(message.format(INSTRUCTION, OPTCODE,VAL, "NA", MODE1, "NA", "NA", STEP))      
            outputmessage = 'PROGRAM OUTPUT: {}\t PROGRAM POINTER: {}'
            STEP = STEP + 2
            HALTCODE = 2
            if log: print(outputmessage.format(VAL, STEP)) 
            return PRGM, VAL, STEP, HALTCODE

        if OPTCODE == 'JMPTRU':
            INSTRUCTION = str(PRGM[STEP:STEP+3])
            if MODE1 == 'P': 
                VAL1 = PRGM[PRGM[STEP+1]]
            else: 
                VAL1 = PRGM[STEP+1]

            if MODE2 == 'P': 
                VAL2 = PRGM[PRGM[STEP+2]]
            else: 
                VAL2 = PRGM[STEP+2]

            if VAL1 != 0:
                STEP = VAL2
            else:
                STEP = STEP + 3
            if log: print(message.format(INSTRUCTION, OPTCODE,VAL1, VAL2, MODE1, MODE2, STOR, STEP)) 
 
        if OPTCODE == 'JMPFLSE':
            INSTRUCTION = str(PRGM[STEP:STEP+3])
            if MODE1 == 'P': 
                VAL1 = PRGM[PRGM[STEP+1]]
            else: 
                VAL1 = PRGM[STEP+1]

            if MODE2 == 'P': 
                VAL2 = PRGM[PRGM[STEP+2]]
            else: 
                VAL2 = PRGM[STEP+2]

            if VAL1 == 0:
                STEP = VAL2
            else:
                STEP = STEP + 3 
            if log: print(message.format(INSTRUCTION, OPTCODE,VAL1, VAL2, MODE1, MODE2, STOR, STEP)) 

        if OPTCODE == 'LESSTHN':
            INSTRUCTION = str(PRGM[STEP:STEP+4])
            if MODE1 == 'P': 
                VAL1 = PRGM[PRGM[STEP+1]]
            else: 
                VAL1 = PRGM[STEP+1]

            if MODE2 == 'P': 
                VAL2 = PRGM[PRGM[STEP+2]]
            else: 
                VAL2 = PRGM[STEP+2]

            STOR = PRGM[STEP+3]

            if VAL1 < VAL2: 
                PRGM[STOR] = 1
            else:
                PRGM[STOR] = 0
            if log: print(message.format(INSTRUCTION, OPTCODE,VAL1, VAL2, MODE1, MODE2, STOR, STEP))
            STEP = STEP + 4          

        if OPTCODE == 'EQUALS':
            INSTRUCTION = str(PRGM[STEP:STEP+4])
            if MODE1 == 'P': 
                VAL1 = PRGM[PRGM[STEP+1]]
            else: 
                VAL1 = PRGM[STEP+1]

            if MODE2 == 'P': 
                VAL2 = PRGM[PRGM[STEP+2]]
            else: 
                VAL2 = PRGM[STEP+2]

            STOR = PRGM[STEP+3]

            if VAL1 == VAL2: 
                PRGM[STOR] = 1
            else:
                PRGM[STOR] = 0
            if log: print(message.format(INSTRUCTION, OPTCODE,VAL1, VAL2, MODE1, MODE2, STOR, STEP))
            STEP = STEP + 4 
               
        if OPTCODE == 'HALT':
            INSTRUCTION = str(PRGM[STEP:STEP+4]) 
            if log: print(message.format(INSTRUCTION, OPTCODE,0, 0, '0', '0', 0, STEP));print('HALTING')
            HALTCODE = 1
            if log: print("RETURNING LAST OUTPUT VALUE OF: {}".format(PRGMINPUT))
            return PRGM, PRGMINPUT, STEP, HALTCODE




def loadProgram(program):
    return list(program)



# generate all possible phase combinations
from itertools import permutations
PHASES = list(permutations([5, 6, 7, 8, 9]))
print('Number of Possible Phase Combinations: {}'.format(len(PHASES)))

AMP = []

program = example1
P = phase1
ans = ans1
kmax = 100
k = 0

def Looper(program, phasecodes, kmax = 1000):
    P = phasecodes
    haltE = 0
    k = 0
    while k <kmax:
        if k == 0:
            programA = loadProgram(program)
            programB = loadProgram(program)
            programC = loadProgram(program)
            programD = loadProgram(program)
            programE = loadProgram(program)

            ampPrgmA, ampA, stepA, __ = Amplifier(programA, P[0], STEP = 0) #Amplifier A
            ampPrgmA, ampA, stepA, __ = Amplifier(ampPrgmA, 0, STEP = stepA,initializing = False) #Amplifier A
        
            ampPrgmB, ampB, stepB, __ = Amplifier(programB, P[1], STEP = 0) #Amplifier B
            ampPrgmB, ampB, stepB, __ = Amplifier(ampPrgmB, ampA, STEP = stepB,initializing = False) #Amplifier B
        
            ampPrgmC, ampC, stepC, __ = Amplifier(programC, P[2], STEP = 0) #Amplifier C
            ampPrgmC, ampC, stepC, __ = Amplifier(ampPrgmC, ampB, STEP = stepC,initializing = False) #Amplifier C
        
            ampPrgmD, ampD, stepD, __ = Amplifier(programD, P[3], STEP = 0) #Amplifier D
            ampPrgmD, ampD, stepD, __ = Amplifier(ampPrgmD, ampC, STEP = stepD,initializing = False) #Amplifier D
        
            ampPrgmE, ampE, stepE, haltE = Amplifier(programE, P[4], STEP = 0) #Amplifier E
            ampPrgmE, ampE, stepE, haltE = Amplifier(ampPrgmE, ampD, STEP = stepE, initializing = False) #Amplifier E 
        else:
            # input is now just the output of loop
            ampPrgmA, ampA, stepA, __ = Amplifier(ampPrgmA, ampE, STEP = stepA,initializing = False) #Amplifier A
            ampPrgmB, ampB, stepB, __ = Amplifier(ampPrgmB, ampA, STEP = stepB,initializing = False) #Amplifier B
            ampPrgmC, ampC, stepC, __ = Amplifier(ampPrgmC, ampB, STEP = stepC,initializing = False) #Amplifier C
            ampPrgmD, ampD, stepD, __ = Amplifier(ampPrgmD, ampC, STEP = stepD,initializing = False) #Amplifier D
            ampPrgmE, ampE, stepE, haltE = Amplifier(ampPrgmE, ampD, STEP = stepE,initializing = False) #Amplifier E  
        if haltE == 1: 
            return ampE 
        if k == kmax:
            print('Too Many Iterations k = kmax')
            return ampE  
        k = k+1   

AMP = []
for P in PHASES:
    finalThrust = Looper(prgm, P)
    print('Permutation: {}\t Amplifier Output: {}'.format(P, finalThrust))
    AMP.append(finalThrust)


maxoutput = max(AMP)
maxoutputIndex = AMP.index(max(AMP))  
maxPhase = PHASES[maxoutputIndex]  
print('Maximum Permutation: {}\tAmplifier Output: {}'.format(maxPhase, maxoutput)) 
