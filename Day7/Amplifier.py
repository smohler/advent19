# --- Day 7: Amplification Circuit ---

# get input data and convert it to integers
data = open('input.txt', 'r').read().strip().split(',')
prgm = list(map(int, data))

#Examples
example1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]; input1 = [4,3,2,1,0]; ans1 = 43210

example2 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,\
101,5,23,23,1,24,23,23,4,23,99,0,0]; input2 = [0,1,2,3,4]; ans2 = 54321

example3 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,\
1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]; input3 = [1,0,4,3,2]; ans3 = 65210


def Amplifier(PRGM, PRGMINPUT, log = False):
    STEP = 0
    inputSTEP = 0
    prgmSize = len(PRGM)
    optcodes = {1:'ADD', 2:'MULT', 3:'INPUT', 4:'OUTPUT',5:'JMPTRU', 6:'JMPFLSE', 7:'LESSTHN', 8:'EQUALS', 99:'HALT'}
    modedefs = {0: 'POSITIONAL', 1: 'IMMEDIATE'}

    if log: message = 'READ:{0:8}OPTCODE:{1:8}PARAMETER MODES:({2:10}, {3:10})\tSTEP:{4:3}'
    while STEP < prgmSize:
        READ = str(PRGM[STEP])
        optint = int(READ[-2:])
        OPTCODE = optcodes[optint]

        #determine the PARAMETER MODES
        if len(READ) <= 2:
            MODE2 = 'POSITIONAL'
            MODE1 = 'POSITIONAL'
        if len(READ) == 3: #mean 101 or 100 which imply modes
            MODE2 = 'POSITIONAL'
            MODE1 = 'IMMEDIATE'
        if len(READ) == 4:
            MODE2 = modedefs[int(READ[0])]
            MODE1 = modedefs[int(READ[1])]

        if log: print(message.format(READ, OPTCODE, MODE1, MODE2, STEP))  

        if OPTCODE == 'ADD': 
            if MODE1 == 'POSITIONAL': 
                VAL1 = PRGM[PRGM[STEP+1]]  
            else: 
                VAL1 = PRGM[STEP+1]

            if MODE2 == 'POSITIONAL': 
                VAL2 = PRGM[PRGM[STEP+2]]
            else: 
                VAL2 = PRGM[STEP+2]
            STOR = PRGM[STEP+3]
            PRGM[STOR] = VAL1+VAL2
            STEP = STEP + 4
            
        if OPTCODE == 'MULT':
            if MODE1 == 'POSITIONAL': 
                VAL1 = PRGM[PRGM[STEP+1]]
            else: 
                VAL1 = PRGM[STEP+1]

            if MODE2 == 'POSITIONAL': 
                VAL2 = PRGM[PRGM[STEP+2]]
            else: 
                VAL2 = PRGM[STEP+2]

            STOR = PRGM[STEP+3]
            PRGM[STOR] = VAL1*VAL2
            STEP = STEP + 4

        if OPTCODE == 'INPUT':
            if log:
                VAL = int(input('User Input: '))
                print('INPUT TO PROGRAM :{}'.format(VAL))
            else:
                VAL = PRGMINPUT[inputSTEP]
            STOR = PRGM[STEP+1]
            PRGM[STOR] = VAL
            STEP = STEP + 2
            inputSTEP =+1

        if OPTCODE == 'OUTPUT':
            if MODE1 == 'POSITIONAL':
                VAL = PRGM[PRGM[STEP+1]]
            else:
                VAL = PRGM[STEP+1]
            outputmessage = 'PROGRAM OUTPUT: {}'
            if log: print(outputmessage.format(VAL))
            PRGM.append(int(VAL)) #OUTPUT the Result to the end of program  
            STEP = STEP + 2

        if OPTCODE == 'JMPTRU':
            if MODE1 == 'POSITIONAL': 
                VAL1 = PRGM[PRGM[STEP+1]]
            else: 
                VAL1 = PRGM[STEP+1]

            if MODE2 == 'POSITIONAL': 
                VAL2 = PRGM[PRGM[STEP+2]]
            else: 
                VAL2 = PRGM[STEP+2]

            if VAL1 != 0:
                STEP = VAL2
            else:
                STEP = STEP + 3 
        if OPTCODE == 'JMPFLSE':
            if MODE1 == 'POSITIONAL': 
                VAL1 = PRGM[PRGM[STEP+1]]
            else: 
                VAL1 = PRGM[STEP+1]

            if MODE2 == 'POSITIONAL': 
                VAL2 = PRGM[PRGM[STEP+2]]
            else: 
                VAL2 = PRGM[STEP+2]

            if VAL1 == 0:
                STEP = VAL2
            else:
                STEP = STEP + 3 

        if OPTCODE == 'LESSTHN':
            if MODE1 == 'POSITIONAL': 
                VAL1 = PRGM[PRGM[STEP+1]]
            else: 
                VAL1 = PRGM[STEP+1]

            if MODE2 == 'POSITIONAL': 
                VAL2 = PRGM[PRGM[STEP+2]]
            else: 
                VAL2 = PRGM[STEP+2]

            STOR = PRGM[STEP+3]
            STEP = STEP + 4

            if VAL1 < VAL2: 
                PRGM[STOR] = 1
            else:
                PRGM[STOR] = 0
            

        if OPTCODE == 'EQUALS':
            if MODE1 == 'POSITIONAL': 
                VAL1 = PRGM[PRGM[STEP+1]]
            else: 
                VAL1 = PRGM[STEP+1]

            if MODE2 == 'POSITIONAL': 
                VAL2 = PRGM[PRGM[STEP+2]]
            else: 
                VAL2 = PRGM[STEP+2]

            STOR = PRGM[STEP+3]
            STEP = STEP + 4

            if VAL1 == VAL2: 
                PRGM[STOR] = 1
            else:
                PRGM[STOR] = 0
               
        if OPTCODE == 'HALT':
            if log: print('HALT')
            return PRGM


# Amplifier Program
ampPrgm = prgm 

# generate all possible phase combinations
from itertools import permutations
PHASES = list(permutations([0, 1, 2, 3, 4]))
print('Number of Possible Phase Combinations: {}'.format(len(PHASES)))

AMP = []
message = 'Amplifier {} Output: {}'
for P in PHASES:
    amp = 0
    for p in list(P):
        ampPrgm = Amplifier(ampPrgm, [p,amp])
        amp = ampPrgm[-1]
    AMP.append(amp)    
    print('Phase Permutation: {}\tAmplifier Output: {}'.format(P, amp)) 
maxoutput = max(AMP)
maxoutputIndex = AMP.index(max(AMP))  
maxPhase = PHASES[maxoutputIndex]  
print('Maximum Permutation: {}\tAmplifier Output: {}'.format(maxPhase, maxoutput)) 
