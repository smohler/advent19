#include jump instructions 
#The Thermal Environment Supervision Terminal (Warmer)

# get input data and convert it to integers
data = open('input.txt', 'r').read().strip().split(',')
prgm = list(map(int, data))

# Example Data output = 999 if input<8, 1000 if input == 8, and 1001 if input >8
example = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

#jump tester (positions mode)  output = 0 if input = 0, output 1 if input !=0
jumpTest1  = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]

#jump tester (immediate mode) output = 0 if input = 0, output 1 if input !=0
jumpTest2 = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]


def Intcode(PRGM, log = False):
    STEP = 0
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
            VAL = int(input("Input: "))
            STOR = PRGM[STEP+1]
            PRGM[STOR] = VAL
            STEP = STEP + 2

        if OPTCODE == 'OUTPUT':
            if MODE1 == 'POSITIONAL':
                VAL = PRGM[PRGM[STEP+1]]
            else:
                VAL = PRGM[STEP+1]
            outputmessage = 'PROGRAM OUTPUT: {}'
            print(outputmessage.format(VAL))
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
            print('HALT')
            return PRGM

Intcode(prgm)